import math
def is_pentagonal(i):
    x = (1 + math.sqrt(1 + 24 * i)) / 6
    return x.is_integer()

def is_hexagonal(i):
    x = (1 + math.sqrt(1 + 8 * i)) / 4
    return x.is_integer()

n = 286
while True:
    tri = n/2 * (n + 1)
    if is_pentagonal(tri) and is_hexagonal(tri):
        break
    n += 1
    

print(n)