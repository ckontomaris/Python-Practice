'''
Created on Feb 16, 2018

@author: ckont
'''
from test.test_binop import isint

#like lists that cannot be changed (immutable)
#use parenthesis are tuples
tupleRandoms= (1, "ayy", 3, 4,5,6,7,"$^%^&")
print(tupleRandoms)

emptyTuple= ();

oneElementTuple= (50,);
print (oneElementTuple)

'''
can still access and slice with brackets
'''

print(tupleRandoms[0])
print(tupleRandoms[1])

#can't do this==>   tupleRandoms[0]= 0

tupleRuple= tupleRandoms+ emptyTuple+ oneElementTuple
print(tupleRuple)

#deletes
del tupleRandoms


#repeat
tupleRepetition= ('hi!',)*4
print(tupleRepetition)


#return length
print(len(tupleRepetition)) 

isIn= (3 in tupleRepetition)
print(isIn)

#notice how we can just have isIn and not isIn==true
if isIn:
    print("yep")
else:
    print("nope")

