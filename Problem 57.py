"""Square root convergents
"""
from utils.utils import get_number_digits
from fractions import Fraction
from decimal import Decimal
import sys

def method_one():
    sys.setrecursionlimit(2005)
    def fraction_generator(i):
        return Fraction(2, 1) + (Fraction(1, fraction_generator(i - 1)) if i > 0 else 0)

    c = 0
    for x in range(1000):
        num = Fraction(1, 1) + Fraction(1, fraction_generator(x))
        f = Fraction(num)
        n = f.numerator
        d = f.denominator
        if get_number_digits(n) > get_number_digits(d): c+= 1

    print(c)

def method_two():
    # ! There's a recurrence, this speeds up the program from 9 seconds to < 0.1
    num, den = 3, 2
    c = 0
    for i in range(1, 1000):
        num, den = 2 * den + num, num + den
        if get_number_digits(num) > get_number_digits(den): c += 1

    print(c)

method_two()

