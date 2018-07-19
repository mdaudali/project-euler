"""Pandigital Primes
"""

import math, itertools
from utils.utils import get_list_of_primes, is_prime

def is_pandigital(x):
    num_digits = math.ceil(math.log10(x + 1))
    s = set(str(x))
    return len(s) == num_digits and "0" in s

# * Heuristic: in base 10, the max thing can be 9 digits long, so you can terminate then
# * Heuristic: In fact, it can't be 9 or 8 digits as sum of 1-9 is 45, which is divisible by 3 and to test if something's divisible by 3 you sum the digits
# * Same for 8 - 36
# * Heuristic: There's significantly fewer n-digit pandigital numbers than numbers in general, so generate them rather than getting all primes 
primes = get_list_of_primes(1000)
cur_max = 0
for n in range(7, 0, -1):
    for number in itertools.permutations(range(1, n+1), n):
        number = int(str(''.join(map(str, number))))
        if n == 4:
            print(number)
        if is_prime(number, primes):
            cur_max = max(cur_max, number)
    if cur_max > 0:
        break
print(cur_max)