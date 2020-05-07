# Math Program
# 7/5/2020

from math import *

print( 2 * 3 )       # Basic Arithmetic: +, -, /, *
print( 2**3 )        # Basic Arithmetic: +, -, /, *
print( 10 % 3 )      # Modulus Op. : returns remainder of 10/3
print( 1 + 2 * 3 )   # order of operations
print(10 / 3.0)      # int's and doubles


num = 10
num += 100 # +=, -=, /=, *=
print(num)

++num
print(num)

# Math module has useful math methods
import math
print( pow(2, 3) )
print( math.sqrt(144) )
print( round(2.7) )

five = 5
print(str(five) + " is my faviorite number")

five = -5
print(abs(five)) # This will output the absolute value of -5

print(max(10, 54, 45)) # This will output the largest number of the 3 numbers

print(min(10, 54, 45)) # This will do the opposite of the above

print(floor(51.36)) # This will remove the decimal point

print(ceil(2.6))
