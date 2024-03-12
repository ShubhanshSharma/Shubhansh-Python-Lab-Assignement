
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

matrix2 = [[1,2,3],
          [4,5,6],
          [7,8,9]]

added = []

for x in range(len(matrix)):
    added.append([])
    for y in range(len(matrix[0])):
        added[x].append(matrix[y][x] + matrix2[y][x])

        
print(added[0])
print(added[1])
print(added[2])