import sys
import serial
OP=sys.argv[1]
PORT=sys.argv[2]
try:
	MSG=sys.argv[3]
except:
	MSG=""
try:
	if(OP=='command' or OP=='send' or OP=='request'):
		lenghtMSG = len(MSG)
		size = hex(lenghtMSG).replace('0x','')
		if lenghtMSG < 16:
			size = '0'+size
		MSG = 'fffe'+size+MSG
	if(OP=='command' or OP=='send'):
		comm = serial.Serial(PORT, 9600, timeout=None)
		comm.open
		comm.isOpen
		comm.write(bytes(MSG, 'utf-8'))
		comm.close
	if(OP=='request' or OP=='listen'):
		comm = serial.Serial(PORT, 9600, timeout=3)
		comm.open
		comm.isOpen
		if OP=='request':
			comm.write(bytes(MSG, 'utf-8'))
		preamble = comm.read(4)
		if preamble == b'fffe':
			lenght = comm.read(2)
			integer = int(lenght.decode(), 16)
			message = comm.read(integer)
			if integer == len(message):
				print (message.decode())
			else:
				sys.exit(1)
		else:
			sys.exit(1)
		comm.close
except:
	print ("Error on connect "+PORT)
	sys.exit(1)
