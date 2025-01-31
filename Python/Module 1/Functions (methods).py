#Functions/Methods

def varfunction():
    "the function prints strings"
    print("this computer")
    print("is nice")
    return

#calling a function
varfunction()
varfunction()

def function2(num1, num2):
    "multiples the 2 numbers"
    return num1 * num2

print(function2(7, 9))

def defaultval(var = 8):
    return var / 2

#as we dont insert a value in the 2nd one, it will automatically input 8 in it
#(continued) as a DEFAULT
print(defaultval(126))
print(defaultval())

#all DEFAULT argument should be written in the end if multiple arguments are used
def multiarg(var1, var2, var3 = 9):
    return var1 + var2 + var3 * 6
print(multiarg(4, 6, ))
