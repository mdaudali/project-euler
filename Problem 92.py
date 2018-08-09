"""Square digit chains
"""
import sys
sys.setrecursionlimit(2005)

# ! Basing code of 74
def get_chain(i, mem=[None for _ in range(10000000)]):
    mem[1] = False
    mem[89] = True
    if mem[i] != None: # ! we've seen this cycle before
        return mem[i]
    # ! We know that everything either ends up at 1 or 89, so we don't need a check to see if we've never seen this cycle before
    ans = get_chain(sum(int(x) ** 2 for x in str(i)))
    mem[i] = ans
    return ans

c = 0
for x in range(1, 10000000):
    if get_chain(x):
        c += 1

print(c)


