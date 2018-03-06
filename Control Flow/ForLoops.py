'''
Created on Feb 16, 2018

@author: ckont
'''
#iterates over the items of any sequence (list or string)
#iterates in the order that they appear in the sequence

#this prints 1 to 5, but does NOT include 6
for counter in range (1,6):
    print (counter)
    
    
counterList= [6, 7,8,9,10]
    
for count in counterList:
    print (count)
    
    
#strings are sequences, so it works like this too
word = "computer"

for letter in word:
    print("ayy lmao:", letter)