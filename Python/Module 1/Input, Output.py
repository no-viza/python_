#File Input/Output 

import os 

#output 
print("I'm a Dell")

#input
#var1 = input("enter name: ")
#print(var1)

#will make a text file if it does not previously exist
# w = writeable
# r = readable 

var2 = open("file.txt", "r+")
print(var2)
print(var2.name)

print("-----")

#to write something in that file
#var2.write("hello aDell")

#reading (specifying the bytes)
string1 = var2.read(50)
print(string1)

#closing the file
var2.close()

#renaming a file
#os.rename("File.txt", "new text file.txt")

#removing a file
#os.remove("Filelocation" and "filename")

#creating a folder/directory
#os.mkdir("new folder")
