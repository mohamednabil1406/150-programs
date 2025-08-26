def transpose(matrix):
    return [list(row) for row in zip(*matrix)]
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

print(transpose(matrix))


"or without  "
def transpose_mat(matrix):
    rows=len(matrix)
    cols=len(matrix[0])
    result=[]
    for c in range(cols):
        transposed_row=[]
        for r in range(rows):
            transposed_row.append(matrix[r][c])
        result.append(transposed_row)
    return result


# Example usage:
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

print(transpose(matrix))