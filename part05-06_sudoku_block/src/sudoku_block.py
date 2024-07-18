# Write your solution here
def block_correct(sudoku:list, row_no: int, column: int):
    count=0
    listx = []

    for i in range(row_no, row_no+3):
        for j in range(column, column+3):
            if sudoku[i][j] >0:
                count+=1
                listx.append(sudoku[i][j])
    return count == len(list(set(listx)))