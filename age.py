#!/usr/bin/python3


import time
from datetime import date
name = input("Name-->")
age = int(input("Age-->")) 

print("current age of "+name+" is -->")
print(age)

today=date.today()



maxi=95
count=(len(range(age,maxi,1)))

	
print(name+" will turn 95 in year -->")
print(today.year+count)




