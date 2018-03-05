'''
Created on Feb 16, 2018

@author: ckont
'''
squares= []
#for loop will include 0 and 7
#notice use of insert
for number in [0,1,2,3,4,5,6,7]:
    squares.insert(number, (number**2))
    
print(squares)