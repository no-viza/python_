#LOOPS
#Logical operators 

#the AND logical operator. if BOTH coditions are ON/OFF

var1 = True
var2 = True
var3 = False
var4 = False

print("AND logical operator")
print(var1 and var2)
print(var3 and var4)
print(var2 and var3)

#OR Logical operator.Checks even if ONE condition is TRUE 

print("OR logical operator")
print(var1 or var2)
print(var3 or var4)
print(var2 or var3)

#NOT Logical operator.Flips operation 

print("NOT logical operator")
print(not(var1))
print(not(var3))
print(not(var1 or var3))
#First the computer will solve the OR operator (BODMAS) then it will go to the second operator i.e. NOT