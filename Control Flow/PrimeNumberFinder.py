'''
Created on Feb 16, 2018

@author: ckontomaris
'''
for n in range(2, 50):
     for x in range(2, n):
        if n % x == 0:
             print (n, 'is', x, '*', n/x)
             break
     else:
         # loop fell through without finding a factor
         print (n, 'is a prime number')
         pass #does nothing