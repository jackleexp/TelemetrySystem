#coding:utf-8
import sys
import serial
import socket
import time

SERIALPORT = "COM1"
BAUDRATE = 9600
parity = serial.PARITY_NONE

server_ip = "127.0.0.1"
server_port = 60060

ser = serial.serial_for_url(SERIALPORT, do_not_open=True)
ser.baudrate = BAUDRATE
ser.parity = parity
ser.timeout = None

try:
   ser.open()
except serial.SerialException as e:
   sys.stderr.write('Could not open serial port {}: {}\n'.format(ser.name, e))
   sys.exit(1)
   

while True:
	try:
		sys.stderr.write("Opening connection to {}:{}...\n".format(server_ip, server_port))
		client_socket = socket.socket()
		try:
			client_socket.connect((server_ip, server_port))
		except socket.error as msg:
			sys.stderr.write('WARNING: {}\n'.format(msg))
			time.sleep(5)  # intentional delay on reconnection as client
			continue
		sys.stderr.write('Connected\n')
		client_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
		
		#~ client_socket.settimeout(5)
	except AttributeError:
		pass # XXX not available on windows


	try:
		while True:
			try:
				data = ser.read(220)
				if not data:
					continue
				sys.stderr.write("Recv one pack from serial\n")
				client_socket.send(data)
			except serial.SerialException as msg:
				sys.stderr.write("ERROR: {} \n".format(msg))

	except KeyboardInterrupt:
		sys.stderr.write("User abort\n")
	except socket.error as msg:
		sys.stderr.write("ERROR: {}\n".format(msg))
	finally:
		sys.stderr.write("Disconnected\n")
		client_socket.close()
	