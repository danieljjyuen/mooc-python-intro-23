# Write your solution here
def copy_and_add(sudoku:list, row_no: int, column_no: int, number: int):
    newlist = []
    for i in range(9):
        newlist.append([])
        for j in range(9):
            newlist[i].append(0)
    
    for i in range(9):
        for j in range(9):
            newlist[i][j] = sudoku[i][j]
    
    newlist[row_no][column_no] = number
    return newlist