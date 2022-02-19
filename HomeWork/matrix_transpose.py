def transpose(array):
    row, column = len(array[0]), len(array)

    transpose_matrix = [[0 for i in range(column)] for j in range(row)]
    for i in range(column):
        for j in range(row):
            transpose_matrix[j][i] = array[i][j]
    return transpose_matrix


print(transpose([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
))
