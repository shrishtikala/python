#!/usr/bin/python3

import os
u = input("enter name:")

if type(u)==str:
	password = "hello" +u
	os.system("useradd -p $(openssl passwd -1 "+password +") "+u)
	print("user created")

else:
	print("invalid username")
