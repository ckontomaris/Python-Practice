'''
Created on Feb 16, 2018

@author: ckont
'''
#we need to import the car class
from Car import *


corolla = Car("white", 15000, 0, False)
yarris = Car("blue", 12000, 0, True)

print(corolla.color)

#printing the documentation
print(Car.__doc__)