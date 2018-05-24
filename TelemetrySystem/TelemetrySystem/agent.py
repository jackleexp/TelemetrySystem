#coding:utf-8
import sys
import serial
import socket
import time
import datetime

SERIALPORT = "COM12"
BAUDRATE = 9600
parity = serial.PARITY_NONE

server_ip = "192.168.1.106"
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


    save_file_name = datetime.datetime.now().strftime("data/%Y-%m-%d_%H%M%S.txt")

    save_file = open(save_file_name, "a+")
    try:
        while True:
            try:
                data = ser.read(220)
                if not data:
                    continue
                sys.stderr.write("{}:Recv one pack from serial\n".format(datetime.datetime.now()))
                save_file.write("{}:{}\n".format(datetime.datetime.now(), data.encode('hex')))
                client_socket.send(data)
            except serial.SerialException as msg:
                sys.stderr.write("ERROR: {} \n".format(msg))
            except KeyboardInterrupt:
                sys.stderr.write("User abort\n")
                break

    except KeyboardInterrupt:
        sys.stderr.write("User abort\n")
    except socket.error as msg:
        sys.stderr.write("ERROR: {}\n".format(msg))
    finally:
        sys.stderr.write("Disconnected\n")
        client_socket.close()
        save_file.close()
    