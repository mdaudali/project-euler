"""Covergents of e
"""
import sys
from fractions import Fraction
convs = []
for i in range(1, 34):
    convs.extend((1, 2 * i, 1))
convs = convs[::-1]

sys.setrecursionlimit(2005)
def fraction_generator(c):
    return Fraction(c.pop(), 1) + (Fraction(1, fraction_generator(c)) if c else 0)

ans = 2 + Fraction(1, fraction_generator(convs))
print(ans)
print(sum(int(x) for x in str(ans.numerator)))