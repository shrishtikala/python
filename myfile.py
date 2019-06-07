#!/usr/bin/python3
import time
import os
import subprocess
import webbrowser


option='''

press 1 to start something from this os
press 2 to play fav song on youtube
press 3 to search something on google 
press 4 to send whatsapp to fav no 
press 5 to check current time and date
press 6 to reboot


'''

print(option)
choice = input()



if choice == '1' :
	#to start something from the os
	os.system('vlc')
elif choice == '2':
	#fav. youtube video
	url = "https://www.youtube.com/watch?v=dhYOPzcsbGM"
	c=webbrowser.get()
	c.open(url)
	
elif choice == '3':
	#for google search
	data =input("search -->>")
	webbrowser.open_new_tab("https://www.google.com/search?q="+data)

elif choice =='5':
	#for current time
	print(time.ctime())
elif choice == '6':
	#to reboot
	os.system("shutdown /s /t 1");


else :
	print("bye")





	
