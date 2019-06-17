#!/usr/bin/python3

import operator

user = input('enter input -->')

if(len(user)>500):
	print("not allowed")


freq={}
for i in user:

	
	if i in freq.keys():
		
		freq[i] =freq[i]+1
		
		
	
	else:
		freq[i]=1

sorted_d = sorted(freq.items(),reverse=True)
print('repeated characters dec order')
print(sorted_d)


words=user.split()
wordfreq={}
for a in words:
	if a not in wordfreq:
		wordfreq[a]=1
	else:
		wordfreq[a]=wordfreq[a]+1

print(wordfreq)






