#Loops

#loops are a piece of functionality that allow you to iterate a code multiple times

var1 = "help"
var2 = 390
var3 = "Appa Binte Nofal"

for character in var1:
    print(character)
#the LHS (left hand side) is what you are getting from the RHS
#the above loop states that for each character in var1, print it

while (var2 < 400):
    print (var2)
    var2 += 1
    print (var2)
else:
    print("var2 is equal to 400")

#Nesting loops: meaning to add another loop within a loop

print("-------")

#LOOP CONTROL STATEMENTS

for character in var3:
    if character == "B":
        print ("First name ONLY")
        break

    print(character)
#break will stop the loop after the condition is fulfilled

print ("------")


for character in var3:
    if character == "B":
        continue
    elif character == "i":
        continue
    elif character == "n":
        continue
    elif character == "t":
        continue
    elif character == "e":
        continue
    print(character)
#continue will continue the loop after fulfilling the condition 

print("------")


for character in var3:
    if character == "B":
        pass
        print ("Passing over")
    print(character)
#the pass command allows us to add another line of code before the rest of the loop continues
