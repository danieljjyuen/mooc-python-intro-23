# Write your solution here
def column_correct(sudoku: list, column_no:int):
    listx = []
    count =0
    for i in sudoku:
        if i[column_no] > 0:
            count+=1
            listx.append(i[column_no])
    return count == len(list(set(listx)))
