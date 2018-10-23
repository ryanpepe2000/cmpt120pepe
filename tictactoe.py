# CMPT 120 Intro to Programming
# Lab #6 – Lists and Error Handling
# Author: Ryan Pepe
# Created: 10/23/2018

symbol = [ " ", "x", "o" ]

def printRow(row):
    for i in range(3):# for each square in the row...
        print("|" + symbol[row[i]] + "  ", end="")# add to output the symbol for this square followed by a border
    print("|")# print the completed output for this row
    pass

def printBoard(board):
    
    for i in range(3): # for each row in the board...
        print("+-----------+")# print the row
        printRow(board[i])
    print("+-----------+")# print the next border
    pass

def markBoard(board, row, col, player):
    # check to see whether the desired square is blank
    # if so, set it to the player number
    pass

def getPlayerMove():
    x,y = input("Enter the row and column (x,y): ") # prompt the user separately for the row and column numbers
    return x,y # then return that row and column instead of (0,0)

def hasBlanks(board):
    for row in range(3):
        for square in range(3):
            if board[row][square] == 0:
                return True 
            else:
                return False

def main():
    board = [[0,0,0],
             [0,0,0],
             [0,0,0]]  # TODO replace this with a three-by-three matrix of zeros
    player = 1
    while hasBlanks(board):
        printBoard(board)
        row,col = getPlayerMove()
        markBoard(board,row,col,player)
        player = player % 2 + 1 # switch player for next turn

main()


