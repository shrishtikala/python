#!/usr/bin/python

import socket
recv_ip="127.0.0.1"
recv_port=4444  #0-1024 --> you can check free udp port netstat -nulp


# creating udp socket
# ip type ip v4, ipv6    ; uDp

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# fitting ip and port with udp socket
s.bind((recv_ip,recv_port))
while 4>3:
	# receiving data from sender

	data=s.recvfrom(150)
	if len(data[0])==150:
		print("error")

	print("msg from sender:  ",data[0])
	print("sender ip+port ",data[1])
	#reply to sender
	if data[0] == "bye":
		exit()

	reply=raw_input("type your reply:   ")
	s.sendto(reply,data[1])
	

s.close()
