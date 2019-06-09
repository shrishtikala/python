#!/usr/bin/python3

adhoc = [1,2,3,1,4,5,66,22,2,6,0,9]
no1=[]
no2=[]
print("Print numbers greater than 5 \n")
for i in adhoc:
	if i > 5:
		no1.append(i)
print(no1)
		


print("numbers less than and equal to 2 \n")

for i in adhoc:
	if i <= 2:
		no2.append(i)

print(no2)
