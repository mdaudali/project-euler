"""Coin sums
"""
d = [0] * 200
coins = [1, 2, 5, 10, 20, 50, 100, 200][::-1]
counter = 0
# ! How many ways can you make it with this coin and how many ways can you make it without this coin
def make_change(n, c):
    global counter
    if not c or n < 0:
        return
    if n == 0:
        counter += 1
        return
    top_coin = c[0]
    make_change(n - top_coin, c)
    make_change(n, c[1:])

make_change(200, coins)
print(counter)
