def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    # Create a new matrix with swapped dimensions
    result = [[0] * rows for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]

    return result



matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(transpose(matrix))  # [[1,4,7],[2,5,8],[3,6,9]]
