#Implementation of Martin Gardner's 'Hexapawn'

#Implement MENACE, from article. Checkers playing robot.

#Guide to the board:

# 1 2 3
# 4 5 6
# 7 8 9

#Moves are on page 6.
#Move1 = {'Left': ['8x4', '8-5', '9-6'], 'Center': ['7-4', '7x5']}


import random

#Describe moves in term of position:

#Human is X, Computer is O

board = {1: ' ', 2: ' ', 3: ' ',
4: ' ', 5: ' ', 6: ' ',
7: ' ', 8: ' ', 9: ' '}
def printBoard(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('\n')    
    


def starting():
    board[1] = 'O'
    board[2] = 'O'
    board[3] = 'O'
    board[7] = 'X'
    board[8] = 'X'
    board[9] = 'X'

starting()

def CPUlegalMove(board, start, end):
    #Checking for capture
    if start == (1 or 3) and (end == 5 and board[5] == 'X'):
        return True
    elif start == 2 and ((end == 4 or 6) and (board[4] or board[6]) == 'X'):
        return True
    elif start == (4 or 6) and (end == 8 and board[8] == 'X'):
        return True
    elif start == 5 and ((end == 7 or 9) and (board[7] or board[9]) == 'X'):
        return True
    #Check if column in front is empty
    elif board[start+3] == ' ':
        return True

def CPUMove(board):
    pieces = []
    legal = {}

    for i in range(1,10):
        if board[i] == 'O':
            pieces.append(i)
    print(pieces)
    for piece in pieces:
        for num in range(piece,10):
            if CPUlegalMove(board, piece, num):
                legal[piece] = num
    print(legal)
    
        


#If situation has already occurred and always results in a loss, do not make move.

def makeMove(board, letter, move):
    board[move] = letter

#Ask player for move
printBoard(board)
oldpiece = int(input('What piece would you like to move? '))
newpiece = int(input('Where would you like to move the piece? '))
board[oldpiece] = ' '
board[newpiece] = 'X'
printBoard(board)

print("This is the board.")
print(board)

CPUMove(board)

#AI move
#TODO

#printBoard(board)

#Check if winning
def win():
    if board['top-L'] == 'X' or board['top-M'] == 'X' or board['top-R'] == 'X':
        print("Player wins. AI will learn from this.")
    if board['low-L'] == 'O' or board['low-M'] == 'O' or board['low-R'] == 'O':
        print("AI wins. AI will not change.")

#AI changes values due to loss
#TODO

# def checkWin():
#     board['top-L'] = 'X'

# checkWin()
# printBoard(board)
# win()