result = 1

# BRO IT SAYS THE SMALLER ONE
# learn how to read lmao
"""
for number in range(1, 11):
    print(f'{result} x {number} = {result*number}')
    result = result * number

print(result)
"""

"""
actually this is far easier with just a little bit of paper:
232792560, see smallest_multiple.png

work on a proper function when you got time
"""

import math

# the smallest number divisible by every number from 1 to 20 is their least common multiple
print(math.lcm(*range(1, 21)))
