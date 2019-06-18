#!/usr/bin/python2

import socket
recv_ip="127.0.0.1"
recv_port=4444  #0-1024 --> you can check free udp port netstat -nulp


# creating udp socket
# ip type ip v4, ipv6    ; uDp

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while 4>3:

	msg=raw_input("plz enter ur msg:  ")

# sending data to receiver

	s.sendto(msg,(recv_ip,recv_port))
	l=s.recvfrom(150)
	if len(l[0]) >= 150:
		print("error")
	else:
		print("reply: " +l[0])
		

		
	a=raw_input("want to quit yes or no :")
	if a == "yes":
		s.sendto("bye",(recv_ip,recv_port))
		exit()
