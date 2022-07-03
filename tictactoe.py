import random

#Describe moves in term of position:

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
    print('\n')    

def starting():
    theBoard['top-L'] = 'O'
    theBoard['top-M'] = 'O'
    theBoard['top-R'] = 'O'
    theBoard['low-L'] = 'X'
    theBoard['low-M'] = 'X'
    theBoard['low-R'] = 'X'


# printBoard(theBoard)
# starting()
# printBoard(theBoard)

def Move(board,letter,move):
    board[move] = letter

# #Check if winning
def win():
    if theBoard['top-L'] == 'X' or theBoard['top-M'] == 'X' or theBoard['top-R'] == 'X':
        print("Player wins. Congratulations.")
    if theBoard['low-L'] == 'O' or theBoard['low-M'] == 'O' or theBoard['low-R'] == 'O':
        print("AI wins. Better luck next time.")

# #AI changes values due to loss
# #TODO

# # def checkWin():
# #     theBoard['top-L'] = 'X'

# # checkWin()
# # printBoard(theBoard)
# # win()