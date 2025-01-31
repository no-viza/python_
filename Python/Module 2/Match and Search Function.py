#Match Function

#RegEx: a function used to determine whether one variable matches another
#if one item is similar to the other
#the 'match' function starts matching from the START of the character

import re

pattern = re.compile('ell')

print(pattern.match("hello world"))
print(pattern.match("hello world", 1))
#"1" to tell the computer from which position to start matching from 
#hence, in the first code, it says none as it starts from the index position 0

#Search Function
#the "search" function searches from the first instance of that wordd

print("--------")

print(pattern.search("hello world"))
print(pattern.search("hello world", 1))
print(pattern.search("hello world", 2))
