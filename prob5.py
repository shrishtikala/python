#!/usr/bin/python


import datetime 

name=input("Name-->")

ct=datetime.datetime.now()


if ct.hour < 12:
	print("Good morning "+name)

elif 12 <= ct.hour < 17:
	print("Good afternoon "+name)

elif 17 <= ct.hour < 20:
	print("Good evening "+name)

else:
	print("Good night "+name)
