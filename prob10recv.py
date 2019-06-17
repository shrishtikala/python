#!/usr/bin/python

import socket
recv_ip="127.0.0.1"
recv_port=4444  #0-1024 --> you can check free udp port netstat -nulp


# creating udp socket
# ip type ip v4, ipv6    ; uDp

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# fitting ip and port with udp socket
s.bind((recv_ip,recv_port))

number=int(raw_input("enter 1 for messaging and 2 for receiving file   :-----"))

if number ==1:
	
	while 4>3:
	# receiving data from sender

		data=s.recvfrom(100)

		print("msg from sender:  ",data[0])
		print("sender ip+port ",data[1])
	#reply to sender

		reply=raw_input("type your reply:   ")
		s.sendto(reply,data[1])
elif number == 2:
	data=s.recvfrom(100)
	print(data)	

s.close()
