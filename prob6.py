#!/usr/in/python3
option='''
press 1 for cat 
press 2 for cat -n
press 3 for cat -e
press 4 for cat text >text
'''


print(option)

choice=input()

if choice == '1':
	f=open('fh1.txt','r')
	data = f.read()
	print(data)
	f.close()

elif choice == '2':

	f=open('fh1.txt','r')

	count=0
	for i in f:
		count=count+1
		print(str(count) +" "+ i.strip())
	f.close()
elif choice == '3':

	f=open('fh1.txt','r')

	for i in f:
		print(i.strip()+"$")
	f.close()

elif choice == '4':
	f=open('fh1.txt','r')
	f2=open('fh2.txt','w')
	r1=f.read()
	f2.write(r1)
	print(f2)

	f2.close()
	
		

	


