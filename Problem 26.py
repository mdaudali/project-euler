"""Reciprocal cycles
"""

def check_prime_factors(n):
    while n % 2 == 0:
        n /= 2
    while n % 5 == 0:
        n /= 5
    return n != 1

def recurring_length(n):
    # Using bus method you can see how you find the decimal expansion
    seen = []
    r = 10
    c = 0
    while r not in seen:
        seen.append(r)
        r = 10 * (r % n)
        c += 1
    return c

m = 0
c = 0
for i in range(2, 1000):
    if check_prime_factors(i):
        d = recurring_length(i)
        if m < d:
            m = d
            c = i
print(c)