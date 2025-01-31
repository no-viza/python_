#Search and replace 
#also called 'sub'

import re

string1 = "24508234. 4871283 sdkfajsdf {aldjas] 78?"

result = re.sub(r'\D', "", string1)
#\D = digits
print(result)

result = re.sub(r'\D', " ", string1)
# the "" is used to add the replacement
# leaving them blank means replacinng it with nothing
print(result)

result = re.sub(r'\D', ".", string1)
#Every character not needed is replaced with a .
print(result)
