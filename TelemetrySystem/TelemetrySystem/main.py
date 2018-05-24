#coding:utf-8

import socket
import traceback
import datetime
from vcdu_parser import *
from apid import all_apid
from elasticsearch import Elasticsearch
import datetime

base_time = datetime.datetime(2018, 5, 1, 0, 0, 0)

es = Elasticsearch(http_auth=('elastic', '0zO8MRnXd0oMK98Sihd7'))

es.indices.create(index='3s_tm_index', ignore=400)


def send_data_to_elastic(key, value, time):
    if key == "_io" or key == "reserve":
        return 

    single_data = {}
    single_data["timestamp"] = datetime.datetime.now()
    single_data["satellite_time"] = (base_time + datetime.timedelta(seconds=time))
    single_data["name"] = key
    single_data["value"] = value
    #print single_data
    es.index(index="3s_tm_index",doc_type="telemetry",body=single_data)



# tm_data: dict
def save_data(tm_data, time):
    tm_dict = dict(tm_data)
    for key,value in tm_dict.items():
        if key.find("byte") == -1:
            send_data_to_elastic(key, value, time)
        else:
            for k,v in value.items():
                send_data_to_elastic(k, v, time)
    print ("Done")




def parse_epdu(byte_list, apid, time):
    epdu_str = GreedyRange(Byte).build(byte_list)
    print ("%d,%d" % (len(byte_list), len(epdu_str)))
    print (epdu_str.encode("hex"))
    try:
        tm_data = all_apid[apid]["struct"].parse(epdu_str)
        save_data(tm_data, time)
    except Exception as e:
        print ("Error:%s" % e)


if __name__ == "__main__":
    last_vc_num = 0
    last_time = 0
    last_remain_data = b""

    while True:
        try:
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_address = ('0.0.0.0', 60060)
            server.bind(server_address)
            server.listen(10)
            print ("Begin to listen port %d" % 60060)
            conn, addr = server.accept()
            print ("Client %s connected" % str(addr))
            while True:
                if conn:
                    data = conn.recv(220)
                    print ("****************************************************************************************")
                    print ("%s:%s" % (datetime.datetime.now(), data.encode("hex")))
                    vcdu_parsered_data = vcdu.parse(data)

                    time = vcdu_parsered_data.time
                    curr_vc_num = vcdu_parsered_data.head.vcct

                    print (time)
                    first_epdu_ptr = vcdu_parsered_data.mpdu.head.ptr
                    if len(last_remain_data) > 0 and curr_vc_num == ((last_vc_num + 1) & 0xFFFFFF):
                        #帧号连续，且上一帧有未完全的数据,则拼帧
                        print(u"帧号连续，且上一帧有%d字节未完全的数据,拼帧" % len(last_remain_data))
                        tail_data = vcdu_parsered_data.mpdu.data[0:vcdu_parsered_data.mpdu.head.ptr]
                        epdu_data = last_remain_data + tail_data
                        print (u"拼后数据长度=%d,本次可用数据长度=%d" % (len(epdu_data), len(tail_data)))
                        time = last_time
                        last_remain_data = b""
                    else:
                        #帧号不连续或者没有剩余数据
                        print(u"帧号不连续或者没有剩余数据")
                        last_remain_data = b""
                        
                        first_epdu_apid = (vcdu_parsered_data.mpdu.data[vcdu_parsered_data.mpdu.head.ptr] * 256 + vcdu_parsered_data.mpdu.data[vcdu_parsered_data.mpdu.head.ptr + 1])
                        first_epdu_len = all_apid[first_epdu_apid]["len"]
                        #提取第一个EPDU的数据
                        print ("ptr=%d,apid=%.4x,len=%d,struct_size=%d" % (first_epdu_ptr, first_epdu_apid, first_epdu_len, all_apid[first_epdu_apid]["struct"].sizeof()))
                        epdu_head = vcdu_parsered_data.mpdu.data[first_epdu_ptr:first_epdu_ptr + 6]
                        epdu_data = vcdu_parsered_data.mpdu.data[first_epdu_ptr+6:first_epdu_ptr + first_epdu_len]

                    if (len(epdu_data) + 6) == first_epdu_len:
                        #如果本次epdu拿到的数据全，则解析
                        print(u"本次epdu拿到的数据全，则解析")
                        parse_epdu(epdu_data, first_epdu_apid, time)
                    else:
                        #数据不全，暂存
                        print(u"数据不全，暂存%d字节" % len(epdu_data))
                        last_remain_data = epdu_data
                    
                    last_time = time
                    last_vc_num = curr_vc_num

        except Exception as e:
            print("Error:{}".format(e))
            traceback.print_exc()


