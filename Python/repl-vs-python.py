number = 174
dept = "cmput"
dept
number

#proving print is an identifier
newWord = print
newWord(9)

#Exercise
#time is a module
#in python, "=" is delimiter

import time
#age = input("What is the legal driving age in Canada?")
#time.sleep(1.5)
#time=identifier
#"time"."= delimiter
#print(age)

#identity
a = 5
b = a
print(id(a))
print(id(b))

a = 10
print(id(a))
print(id(b))
#id of a changed in the second test

#'.upper()' is a method

x = "why"
print (x.upper())

#the importance of NONE is to make sure that the expression 
#that doesnt need to be evaluated does not get presented

#print can be given 0 argument while funtions like lenght [len()] CANNOT
len(x)

multistring = '''
This is considered a multi-line string. you can use it to write multi-line 
comments as well but it is essentially a multi-line string.
'''
