# IF/ELSE (ELSEIF "ELIF")

# Q: Ask 3 numbers from the user and print the largest number

var1 = int(input("INPUT NUMBER 1"))
var2 = int(input("INPUT SECOND NUMBER"))
var3 = int(input("THIRD NUMBER...PLIS"))

if (var1 > var2 and var1 > var3):
    print ("Big brain")
    print (var1, "is the largest number if you didn't know")
elif (var2 > var1 and var2 > var3):
    print (var2, "is greatest")
else: 
    print (var3, "is CHONK")

#Q- ask password and email from the user and if they are correct then print successful login and even if one is wrong print incorrect 
# information
#the correct password should be : 12ab
#the correct email should be : 123@m

var3 = input ("input PASSWORD")
var4 = input ("input EMAIL")

if ("12ab" == var3 and "123@m" == var4):
    print ("successful login")
else: 
    print ("incorrect info")
