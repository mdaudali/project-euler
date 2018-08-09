"""Digit Factorial Chains
"""

# ! math.factorial is very fast
# ! Memoize the chains?
# What's the largest answer - 9! + 9! + 9! + 9! + 9! + 9! = 2177280

import math

def find_chain(i, n=0, mem=[[False, -1] for _ in range(2177281)]):
    if mem[i][1] > -1:  # ! we've seen this cycle before
        return n + mem[i][1]
    elif mem[i][0]:  # ! We've seen this number before but not this cycle before
        return n
    else:
        mem[i][0] = True
        n2 = find_chain(sum(math.factorial(int(x)) for x in str(i)), n + 1)
        mem[i] = [False, n2 - n]
        return n2

c = 0
for i in range(0, 1000000):
    if find_chain(i) == 60:
        c += 1
print(c)