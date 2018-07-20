"""Pandigital Products
"""
from math import log10, ceil
from itertools import product
from functools import lru_cache

def is_pandigital(x):
    # num_digits = math.ceil(math.log10(x + 1))
    s = set(str(x))
    return len(s) == 9 and "0" not in s

def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:            
            memo[x] = f(x)
        return memo[x]
    return helper

@memoize
def get_number_digits(x):
    return int(ceil(log10(x + 1)))

numbers = [i for i in range(1, 10000) if len(str(i)) == len(set(str(i)))]
cache = {i: int(ceil(log10(i + 1))) for i in numbers}
prods = set()

for a, b in product(numbers, repeat=2):
    dig_a, dig_b = cache[a], cache[b]
    ab = a * b
    if dig_a + dig_b + get_number_digits(ab) == 9:
        if is_pandigital(str(a) + str(b) + str(ab)):
            prods.add(ab)
print(sum(prods))

