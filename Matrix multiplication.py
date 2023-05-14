# define matrices
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

# initialize resulting matrix
result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# iterate over rows of first matrix
for i in range(len(A)):
    # iterate over columns of second matrix
    for j in range(len(B[0])):
        # iterate over rows of second matrix
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]

# print resulting matrix
for row in result:
    print(row)
