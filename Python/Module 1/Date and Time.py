#Date and Time

import time
import calendar

#epoch time
#tells the number of ticks
var1 = time.time()
print(var1)

#local time
local = time.localtime(time.time())
print(local)

#formatted local time
timeLocal = time.asctime(time.localtime(time.time()))
print(timeLocal)

print("---------")

#calenders
var2 = calendar.month(2024, 5)
print(var2)