# Write your solution here
def sudoku_grid_correct(sudoku: list):
    listx = []
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] >0:
                listx.append(f"row {i} is {sudoku[i][j]}")
                listx.append(f"column {j} is {sudoku[i][j]}")
                listx.append(f"box r {i//3} c {j//3} is {sudoku[i][j]}")
    listxx = list(set(listx))
    # print(len(listx))
    # print(len(listxx))
    return len(listx) == len(listxx)
