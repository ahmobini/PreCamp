def determinant(matrix, multiple):
    row = len(matrix)
    if row == 2:
        return multiple * (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0])
    else:
        answer, sign = 0, -1
        for i in range(row):
            sub_matrix = []
            for j in range(1, row):
                inner_list = []
                for k in range(row):
                    if k != i:
                        inner_list.append(matrix[j][k])
                sub_matrix.append(inner_list)
            sign *= -1
            answer += multiple*determinant(sub_matrix, sign*matrix[0][i])
    return answer


matrix = [
    [6, 1, 1],
    [4, -2, 5],
    [2, 8, 7]
]

print(determinant(matrix, 1))
