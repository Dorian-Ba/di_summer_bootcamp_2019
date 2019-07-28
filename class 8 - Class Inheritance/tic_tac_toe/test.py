import random
from Board import Board


board_5=Board(5)
board_5.print_board()

for line in range(1,len(board_5.board)+1):
    for col in range(1,len(board_5.board)+1):
        if(col==2):
            board_5.add_symbol('X', line, col)
        else:
            gen_sym=random.choice(['X','O',' '])
            board_5.add_symbol(gen_sym,line,col)

board_5.print_board()
board_5.is_there_a_winner()
