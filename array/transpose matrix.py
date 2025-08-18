def transpose(matrix):
    result = []
    for j in range(len(matrix[0])):      # loop over columns
        new_row = []
        for i in range(len(matrix)):     # loop over rows
            new_row.append(matrix[i][j]) # swap row <-> col
        result.append(new_row)
    return result

# Example
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(transpose(matrix))  # [[1,4,7],[2,5,8],[3,6,9]]
