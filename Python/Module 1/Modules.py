#Modules

#Modules allow user to oragnise their code
#modules allows you to import functions

#importing/includinga module
import math
import time
#"math", "time" is the module
print(math.pi)

#if you want to import a certain function from the module
#from [module name] import [function]
from math import sin, pi
print(sin (pi/2))
 
#"dir" or directory is all the contents of the module
contents = dir(math)
print(contents)

print("----------")

contents2 = dir(time)
print(contents2)

