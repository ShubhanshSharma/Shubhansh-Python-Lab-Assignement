
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

matrix2 = [[1,2,3],
          [4,5,6],
          [7,8,9]]

added = []

if (len(matrix[0]) == len(matrix2)):
    for x in range(len(matrix)):
        added.append([])
        for y in range(len(matrix[0])):
            added[x].append(matrix[x][0] * matrix2[0][y] + matrix[x][1] * matrix2[1][y] + matrix[x][2] * matrix2[2][y])

        
print(added[0])
print(added[1])
print(added[2])