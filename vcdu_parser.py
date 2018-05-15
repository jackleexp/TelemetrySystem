#coding:utf-8

from construct import *


vcdu = Struct (
	"head" / BitStruct (
		"ver" / BitsInteger(2), 
		"scid" / BitsInteger(8),
		"vcid" / BitsInteger(6), 
		"vcct" / BitsInteger(24),
		"rk" / BitsInteger(1),
		"fr" / BitsInteger(7)
		),
	"time" / Int32ub,
	"non" / Array(4, Byte),
	"mpdu" / Struct(
		"head" / BitStruct (
			"bk" / BitsInteger(5),
			"ptr" / BitsInteger(11)
			),
		"data" / Array(204, Byte)
		)
)