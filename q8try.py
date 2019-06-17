#!/usr/bin/python3  

import os
k=[]
f=open('commandfile.txt','a+')

while 4>3:
	data=input("Enter Command-->>> ")
	if data in k:
		os.system('echo " COMMAND IS REPEATED " | festival --tts ')
	else:
		k.append(data)
		f.write(data)
		os.system(data)


