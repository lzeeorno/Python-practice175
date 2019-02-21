#assignment 2 
#Zheng Fuchen(leon): 1465251

import random as rnd
import os
import sys

class Grid():
    def __init__(self, row=4, col=4, initial=2):
        self.row = row                              # number of rows in grid
        self.col = col                              # number of columns in grid
        self.initial = initial                      # number of initial cells filled
        self.score = 0

        self._grid = self.createGrid(row, col)    # creates the grid specified above

        self.emptiesSet = list(range(row * col))    # list of empty cells

        for _ in range(self.initial):               # assignation to two random cells
            self.assignRandCell(init=True)


    def createGrid(self, row, col):

        """
        Create the grid here using the arguments row and col
        as the number of rows and columns of the grid to be made.

        The function should return the grid to be used in __init__()
        """
        # version 1
        # grid_list = []
        # for i in range(row):
        #     row_list = []
        #     for j in range(col):
        #         row_list.append(0)
        #     grid_list.append(row_list)

        # version 2
        #grid_list = [[0 for j in range(col)] for i in range(row)]

        # version 3
        col_original = col
        grid_list = []
        while row>0:
            row_list = []
            col = col_original
            while col>0:
                row_list.append(0)
                col = col - 1
            grid_list.append(row_list)
            row = row - 1
        return grid_list



    def setCell(self, cell, val):

        """
        This function should take two arguments cell and val and assign
        the cell of the grid numbered 'cell' the value in val.

        This function does not need to return anything.

        You should use this function to change values of the grid.
        """
        row = cell // self.col
        col = cell % self.col
        self._grid[row][col] = val


    def getCell(self, cell):

        """"
        This function should return the value in cell number 'cell'
        of the grid.

        You should use this function to access values of the grid
        """
        """
        0  1  2  3
        4  5  6  7
        8  9  10 11
        12 13 14 15
        """
        row = cell // self.col
        col = cell % self.col
        return self._grid[row][col]


    def assignRandCell(self, init=False):

        """
        This function assigns a random empty cell of the grid
        a value of 2 or 4.

        In __init__() it only assigns cells the value of 2.

        The distribution is set so that 75% of the time the random cell is
        assigned a value of 2 and 25% of the time a random cell is assigned
        a value of 4
        """

        if len(self.emptiesSet):
            cell = rnd.sample(self.emptiesSet, 1)[0]
            if init:
                self.setCell(cell, 2)
            else:
                cdf = rnd.random()
                if cdf > 0.75:
                    self.setCell(cell, 4)
                else:
                    self.setCell(cell, 2)
            self.emptiesSet.remove(cell)


    def drawGrid(self):

        """
        This function draws the grid representing the state of the game
        grid
        """

        for i in range(self.row):
            line = '\t|'
            for j in range(self.col):
                if not self.getCell((i * self.row) + j):
                    line += ' '.center(5) + '|'
                else:
                    line += str(self.getCell((i * self.row) + j)).center(5) + '|'
            print(line)
        print()


    def updateEmptiesSet(self):

        """
        This function should update the list of empty cells of the grid.
        """

        self.EmptiesSet = []
        for i in range(self.row):
            for j in range(self.col):
                if not self.getCell(i*self.row+j):
                    self.EmptiesSet.append(i*self.row+j)


    def collapsible(self):

        """
        This function should test if the grid of the game is collapsible
        in any direction (left, right, up or down.)

        It should return True if the grid is collapsible.
        It should return False otherwise.
        """
        # 0 in grid
        for i in range(self.row*self.col):
            if self.getCell(i) == 0:
                return True
        
        # see horizontal neighbor
        for row in range(self.row):
            cell_value = self.getCell(row*self.col + 0)
            for col in range(1, self.col):
                cell_value_2 = self.getCell(row*self.col + col)
                if cell_value == cell_value_2:
                    return True
                cell_value = cell_value_2
        
        # see vertical neighbor
        for col in range(self.col):
            cell_value = self.getCell(col)
            for row in range(1, self.row):
                cell_value_2 = self.getCell(row*self.col + col)
                if cell_value == cell_value_2:
                    return True
                cell_value = cell_value_2
        
        return False

        


    def collapseRow(self, lst):

        """
        This function takes a list lst and collapses it to the LEFT.

        This function should return two values:
        1. the collapsed list and
        2. True if the list is collapsed and False otherwise.
        """
        out = []
        collapsed = False
        collapsed_in_row = False
        for i in range(len(lst)):

            if len(out)>=1 and lst[i] == out[-1] and not collapsed:
                collapsed = True
                collapsed_in_row = True
                out[-1] += lst[i]
                self.score += out[-1]
            else:
                if lst[i] != 0:
                    out.append(lst[i])
                    collapsed = False

        temp = len(out)
        for i in range(len(lst) - temp):
            out.append(0)

        return out, collapsed_in_row




    def collapseLeft(self):

        """
        This function should use collapseRow() to collapse all the rows
        in the grid to the LEFT.

        This function should return True if any row of the grid is collapsed
        and False otherwise.
        """
        row_is_collapsed = False
        for row in range(self.row):
            # get row
            row_list = []
            for col in range(self.col):
                cell = self.getCell(row * self.col + col)
                row_list.append(cell)
            ############

            # collapse this row
            row_collapsed, is_collapsed = self.collapseRow(row_list)
            if is_collapsed:
                row_is_collapsed = True

            ############
            # save result to grid
            for col in range(self.col):
                self.setCell(row * self.col + col, row_collapsed[col])

        return row_is_collapsed



    def collapseRight(self):

        """
        This function should use collapseRow() to collapse all the rows
        in the grid to the RIGHT.

        This function should return True if any row of the grid is collapsed
        and False otherwise.
        """
        row_is_collapsed = False
        for row in range(self.row):
            # get row
            row_list = []
            for col in range(self.col):
                cell = self.getCell(row * self.col + col)
                row_list.append(cell)
            row_list.reverse() 

            # collapse this row
            row_collapsed, is_collapsed = self.collapseRow(row_list)
            if is_collapsed:
                row_is_collapsed = True
            row_collapsed.reverse()

            ############
            # save result to grid
            for col in range(self.col):
                self.setCell(row * self.col + col, row_collapsed[col])

        return row_is_collapsed
        



    def collapseUp(self):

        """
        This function should use collapseRow() to collapse all the columns
        in the grid to UPWARD.

        This function should return True if any column of the grid is
        collapsed and False otherwise.
        """
        col_is_collapsed = False
        for col in range(self.col):
            # get col
            col_list = []
            for row in range(self.row):
                cell = self.getCell(row * self.col + col)
                col_list.append(cell)
            # collapse this col
            row_collapsed, is_collapsed = self.collapseRow(col_list)
            if is_collapsed:
                col_is_collapsed = True
            # save result to grid
            for row in range(self.row):
                self.setCell(row * self.col + col, row_collapsed[row])

        return col_is_collapsed
                
            
        
        



    def collapseDown(self):

        """
        This function should use collapseRow() to collapse all the columns
        in the grid to DOWNWARD.

        This function should return True if any column of the grid is
        collapsed and False otherwise.
        """
        col_is_collapsed = False
        for col in range(self.col):
            col_list = []
            for row in reversed(range(self.row)):
                col_list.append(self.getCell(row*self.col+col))
            
            # collapse this col
            row_collapsed, is_collapsed = self.collapseRow(col_list)
            if is_collapsed:
                col_is_collapsed = True
                # save result to grid
            for row in reversed(range(self.row)):
                self.setCell(row * self.col + col, row_collapsed[self.row-row-1])
    
        return col_is_collapsed
        
                
            
                
                
        



class Game():
    def __init__(self, row=4, col=4, initial=2):

        """
        Creates a game grid and begins the game
        """

        self.game = Grid(row, col, initial)
        self.play()


    def printPrompt(self):

        """
        Prints the instructions and the game grid with a move prompt
        """

        if sys.platform == 'win32':
            os.system("cls")
        else:
            os.system("clear")

        print('Press "w", "a", "s", or "d" to move Up, Left, Down or Right respectively.')
        print('Enter "p" to quit.\n')
        self.game.drawGrid()
        print('\nScore: ' + str(self.game.score))


    def play(self):

        moves = {'w' : 'Up',
                 'a' : 'Left',
                 's' : 'Down',
                 'd' : 'Right'}

        stop = False
        collapsible = True

        while not stop and collapsible:
            self.printPrompt()
            key = input('\nEnter a move: ')

            while not key in list(moves.keys()) + ['p']:
                self.printPrompt()
                key = input('\nEnter a move: ')

            if key == 'p':
                stop = True
            else:
                move = getattr(self.game, 'collapse' + moves[key])
                collapsed = move()

                if collapsed:
                    self.game.updateEmptiesSet()
                    self.game.assignRandCell()

                collapsible = self.game.collapsible()

        if not collapsible:
            if sys.platform == 'win32':
                os.system("cls")
            else:
                os.system("clear")
            print()
            self.game.drawGrid()
            print('\nScore: ' + str(self.game.score))
            print('No more legal moves.')


def main():
    game = Game()

main()