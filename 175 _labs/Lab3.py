

class TicTacToe:
    def __init__(self):
        # "board" is a list of 10 strings representing the board (ignore index 0)
        self.board = [" "]*10
        self.board[0]="#"
        
#------------------------------------------------------------- 
    def drawBoard(self):
        # This method prints out the board with current plays adjacent to a board with index.
       
        print(self.board[7],"|",self.board[8],"|",self.board[9]+'   ','7','|','8','|','9')
        print('----------  -----------')
        print(self.board[4],"|",self.board[5],"|",self.board[6]+'   ',4,"|",5,'|',6)
        print('----------  -----------')
        print(self.board[1],"|",self.board[2],"|",self.board[3]+'   ',1,'|',2,'|',3)

        #write some code here

#------------------------------------------------------------- 
    def boardFull(self):
        # This method checks if the board is already full and returns True. Returns false otherwise
        if (' ' in self.board):
            return False
        else:
            return True

#------------------------------------------------------------- 
    def cellIsEmpty(self, cell):
        if (self.board[cell] == ' '):
            return True
        else:
            return False
        
       
        #write some code here

#------------------------------------------------------------- 
    def assignMove(self, cell,ch):
        # assigns the cell of the board to the character ch
        self.board[cell] = ch

        #write some code here

#------------------------------------------------------------- 
    def whoWon(self):
    # returns the symbol of the player who won if there is a winner, otherwise it returns an empty string. 
        if self.isWinner("x"):
            return "x"
        elif self.isWinner("o"):
            return "o"
        else:
            return ""

#-------------------------------------------------------------   
    def isWinner(self, ch):
        # Given a player's letter, this method returns True if that player has won.
        b= self.board
        #win by rows
        if (b[7]==ch and b[8]==ch and b[9]==ch):
            return True
        elif (b[4]==ch and b[5]==ch and b[6]==ch):
            return True
        elif (b[1]==ch and b[2]==ch and b[3]==ch):
            return True        
        #win bycolumn
        elif (b[1]==ch and b[4]==ch and b[7]==ch):
            return True
        elif (b[2]==ch and b[5]==ch and b[8]==ch):
            return True
        elif (b[3]==ch and b[6]==ch and b[9]==ch):
            return True    
        #win by diagonal
        elif (b[1]==ch and b[5]==ch and b[9]==ch):
            return True
        elif (b[3]==ch and b[5]==ch and b[7]==ch):
            return True  
        #no win 
        return False



#----------------main-function------------------------------
myBoard =TicTacToe()
player ="o"
while True:
    myBoard.drawBoard()
    
    try:
        move_cell = int(input("It is the turn for "+ player+ ". What is your move?"))
    except:
        print("error! not a cell. ")
        continue
    if (move_cell>9 or move_cell<1):
        print("error!not a vaild cell")
        continue 
    #checking empty 
    if (myBoard.cellIsEmpty(move_cell)):
        myBoard.assignMove(move_cell,player)
    else:
    
        print("error! the cell you choose is not full")
        continue
    # checking winner    
    if (myBoard.boardFull()):
        break
    else:
        if (myBoard.whoWon()!=''):
            break
        
    if (player=="o"):
        player = "x"
    else:
        player = "o"
    
    
        
myBoard.drawBoard()

winner = myBoard.whoWon()
if (winner == ''):
    print(" it is a tie, no one wins ")
else:
    print(winner, "wins. congrats!")


