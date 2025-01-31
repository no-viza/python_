#Strings

string1 = "I need help"

print(string1)
print(string1[0:6])
print(string1[8])

print(string1[:6] + " pizza")
print(string1[7:] + " me")

#escape characters

string2 = "Who needs help"

print("hello \n python")
# "\n" means that everything after will be in a NEW LINE

#concatination
string3 = string1 + " " + string2

print(string1 + " " + string2)
print(string3)
# " " = space

#format character "%"
var1 = "hello"
var2 = "world"

print("%s this is the best %s" % (var1, var2))

#"%s" = string
#"%f" = float

print("-------------")

poem = """Nature's first green is gold,
Her hardest hue to hold.
Her early leaf's a flower;
But only so an hour."""

#the """ mean that anything after will continue to be part of that string until its closed
print(poem)

print("-------------")
var3 = "hi python"
print(var3.capitalize())
#capitalizes the first letter
#brackets in the end because this is a method

print(var3.upper())
#complete string in UPPERCASE

