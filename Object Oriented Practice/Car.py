'''
Created on Feb 16, 2018

@author: ckont
'''


class Car:
    "Class documentation and stuff goes here"
    "it can be printed using ClassName.__doc__"
    
    # instance vars, default values
    color = "null"
    value = 0
    miles = 0
    used = False
    
    # methods all need the have self as a parameter
    # constructor
    def __init__(self, color, value, miles, used):
        self.color = color
        self.value = value
        self.miles = miles
        self.used = used

    def drive(self, miles):
        self.miles += miles

    def paintJob(self, newColor):
        color = newColor
        if newColor == "red":
            value += 500
        elif newColor == "blue":
           value += 1000
        elif newColor == "white":
            value += 1500
    
    def calculateUsedValue(self, orig):
        value = orig - (miles / 10)
        
        
