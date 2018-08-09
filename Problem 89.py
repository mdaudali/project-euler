"""Roman numerals
"""


def convert_roman_to_int(rn):
    mapping = {
        "I": 1,
        "IV": 4,
        "V": 5,
        "IX": 9,
        "X": 10,
        "XL": 40,
        "L": 50,
        "XC": 90,
        "C": 100,
        "CD": 400,
        "D": 500,
        "CM": 900,
        "M": 1000
    }
    prev_digit = mapping[rn[0]]
    s = prev_digit
    for i in range(1, len(rn)):
        val = mapping[rn[i]]
        if val > prev_digit:
            s -= prev_digit
            s += mapping[rn[i-1:i+1]]
            prev_digit = mapping[rn[i-1:i+1]]
        else:
            s += val
            prev_digit = val
    return s

def convert_int_to_roman(i):
    mapping = {
        1: 'I',
        4: 'IV',
        5: 'V',
        9: 'IX',
        10: 'X',
        40: 'XL',
        50: 'L',
        90: 'XC',
        100: 'C',
        400: 'CD',
        500: 'D',
        900: 'CM',
        1000: 'M'
    }
    c = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    rn = ""
    while i > 0:
        if i >= c[0]:
            rn += mapping[c[0]]
            i -= c[0]
        else:
            c.pop(0)
    return rn

counter = 0
with open("data/p089_roman.txt", "r") as f:
    for line in f:
        line = line.strip()
        original_length = len(line)
        new_length = len(convert_int_to_roman(convert_roman_to_int(line)))
        counter += original_length - new_length
print(counter)

