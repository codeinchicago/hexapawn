#Implementation of Martin Gardner's 'Hexapawn'

#Implement MENACE, from article. Checkers playing robot.

#Guide to the board:

# 7 8 9
# 4 5 6
# 1 2 3

#Moves are on page 6.
#Move1 = {'Left': ['8x4', '8-5', '9-6'], 'Center': ['7-4', '7x5']}

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

starting()



#Define legal move
#TODO

#Ask player for move
oldpiece = input('What piece would you like to  move?')
newpiece = input('Where would you like to move the piece?')
theBoard[oldpiece] = ' '
theBoard[newpiece] = 'X'

#AI move
#TODO

#printBoard(theBoard)

#Check if winning
def win():
    if theBoard['top-L'] == 'X' or theBoard['top-M'] == 'X' or theBoard['top-R'] == 'X':
        print("Player wins. AI will learn from this.")
    if theBoard['low-L'] == 'O' or theBoard['low-M'] == 'O' or theBoard['low-R'] == 'O':
        print("AI wins. AI will not change.")

#AI changes values due to loss
#TODO

# def checkWin():
#     theBoard['top-L'] = 'X'

# checkWin()
# printBoard(theBoard)
# win()