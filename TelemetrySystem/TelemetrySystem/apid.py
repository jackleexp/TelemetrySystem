#coding:utf-8

from construct import *

all_apid = {
	0x0401:{
	"len":135 + 6,
	"struct":
		Struct(
		"byte1" / BitStruct(
			"PV_A_+X1_PG" / BitsInteger(1),
			"PV_A _-X1_PG" / BitsInteger(1),
			"PV_A _+X2_PG" / BitsInteger(1),
			"PV_A _-X2_PG" / BitsInteger(1),
			"Solar_Bus1_A_Current" / BitsInteger(12)),
		"byte2" / BitStruct(
			"PV_B_+X1_PG" / BitsInteger(1),
			"PV_B _-X1_PG" / BitsInteger(1),
			"PV_B _+X2_PG" / BitsInteger(1),
			"PV_B _-X2_PG" / BitsInteger(1),
			"Solar_Bus2_A_Current" / BitsInteger(12)),
		"byte3" / BitStruct(
			"BAT_A _ON _PG1" / BitsInteger(1),
			"BAT_A _ON _PG2" / BitsInteger(1),
			"BAT_A _ON _PG3" / BitsInteger(1),
			"BAT_A _ON _PG4" / BitsInteger(1),
			"Solar_Bus1_B_Current" / BitsInteger(12)),
		"byte3-1" / BitStruct(
			"BAT_B _ON _PG1" / BitsInteger(1),
			"BAT_B _ON _PG2" / BitsInteger(1),
			"BAT_B _ON _PG3" / BitsInteger(1),
			"BAT_B _ON _PG4" / BitsInteger(1),
			"Solar_Bus2_B_Current" / BitsInteger(12)),
		"BAT1_A_YC" / Int8ub,
		"BAT2_A_YC" / Int8ub,
		"BAT3_A_YC" / Int8ub,
		"BAT4_A_YC" / Int8ub,
		"BAT1_B_YC" / Int8ub,
		"BAT2_B_YC" / Int8ub,
		"BAT3_B_YC" / Int8ub,
		"BAT4_B_YC" / Int8ub,
		"byte4" / BitStruct (
			"start_type" / BitsInteger(4),
			"V_BUS_A_Current" / BitsInteger(12)
			) ,
		"V_BUS_A _YC" / Int8ub,
		"5V_BUS_A _YC" / Int8ub,
		"5V_BUS1_YC" / Int8ub,
		"byte5" / BitStruct(
			"TmTcCheckCounter" / BitsInteger(4),
			"V_BUS_B_Current" / BitsInteger(12)
			),
		"5V_BOOST_YC" / Int8ub,  #22
		"byte6" / BitStruct(
			"start_counter" / BitsInteger(4),
			"5V_BOOST_CUR" / BitsInteger(12)
			),
		"9V_BOOST_YC" / Int8ub,
		"byte7" / BitStruct(
			"last_error_code" / BitsInteger(4),
			"9V_BOOST_CUR" / BitsInteger(12)
			),    #27
		"3.3V_LDO_YC" / Int8ub,
		"3.3V_CPU_YC" / Int8ub,
		"3.3V_CPU" / Int8ub,
		"3.3V_CPU_B" / Int8ub,
		"exception_type" / Int8ub,
		"reset_type" / Int8ub,
		"TC_correct_count" / Int8ub,
		"TC_error_count" / Int8ub,
		"TC_check_error_count" / Int8ub,
		"TC_head_error_count" / Int8ub,
		"TC_illegal_error_count" / Int8ub,
		"esm_error_code" / Int8ub,
		"Delay_cmd_count" / Int8ub,   #40
		"byte8" / BitStruct(
			"dt_work_mode" / BitsInteger(3),
			"reserve" / BitsInteger(1),
			"BAT_TEMP_A" / BitsInteger(12)
			),
		"byte9" / BitStruct(
			"ram1status" / BitsInteger(2),
			"reserve" / BitsInteger(2),
			"BAT_TEMP_B" / BitsInteger(12)
			),
		"byte10" / BitStruct(
			"ram2status" / BitsInteger(2),
			"reserve" / BitsInteger(2),
			"heatAstatus" / BitsInteger(12)
			),
		"byte11" / BitStruct(
			"ram3status" / BitsInteger(2),
			"reserve" / BitsInteger(2),
			"heatBstatus" / BitsInteger(12)
			),	
		"UV_3.3V" / Int8ub,
		"byte12" / BitStruct(
			"ram4status" / BitsInteger(2),
			"reserve" / BitsInteger(2),
			"UV_3.3_Current" / BitsInteger(12)
			),
		"IMU1_supply" / Int8ub,
		"IMU1_current" / Int16ub,
		"5V_IMU2_YC" / Int8ub,
		"GPS_5V_YC" / Int8ub,
		"MTQ_5V_YC" / Int8ub,
		"MX-current-YC" / Int16ub,
		"MY-current-YC" / Int16ub,
		"MZ-current-YC" / Int16ub,   #67
		"byte13" / BitStruct(
			"reserve" / BitsInteger(3),
			"rw_1_speed" / BitsInteger(13)
			),
		"byte14" / BitStruct(
			"reserve" / BitsInteger(3),
			"rw_2_speed" / BitsInteger(13)
			),
		"gnc_work_mode" / Int8ub,
		"gnc_control_mode" / Int8ub,
		"imu_supply" / Int16ub,
		"imu1_Xgyro" / Int16ub,
		"imu1_Ygryo" / Int16ub,
		"imu1_Zgryo" / Int16ub,
		"imu1_Xmagn" / Int16ub,
		"imu1_Ymagn" / Int16ub,
		"imu1_Zmagn" / Int16ub,   #87
		"byte15" / BitStruct(
			"adsb_5V_yc" / BitsInteger(1),
			"dt_transmitter_on_off" / BitsInteger(1),
			"imu2_supply" / BitsInteger(14)
			),
		"imu2_Xgyro" / Int16ub,
		"imu2_Ygryo" / Int16ub,
		"imu2_Zgryo" / Int16ub,
		"imu2_Xmagn" / Int16ub,
		"imu2_Ymagn" / Int16ub,
		"imu2_Zmagn" / Int16ub,   #101
		"DCS_5V_YC" / Int8ub,
		"AIS_3.3V" / Int8ub,
		"DCS_3.3V_YC" / Int8ub,
		"AIS_decode_count" / Int16ub,
		"ADS-B_decode_count" / Int16ub,
		"DCS_decode_count" / Int16ub,
		"channel_401p8_decode_count" / Int16ub,
		"channel_402p2_decode_count" / Int16ub,
		"channel_402p4_decode_count" / Int16ub,
		"DT_5V_YC" / Int8ub,
		"DT_9V_YC" / Int8ub,
		"dt_power" / Int8ub,
		"dt_temp" / Int8ub,   #120
		"gnss_capture_time" / Int32ub,
		"gnss_pos_x" / Int32ub,
		"gnss_pos_y" / Int32ub,
		"gnss_pos_z" / Int32ub,
		"error_log_count" / Int8ub
		),
		"transform":{
		"PV_A_+X1_PG" : "'TRUE' if x==1 else 'FALSE'",
		"PV_A _-X1_PG" : "'TRUE' if x==1 else 'FALSE'",
		"PV_A _+X2_PG" : "'TRUE' if x==1 else 'FALSE'",
		"PV_A _-X2_PG" : "'TRUE' if x==1 else 'FALSE'",
		"Solar_Bus1_A_Current" : "x / 4096.0 * 3.3",
		"PV_B_+X1_PG" : "'TRUE' if x==1 else 'FALSE'",
		"PV_B _-X1_PG" : "'TRUE' if x==1 else 'FALSE'",
		"PV_B _+X2_PG" : "'TRUE' if x==1 else 'FALSE'",
		"PV_B _-X2_PG" : "'TRUE' if x==1 else 'FALSE'",
		"Solar_Bus2_A_Current" : "x / 4096.0 * 3.3",
		"BAT_A _ON _PG1" : "'TRUE' if x==1 else 'FALSE'",
		"BAT_A _ON _PG2" : "'TRUE' if x==1 else 'FALSE'",
		"BAT_A _ON _PG3" : "'TRUE' if x==1 else 'FALSE'",
		"BAT_A _ON _PG4" : "'TRUE' if x==1 else 'FALSE'",
		"Solar_Bus1_B_Current" : "x / 4096.0 * 3.3",
		"BAT_B _ON _PG1" : "'TRUE' if x==1 else 'FALSE'",
		"BAT_B _ON _PG2" : "'TRUE' if x==1 else 'FALSE'",
		"BAT_B _ON _PG3" : "'TRUE' if x==1 else 'FALSE'",
		"BAT_B _ON _PG4" : "'TRUE' if x==1 else 'FALSE'",
		"Solar_Bus2_B_Current" : "x / 4096.0 * 3.3",
		"BAT1_A_YC" : "x / 256.0 * 3.3 * 2.0",
		"BAT2_A_YC" : "x / 256.0 * 3.3 * 2.0",
		"BAT3_A_YC" : "x / 256.0 * 3.3 * 2.0",
		"BAT4_A_YC" : "x / 256.0 * 3.3 * 2.0",
		"BAT1_B_YC" : "x / 256.0 * 3.3 * 2.0",
		"BAT2_B_YC" : "x / 256.0 * 3.3 * 2.0",
		"BAT3_B_YC" : "x / 256.0 * 3.3 * 2.0",
		"BAT4_B_YC" : "x / 256.0 * 3.3 * 2.0",
		"start_type" : u"SWITCH0x11:上电,0x22:晶振失效复位,0x44:看门狗复位,0x88:仿真器复位,0x99:CPU复位,0xAA:软件复位,0x55:外部复位按钮复位,0x0:未知复位,0x1:上电,0x2:晶振失效复位,0x4:看门狗复位,0x8:仿真器复位,0x9:CPU复位,0xA:软件复位,0x5:外部复位按钮复位",
 		"V_BUS_A_Current" : "x / 4096.0 * 3.3",
		"V_BUS_A _YC" : "x / 256.0 * 3.3 * 2.0",
		"5V_BUS_A _YC" : "x / 256.0 * 3.3 * 2.0",
		"5V_BUS1_YC" : "x / 256.0 * 3.3 * 2.0",
		"TmTcCheckCounter" : "DISPLAY%d",
		"V_BUS_B_Current" : "x / 4096.0 * 3.3",
		"5V_BOOST_YC" : "x / 256.0 * 3.3 * 2.0",  #22
		"start_counter" : "DISPLAY%d",
		"5V_BOOST_CUR" : "x / 4096.0 * 3.3 * 2.0",
		"9V_BOOST_YC" : "x / 256.0 * 5.0 * 3.0",
		"last_error_code" : "DISPLAY%d", 
		"9V_BOOST_CUR" : "x / 4096.0 * 5.0 * 2.0",    #27
		"3.3V_LDO_YC" : "x / 256.0 * 3.3 * 2.0",
		"3.3V_CPU_YC" : "x / 256.0 * 3.3",
		"3.3V_CPU" : "x / 256.0 * 3.3 * 2.0",
		"3.3V_CPU_B" : "x / 256.0 * 3.3 * 2.0",
		"exception_type" : "DISPLAY%d",  
		"reset_type" : u"SWITCH0x11:上电,0x22:晶振失效复位,0x44:看门狗复位,0x88:仿真器复位,0x99:CPU复位,0xAA:软件复位,0x55:外部复位按钮复位,0x0:未知复位,0x1:上电,0x2:晶振失效复位,0x4:看门狗复位,0x8:仿真器复位,0x9:CPU复位,0xA:软件复位,0x5:外部复位按钮复位",
		"TC_correct_count" : "DISPLAY%d",
		"TC_error_count" : "DISPLAY%d",
		"TC_check_error_count" : "DISPLAY%d",
		"TC_head_error_count" : "DISPLAY%d",
		"TC_illegal_error_count" : "DISPLAY%d",
		"esm_error_code" : "DISPLAY0x%x",
		"Delay_cmd_count" : "DISPLAY%d",   #40
		"dt_work_mode" : u"SWITCH0x0:待机,0x1:擦除,0x2:记录,0x3:回放,0x4:测试,0x5:单载波,0x6:非法,0x7:非法",
		"reserve" : "",
		"BAT_TEMP_A" : "x * 196.078- 273.0",
		"ram1status" : u"SWITCH0x0:待机,0x1:记录,0x2:回放,0x3:擦除",  
		"reserve" : "",
		"BAT_TEMP_B" : "x * 196.078- 273.0",
		"ram2status" : u"SWITCH0x0:待机,0x1:记录,0x2:回放,0x3:擦除",
		"reserve" : "",
		"heatAstatus" : "x / 4096 * 5.0",
		"ram3status" : u"SWITCH0x0:待机,0x1:记录,0x2:回放,0x3:擦除",
		"reserve" : "",
		"heatBstatus" : "x / 4096 * 5.0",	
		"UV_3.3V" : "x / 256.0 * 3.3 * 2.0",
		"ram4status" : u"SWITCH0x0:待机,0x1:记录,0x2:回放,0x3:擦除",
		"reserve" : "",
		"UV_3.3_Current" : "x / 4096.0 * 3.3",
		"IMU1_supply" : "x / 256.0 * 3.3 * 2.0",
		"IMU1_current" : "x / 4096.0 * 3.3",
		"5V_IMU2_YC" : "x / 256.0 * 3.3 * 2.0",
		"GPS_5V_YC" : "x / 256.0 * 3.3 * 2.0",
		"MTQ_5V_YC" : "x / 256.0 * 3.3 * 2.0",
		"MX-current-YC" : "x / 4096.0 * 5.0 - 1.33",
		"MY-current-YC" : "x / 4096.0 * 5.0 - 1.33",
		"MZ-current-YC" : "x / 4096.0 * 5.0 - 1.33",   #67
		"reserve" : "",
		"rw_1_speed" : "DISPLAY%d",
		"reserve" : "",
		"rw_2_speed" : "DISPLAY%d",
		"gnc_work_mode" : u"SWITCH0x0:空闲,0x1:Bdot阻尼,0x10:转移,0x7F:三轴稳定",
		"gnc_control_mode" : u"SWITCH0x0:空闲,0x1:Bdot阻尼,0x10:转移,0x7F:三轴稳定",
		"imu_supply" : "(x & 0x3FFF) * 0.002418",
		"imu1_Xgyro" : "((x & 0x3FFF) * 0.05) if ((x & 0x3FFF) < 0x2000) else (((~(x & 0x3FFF) & 0x3FFF) + 1) * (-0.05))",
		"imu1_Ygryo" : "((x & 0x3FFF) * 0.05) if ((x & 0x3FFF) < 0x2000) else (((~(x & 0x3FFF) & 0x3FFF) + 1) * (-0.05))",
		"imu1_Zgryo" : "((x & 0x3FFF) * 0.05) if ((x & 0x3FFF) < 0x2000) else (((~(x & 0x3FFF) & 0x3FFF) + 1) * (-0.05))",
		"imu1_Xmagn" : "((x & 0x3FFF) * 0.0005) if ((x & 0x3FFF) < 0x2000) else (((~(x & 0x3FFF) & 0x3FFF) + 1) * (-0.0005))",
		"imu1_Ymagn" : "((x & 0x3FFF) * 0.0005) if ((x & 0x3FFF) < 0x2000) else (((~(x & 0x3FFF) & 0x3FFF) + 1) * (-0.0005))",
		"imu1_Zmagn" : "((x & 0x3FFF) * 0.0005) if ((x & 0x3FFF) < 0x2000) else (((~(x & 0x3FFF) & 0x3FFF) + 1) * (-0.0005))",   #87
		"adsb_5V_yc" : "'TRUE' if x==1 else 'FALSE'",
		"dt_transmitter_on_off" : "'TRUE' if x==1 else 'FALSE'",
		"imu2_supply" : "(x & 0x3FFF) * 0.002418",
		"imu2_Xgyro" : "((x & 0x3FFF) * 0.05) if ((x & 0x3FFF) < 0x2000) else (((~(x & 0x3FFF) & 0x3FFF) + 1) * (-0.05))",
		"imu2_Ygryo" : "((x & 0x3FFF) * 0.05) if ((x & 0x3FFF) < 0x2000) else (((~(x & 0x3FFF) & 0x3FFF) + 1) * (-0.05))",
		"imu2_Zgryo" : "((x & 0x3FFF) * 0.05) if ((x & 0x3FFF) < 0x2000) else (((~(x & 0x3FFF) & 0x3FFF) + 1) * (-0.05))",
		"imu2_Xmagn" : "((x & 0x3FFF) * 0.0005) if ((x & 0x3FFF) < 0x2000) else (((~(x & 0x3FFF) & 0x3FFF) + 1) * (-0.0005))",
		"imu2_Ymagn" : "((x & 0x3FFF) * 0.0005) if ((x & 0x3FFF) < 0x2000) else (((~(x & 0x3FFF) & 0x3FFF) + 1) * (-0.0005))",
		"imu2_Zmagn" : "((x & 0x3FFF) * 0.0005) if ((x & 0x3FFF) < 0x2000) else (((~(x & 0x3FFF) & 0x3FFF) + 1) * (-0.0005))",   #101
		"DCS_5V_YC" : "x / 256.0 * 5.0 * 2.0",
		"AIS_3.3V" : "x / 256.0 * 3.3",
		"DCS_3.3V_YC" : "x / 256.0 * 5.0 *2.0",
		"AIS_decode_count" : "DISPLAY%d",
		"ADS-B_decode_count" : "DISPLAY%d",
		"DCS_decode_count" : "DISPLAY%d",
		"channel_401p8_decode_count" : "DISPLAY%d",
		"channel_402p2_decode_count" : "DISPLAY%d",
		"channel_402p4_decode_count" : "DISPLAY%d",
		"DT_5V_YC" : "x / 256.0 * 5.0 * 2.0",
		"DT_9V_YC" : "x / 256.0 * 5.0 * 3.0",
		"dt_power" : "DISPLAY0x%x",
		"dt_temp" : "DT_TEMP",   #120
		"gnss_capture_time" : "TIME2017-1-1 0:0:0",
		"gnss_pos_x" : "x * 0.1",
		"gnss_pos_y" : "x * 0.1",
		"gnss_pos_z" : "x * 0.1",
		"error_log_count" : "DISPLAY%d"
		}
	}
}