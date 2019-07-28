import random
from Board import Board
from Player import Player

#Main code
#Step 1: Create the board
# Ask siwe of the board
name_player1=input("Insert name player 1:")
name_player2=input("Insert name player 2:")
board_size=input("Insert size of board:")

b=Board(int(board_size))

#Step 2 create players
p1=Player(name_player1,'X')
p2=Player(name_player2,'O')



while True:
    active_player=p1
    print("{} is your turn".format(active_player.username))

    while(True):
        if b.is_full():
            print("Game Over - No Winner")
            #end of game
            break;
        else:
            b.print_board()
            active_player.play(b)
            is_winner,s=b.is_there_a_winner()
            if(is_winner):
                if p1.symbol==s:
                    winner=p1
                else:
                    winner=p2

                winner.win_game()
                p1.display_score()
                p2.display_score()
                print("End of the Game")
                break;
            else:
                if active_player==p1:
                    active_player=p2
                else:
                    active_player=p1
                print("{} is your turn".format(active_player.username))
    answer=input("Do you want to play again:")
    if(answer!='y')
        break
    b.clear_board()
