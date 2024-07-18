# Write your solution here
def play_turn(game_board:list, x:int, y:int, piece: str):
    if x > 2 or y > 2 or x <0 or y <0:
        return False
    if game_board[y][x] =="":
        game_board[y][x] = piece
        return True
    else:
        return False
    
# board = [['s','',''],['','',''],['','','']]
# print(play_turn(board, 0, 0, "X"))