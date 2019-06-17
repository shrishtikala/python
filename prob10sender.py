#!/usr/bin/python2

import socket
recv_ip="127.0.0.1"
recv_port=4444  #0-1024 --> you can check free udp port netstat -nulp


# creating udp socket
# ip type ip v4, ipv6    ; uDp



s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
num=int(raw_input("enter no 1 for messaging and 2 for sending file   :-----"))


if num == 1:
	while 4>3:

		msg=raw_input("plz enter ur msg:  ")

		# sending data to receiver

		s.sendto(msg,(recv_ip,recv_port))
		print(s.recvfrom(10))


elif num==2:
	f=open('filee.txt','r')
	f1 = f.read()
	s.sendto(f1,(recv_ip,recv_port))
	
