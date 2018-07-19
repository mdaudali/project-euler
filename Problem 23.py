"""Non-abundant sums
"""
import math, itertools
from utils.utils import get_proper_divisors
# * Get all divisors
print(get_proper_divisors(2))

# * get sum of all divisors for all numbers up to 21823

numbers = []
for a in range(1, 28123):  
    numbers.append(sum(get_proper_divisors(a)))

abundant_numbers = [ind for ind, i in enumerate(numbers, start=1) if i > ind]

sum_of_pairs = [i for i in range(1, 28123)]

for a, b in itertools.product(abundant_numbers, repeat=2):
    s = a + b
    if a + b < 28123:
        sum_of_pairs[s - 1] = False

print(sum(sum_of_pairs))