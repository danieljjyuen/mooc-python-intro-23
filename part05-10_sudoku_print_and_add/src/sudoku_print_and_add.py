def print_sudoku(sudoku: list):
    for i in range(9):
        sentence = f""
        for j in range(9):
            if j == 3 or j == 6:
                sentence+= f" "
            if sudoku[i][j] == 0:
                sentence+= f"_"
            else:
                sentence+=f"{sudoku[i][j]}"
            if j != 8:
                sentence+=f" "
        print(sentence)
        if i == 2 or i == 5:
            print("")
        

def add_number(sudoku:list, row_no: int, column_no: int, number:int):
    sudoku[row_no][ column_no] = number


# s = [
#   [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
#   [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
#   [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
#   [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
#   [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
#   [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
#   [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
#   [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
#   [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
# ]
# add_number(s, 1, 1, 5)

# print_sudoku(s)