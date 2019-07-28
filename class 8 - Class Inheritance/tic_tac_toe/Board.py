class Board():
    def __init__(self,size=3,):
        self.size=size
        self.board=[]

        for r in range(self.size):
            self.board.append([])
            for c in range(self.size):
                self.board[r].append(" ")

    def print_board(self):
        print("----"*len(self.board[0]))

        for line in self.board:
            for column in line:
                print("| {} ".format(column), end="")
            print("|")
            print("----"*len(self.board[0]))

    def clear_board(self):
        for r in range(self.row):
            for c in range(self.column):
                self.board[r][c]=" "

    def add_symbol(self,symbol,row,column):
        if self.is_in_boundaries(row,column):
            self.board[row-1][column-1]=symbol
            return True
        else:
            return False

    def is_full(self):
        for r in range(len(self.board)):
            for c in range(len(self.board[0])):
                if self.board[r][c]==' ':
                    return False
        return True

    def is_position_taken(self,row,column):
        if self.is_in_boundaries(row,column):
            if self.board[row-1][column-1]!=" ":
                print("This position is taken")
                return True
        else:
            print("This position is not existing")
            return False

    def is_in_boundaries(self,row,column):
        return 0<row and row<=len(self.board) and 0<column and column<=len(self.board[0])


    def is_there_a_winner(self):

        #Step 1 find if there a winner in the row
        for r in range(self.size):
            potential_winner_symbol=self.board[r][0]
            if potential_winner_symbol==" ":
                continue
            is_winner=True

            for c in range(self.size):
                # Check winner in a row
                if self.board[r][c]!=potential_winner_symbol:
                    is_winner=False
                    break

            if is_winner:
                print("winner step 1")
                return (True,potential_winner_symbol)

        #Step 2: Check if there is a winner in the column
        for c in range(self.size):
            potential_winner_symbol = self.board[0][c]

            if potential_winner_symbol==" ":
                continue

            is_winner = True

            for r in range(self.size):
                # Check winner in a row
                if self.board[r][c] != potential_winner_symbol:
                    is_winner = False
                    break

            if is_winner:
                print("winner step 2")
                return (True,potential_winner_symbol)

        #Step 3: Check if there is a winner in the diagonale from left
        potential_winner_symbol = self.board[0][0]
        if potential_winner_symbol != " ":
            is_winner = True
            for e in range(self.size):
                if self.board[e][e] != potential_winner_symbol:
                        is_winner = False
                        break
            if is_winner:
                print("winner step 3")
                return (True,potential_winner_symbol)

        #Step 4: Check if there is a winner in the diagonale from right
        potential_winner_symbol = self.board[0][len(self.board)-1]
        if potential_winner_symbol != " ":
            is_winner = True
            for e in range(self.size):
                if self.board[e][len(self.board)-1-e] != potential_winner_symbol:
                        is_winner = False
                        break
            if is_winner:
                print("winner step 4")
                return (True,potential_winner_symbol)

        #we test all cases
        print("No winner step 5")
        return (False,' ')
