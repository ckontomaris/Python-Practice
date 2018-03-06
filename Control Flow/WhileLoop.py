'''
Created on Feb 16, 2018

@author: ckont
'''

# does something as long as condition is met

population = 2;
x=1

while population < (pow(2, 100)):
    population = population ** 2
    print (population)
    x=x+1

print("oh no, the population is \nTOO BIG")
print("after", x, "years, the population became",population)