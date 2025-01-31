#Dictionary

dictionary = {}
dictionary[1] = "item 1"
dictionary["popup"] = "item 2"
dictionary[2] = "item 3"

#in a dictionary, each key is unique meaning there can be NO DUPLICATES

#accessing dictionary
print(dictionary["popup"])
print(dictionary[2])
print(dictionary)
print(dictionary.values())
print(dictionary.keys())
#"Values" being the actual value that was assigned
#"Keys" being the string or number used to assign the value

print("------------")

NewbieDictionary = {"A":"item a", "B":"item b", "C":"item c"}
print(NewbieDictionary)
#A shortcut to create a dictionary

print("------------")

#DICTIONARY IN DEPTH
dictionary1 = {'1': 'item a', '2': 'item b', '3': 'item c', '4': 9}

#updating dictionary
dictionary1['4'] = 10
print(dictionary1['4'])

dictionary1['4'] = 3
print(dictionary1['4'])

print("------------")

#deleting values in dictionary
del dictionary1['2']
print(dictionary1)

#deleting the entire dictionary
# del dictionary1

# to still keep the dictionary but clean all its elements 
# dictionary1.clear() 

#length of the dictionary
print(len(dictionary1))





