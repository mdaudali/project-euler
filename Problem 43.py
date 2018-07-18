
from itertools import permutations
perms = permutations(map(str, range(0, 10)))
c = 0
primes = [2, 3, 5, 7, 11, 13, 17]
for p in perms:
    if p[0] == 0:
        continue
    for i in range(len(primes)):
        s = int(''.join(p[i+1:i+4]))
        if s % primes[i] != 0:
            break
    else:
        c += int(''.join(p))

print(c)

    