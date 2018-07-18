import math
def prime_factorisation(i):
    ps = set()
    while i % 2 == 0:
        ps.add(2)
        i /= 2
    c = 3
    while i != 1:
        if i % c == 0:
            ps.add(c)
            i /= c
            continue
        c += 2
    return ps

nums_four = []
c = 2
num_test = 4
while True:
    if len(prime_factorisation(c)) == num_test:
        nums_four.append(c)
        ind = len(nums_four) - 1
        if ind > num_test and nums_four[ind] - nums_four[ind - num_test + 1] == num_test - 1:
            print(nums_four[ind - num_test + 1])
            break
    c += 1

