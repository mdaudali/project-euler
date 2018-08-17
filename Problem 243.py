"""Resilience
"""
import math
from utils.utils import get_list_of_primes, get_prime_factors
from functools import reduce
from operator import mul
THRESHOLD = 15499 / 94744


def binary_gcd(u, v):
    if (u == 0): return v
    if (v == 0): return u
    
    c = 0
    while (u | v) & 1 == 0:
        u = u >> 1
        v = v >> 1
        c += 1
    
    while (u & 1) == 0:
        u = u >> 1;

    while True:
        while (v & 1) == 0:
            v = v >> 1

        if u > v:
            u, v = v, u
        
        v = v - u

        if v == 0:
            return u << c


def get_resilience(d):
    num_factors = d / 2 
    truth_list = [False] * int(math.ceil(((d - 3) / 2)))
    for x in range(3, d, 2):
        if truth_list[int(math.ceil(((x - 3) / 2)))]:
            num_factors += 1
            continue
        if binary_gcd(x, d) != 1:
            num_factors += 1
            for _ in range(x, d, x * 2):
                truth_list[int(math.ceil(((_ - 3) / 2)))] = True
    resilience = (d - num_factors) / (d - 1)
    return resilience


"""Finding composite that is over threshold by just multiplying primes
"""
def euler_product_formula_resilience(ps):
    n = reduce(mul, ps)
    v = [(p - 1) / p for p in set(ps)]
    return (n * reduce(mul, v))/(n-1)

# primes = get_list_of_primes(1000)
# for i in range(1, len(primes)):
#     r = euler_product_formula_resilience(primes[:i])
#     if r < THRESHOLD:
#         print (r, primes[:i])
#         break
 # ! this has told us it's between 2 x ... 23 and 2 x ... 29

start = 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19 * 23
for i in range(start, start * 29, start):  # ! Increment by start as you know it should contain all the primes up to 23
    r = euler_product_formula_resilience(get_prime_factors(i))
    if r < THRESHOLD:
        print (r, i)
        break

# !!! 0.113 seconds!!!
# primes = get_list_of_primes(1000)[1:]
# r = 10000
# c = 2
# while r > THRESHOLD:
#     c *= primes.pop(0)
#     r = get_resilience(c)
#     print(c, r)

# print(c)
# for d in range(24000, 1000000, 2):
#     num_factors = d / 2
#     truth_list = [False] * int(math.ceil(((d - 3) / 2)))
#     for x in range(3, d, 2):
#         if truth_list[int(math.ceil(((x - 3) / 2)))]:
#             num_factors += 1
#             continue
#         if binary_gcd(x, d) != 1:
#             num_factors += 1
#             for _ in range(x, d, x * 2):
#                 truth_list[int(math.ceil(((_ - 3) / 2)))] = True
#     resilience = (d - 1 - num_factors) / (d - 1)
#     if d % 1000 == 0:
#         print (d, resilience, flush=True)
#     if resilience < THRESHOLD:
#         print(d, resilience, truth_list)
#         break