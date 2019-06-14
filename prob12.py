#!/usr/bin/python3
import time
import webbrowser
import pyqrcode 
from pyqrcode import QRCode

from googlesearch import search

data=input("search-->")

url=[]
for i in search(data,stop=3):
	time.sleep(1)
	url.append(i)
	print(i)


	qrc=pyqrcode.create(i)
	qrc.svg("qr1.svg",scale=8)
	print(qrc.terminal())
