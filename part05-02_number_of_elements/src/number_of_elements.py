# Write your solution here 
def count_matching_elements(my_matrix: list, element: int):
    count =0

    for i in my_matrix:
        # print("i", i)
        for j in i:
            # print(j)
            if j == element:
                count+=1
    return count

#count_matching_elements([[1,2,1], [0,3,4], [1, 0,0]], 1)