#coding:utf-8

import socket
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
                    print ("%s:%s" % (datetime.datetime.now(), data.hex()))
                    vcdu_parsered_data = vcdu.parse(data)

                    time = vcdu_parsered_data.time
                    print (time)
                    first_epdu_ptr = vcdu_parsered_data.mpdu.head.ptr
                    first_epdu_apid = (vcdu_parsered_data.mpdu.data[vcdu_parsered_data.mpdu.head.ptr] * 256 + vcdu_parsered_data.mpdu.data[vcdu_parsered_data.mpdu.head.ptr + 1])
                    first_epdu_len = all_apid[first_epdu_apid]["len"]

                    print ("ptr=%d,apid=%.4x,len=%d,struct_size=%d" % (first_epdu_ptr, first_epdu_apid, first_epdu_len, all_apid[first_epdu_apid]["struct"].sizeof()))
                    epdu_head = vcdu_parsered_data.mpdu.data[first_epdu_ptr:first_epdu_ptr + 6]
                    epdu_data = vcdu_parsered_data.mpdu.data[first_epdu_ptr+6:first_epdu_ptr + first_epdu_len]
                    parse_epdu(epdu_data, first_epdu_apid, time)
        except Exception as e:
            print("Error:{}".format(e))




