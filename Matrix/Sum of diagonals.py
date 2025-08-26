matrix = [[1,2,3],[4,5,6],[7,8,9]]
primary=sum(matrix[i][i] for i in range(len(matrix)))
secondary=sum(matrix[i][len(matrix)-1-i] for i in range(len(matrix)))
print(primary, secondary)