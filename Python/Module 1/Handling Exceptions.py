#Handling Exceptions

#assert function allows us to "assert" what is valid or invalid
def function1(var1):
    assert(var1 != 0) , "Divide by zero error"
    return 10 / var1

print(function1(5))
print("--------")
#print(function1(0))

try:
    file = open("File.txt", "w")
    file.write("go to python")
except IOError:
    print("file not found")
else:
    print("A ok")
    file.close()