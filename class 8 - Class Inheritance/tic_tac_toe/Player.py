class Player:
    def __init__(self,username,symbol):
        self.username=username
        self.symbol=symbol
        self.score=0

    def play(self,board):
        row=int(input("Insert a row position:"))
        column=int(input("Insert a column position:"))

        while(board.is_position_taken(row,column)):
            board.print_board()
            row = int(input("Insert a row position:"))
            column = int(input("Insert a column position:"))

        board.add_symbol(self.symbol,row,column)

    def win_game(self):
        self.score+=1

    def display_score(self):
        print("Score of {} is {}".format(self.username,self.score))