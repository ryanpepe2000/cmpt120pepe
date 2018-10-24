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
    if board[row][col] == 0:
        board[row][col] = player
    pass

def getPlayerMove():
    x = int(input("Enter the row: "))
    y = int(input("Enter the column: "))
    return x,y 

def hasBlanks(board):
    for row in range(3):
        for col in range(3):
            if board[row][col] == 0:
                return True
    return False

def main():
    board = [[0,0,0],
             [0,0,0],
             [0,0,0]]  
    player = 1
    while hasBlanks(board):
        printBoard(board)
        row,col = getPlayerMove()
        markBoard(board,row,col,player)
        player = player % 2 + 1 # switch player for next turn

main()


