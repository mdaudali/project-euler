from utils.utils import prime_sieve, get_list_of_primes_pre_calc

search = prime_sieve(1000000)
primes = get_list_of_primes_pre_calc(search)

def rotate(n):
    as_str = str(n)
    num_digits = len(as_str)
    for i in range(1, num_digits + 1):
        yield int(as_str[i:] + as_str[:i])

cyclic = set()
for p in primes:
    for r in rotate(p):
        if not search[r]:
            break
    else:
        cyclic.add(p)

print(len(cyclic))