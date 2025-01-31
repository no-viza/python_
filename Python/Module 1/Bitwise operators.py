#Bitwise operators

#performs operators on INDIVIDUAL BINARY BITS 

var1 = 13  # 1101 (in binary)
var2 = 5   # 0101 
# 13    1101
# 5     0101
#       ----
# AND   0101
# AND checks if BOTH the bits are ON at one time 
print (var1 & var2)

var3 = 15 # 1111
var4 = 4  # 0100 
# 15    1111
# 4     0100
#       ----
# OR    1111
# OR operator checks if at least 1 operator is ON or NOT
print (var3 | var4)

# 13    1101
# 5     0101
#       ----
# XOR   1000
# XOR checks if ONLY ONE bit is ON at one time 
print (var1 ^ var2)

# 13                0000 1101
#                   ---- ----
# Ones Complement   1111 0010
# This operator simply FLIPS the BITS
# Because its 13 (Greater than 8) so, 8-bit calculations will be used
# Therefore, the one's complement answer will be -14
# Calculations: (1 + 2 + 4 + 8 + 16 + 32 + 64) - 128
print (~var1)

# Binary Shift LEFT    0000 1101 will be 0001 1010 
# Will shift the whole bits to the number of SHIFTS
print (var1 << 1)
# Shift LEFT to 1 means that that LEFT-MOST 1 will be gone
# And that a 0 will come in the RIGHT-MOST place
# because EVERYTHING shifted 1 place to the LEFT

# Binary Shift RIGHT    0000 1101 will be 0000 0110
#the OPPOSITE of the above function 
print (var1 >> 1)