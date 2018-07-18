from utils.utils import prime_sieve, get_list_of_primes_pre_calc
from itertools import product

primes = prime_sieve(1001)
b_list = [1] + get_list_of_primes_pre_calc(primes)
a_list = b_list

a_cross_b = product(a_list, b_list)
all_primes = prime_sieve(10000000)


def get_num_primes(a, b):
    n = 0
    while True:
        if all_primes[n ** 2 + a * n + b]:
            n += 1
        else:
            break
    return n, a * b

# Slightly flawed logic, but it worked - b did have to be prime for n = 0 to work,
# but a didn't necessarily have to be prime, it just had to be odd


max_n = 0
max_prod = 0
for a, b in a_cross_b:

    # With both positive
    n, prod = max((get_num_primes(a, b), get_num_primes(a, -b), get_num_primes(-a, b), get_num_primes(-a, -b)), key=lambda x: x[0])
    if n > max_n:
        max_n = n
        max_prod = prod

print(max_prod, max_n)



