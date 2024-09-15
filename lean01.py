#12.59 transpose
matrix1 = [[1,2,3,4],
           [5,6,7,8]]

transpose_matrix = [[0,0],
                    [0,0],
                    [0,0],
                    [0,0]]

n_row = len(matrix1)
n_col = len(matrix1[0])

for r in range(n_row):
  for c in range(n_col):
    transpose_matrix[c][r] = matrix1[r][c]

print(transpose_matrix)
