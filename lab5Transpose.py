
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

# transpose is :
transpose = []

for x in range(len(matrix[0])):
    transpose.append([])
    for y in range(len(matrix)):
        transpose[x].append(matrix[y][x])

# transpose = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

print(transpose[0])
print(transpose[1])
print(transpose[2])