#Lists

BasicList = ['help', 98, 'me', 'ASAP']

#Accessing the list
print(BasicList)
print(BasicList[0])
print(BasicList[2])
print(BasicList[2:3])
print(BasicList + BasicList)
#the plus sign merges 2 lists while the * sign will multiply
print(BasicList * 3)

BasicList[2] = 5

print(BasicList[2])

print("------------")

BasicTuple = ('help', 98, 'me', 'ASAP')

#Accessing tuples
print(BasicTuple)
print(BasicTuple[0])
print(BasicTuple[2])
print(BasicTuple[2:3])

#BasicTuple[2] = 5 
#will show an error as tuples can NOT be assigned values
#so for data the needs to be READ ONLY, tuples are used

print("------------")

#LISTS IN ADVANCE

listnumber1 = [1, 2, 3, "hakuna", 9, "matata"]
listnumber2 = [12, 14, 37, 24, 19, 93]

#updating a list
print(listnumber1[0])
listnumber1[0] = "no.1 was replaced"
print(listnumber1[0])
listnumber1[0] = 1

#Deleting something in a list 
print(listnumber1[3])
del listnumber1[3]
print(listnumber1)

#to know the length of the list
print(len (listnumber1))

#to know max/min value
print(max(listnumber2))
print(min(listnumber2))

#to convert list to tuple
listTuple = tuple(listnumber2)
print(listnumber2)

print("------------")

#TUPLES IN DEPTH

tuple1 = (2, 4, "x", "y", "z")

#updating/deleting any value in a tuple is not possible as tuples do not allow changes to be made
#however, you can delete the complete tuple 

#calculating the length of the tuple
print(len(tuple1))



 