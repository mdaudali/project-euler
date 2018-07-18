cap = 1000000
def sieve():
    prime_list= [True] * cap
    for i in range(2, cap):
        for j in range(i * 2, cap, i):
            prime_list[j] = False
    return prime_list

primes_bool = sieve() # Starts from 0, index in as normal without - 1
primes = [i for i, p in enumerate(primes_bool) if p][2:]
counter = 1000
flag = False
while not flag:
    for i in range(len(primes) - counter + 1):
        s = sum(primes[i:counter + i])
        if s < cap and primes_bool[s]:
            print(s, primes[i:counter + i])
            flag = True
            break
    counter -= 1
