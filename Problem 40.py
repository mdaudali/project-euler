import math
from functools import reduce
from operator import mul
counter = 0
n = 0
d = []
for i in [1, 10, 100, 1000, 10000, 100000, 1000000]:
    while n < i:
        counter += 1    
        n += math.ceil(math.log10(counter))
    print(counter)
    digits = math.ceil(math.log10(counter))
    dif = i - (n - digits)
    print(str(counter)[dif - 1])
    d.append(str(counter)[dif - 1])

print (d)
print(reduce(mul, map(int, d)))  # Chooses 2 as the first digit, so corrected by halving