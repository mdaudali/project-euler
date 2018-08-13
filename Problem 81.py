"""Path sum: two ways
"""
matrix_height = 80
matrix_width = 80

def traverse(matrix, v, h, cur_score=0, max_path=[[False] * matrix_width for x in range(matrix_height)]):
    max_path[matrix_height-1][matrix_width-1] = matrix[matrix_height-1][matrix_width-1]
    min_score = float("inf")
    if max_path[v][h]:
        return cur_score + max_path[v][h]
    if v + 1 < matrix_height:
        min_score = min(min_score, traverse(matrix, v + 1, h, cur_score + matrix[v][h]))
    if h + 1 < matrix_width:
        min_score = min(min_score, traverse(matrix, v, h + 1, cur_score + matrix[v][h]))
    max_path[v][h] = min_score
    return min_score
matrix = []
with open("./data/p091_matrix.txt", "r") as f:
    for line in f:
        matrix.append(list(map(int, line.split(","))))

for x in range(matrix_height-1, -1, -1):
    for y in range(matrix_height-1, -1, -1):
        traverse(matrix, x, y)
    
print(traverse(matrix, 0, 0))