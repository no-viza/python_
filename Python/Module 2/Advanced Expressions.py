#ADVANCED EXPRESSIONS

import re

string1 = "Help me I am in trouble"

result = re.search(r'(.*) me (.*?) .*', string1, re.M|re.I)
#re.M = Multi.line matching
#re.I = Case Insensitive matching
# .* = the word before
# .*? = the word after
#the 3 parameters required for re.search = 1.pattern, 2.string, 3.flags

if(result):
    print(result.group())
    print(result.group(1))
    print(result.group(2))
else:
    print("no match")