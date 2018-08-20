"""Combinatoric Selections
"""
num_rows = 101
grid = [[0] * num_rows for i in range(num_rows)]
for i in range(num_rows):
    grid[i][0] = 1

for i in range(1, num_rows):
    for z in range(1, i+1):
        grid[i][z] = grid[i-1][z-1] + grid[i-1][z]
c = 0
for a in grid:
    for b in a:
        if b > 1000000:
            c += 1
print(c)
 
