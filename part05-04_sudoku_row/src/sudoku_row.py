# Write your solution here
def row_correct(sudoku: list, row_no: int):
    count =0
    listx = []
    for i in sudoku[row_no]:
        if i != 0:
            count+=1
            listx.append(i)
    if count == len(list(set(listx))):
        return True
    else:
        return False