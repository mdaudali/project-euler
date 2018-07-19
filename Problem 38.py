"""Pandigital Multiples, this is gross in terms of the fact that it's string processing
"""
import math
def find_pandigital(n):
    """Finds a 9 digit pandigital if possible, otherwise returns 0. Will also return 0 if the first digit is not 9 - can optimise to ignore less than current multiple
    
    Args:
        n (int): the number to multiply
    """
    number_of_digits_left = 9
    val = ""
    m = n * 1
    val += str(m)
    if val[0] != "9":
        return "0"
    number_of_digits_left -= math.ceil(math.log10(m + 1))
    c = 1
    while number_of_digits_left > 0:
        c += 1
        m = n * c
        number_of_digits_left -= math.ceil(math.log10(m + 1))
        val += str(m)
    s = set(val)
    if number_of_digits_left != 0 or "0" in s or len(s) != 9:
        return "0"
    return val

cur_max = "918273645"
for x in range(1, 10000):
    p = find_pandigital(x)
    cur_max = max(p, cur_max)

print(cur_max)

