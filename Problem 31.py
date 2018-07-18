"""This will use a bottom up dynamic programming approach
d[i] = max(d[i - v] for v in coins) + 1
"""
d = [0] * 200
coins = [1, 2, 5, 10, 20, 50, 100, 200]

def make_change(i):
    lists = []
    c = 0
    for v in coins:
        if i - v < 0:
            break
        elif i - v == 0:
            c += 1
        else:
            c += d[i-v-1]
    return c

for x in range(1, 201):
    d[x - 1] = make_change(x)

print(d)

