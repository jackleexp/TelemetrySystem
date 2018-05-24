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
		)
	}
}