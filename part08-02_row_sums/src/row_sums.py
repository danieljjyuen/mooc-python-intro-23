# Write your solution here

def row_sums(my_matrix:list):
    for index in range(len(my_matrix)):
        summ =0
        for val in my_matrix[index]:
            summ+=val
        my_matrix[index].append(summ)
