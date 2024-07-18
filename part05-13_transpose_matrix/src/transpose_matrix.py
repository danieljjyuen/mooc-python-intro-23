# Write your solution here
def transpose(matrix: list):
    for i in range(len(matrix)):
        for j in range(i+1,len(matrix)):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        

# m = [[10, 100], [10, 100]]
# transpose(m)
