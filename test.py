#Implementation of Martin Gardner's 'Hexapawn'
import random

#Need weighting of possibilities according to losses.
#How to decide which piece to move if more than one pawn can capture?


#Describe moves in term of position:

#Human is X, Computer is O

fail_dict = {}

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
    board[4] = 'X'
    board[8] = 'X'
    board[9] = 'X'

starting()

def CPUlegalMove(board, start):
    legal = []
    #Check if column in front is empty
    if board[start+3]  == ' ':
        legal.append(start+3)
    #Checking for capture
    if start == 1 and board[5] == 'X':
        legal.append(5)
    if start == 2 and board[4] == 'X':
        legal.append(4)
    if start == 2 and board[6] == 'X':
        legal.append(6)
    if start == 3 and board[5] == 'X':
        legal.append(5)
    if start == 4 and board[8] == 'X':
        legal.append(8)
    if start == 5 and board[7] == 'X':
        legal.append(7)
    if start == 5 and board[9] == 'X':
        legal.append(9)
    if start == 6 and board[8] == 'X':
        legal.append(8)
    #print(legal)
    return legal


def CPUMove(board):
    pieces = [2]
    potential_moves = []
    # for i in range(1,10):
    #     if board[i] == 'O':
    #         pieces.append(i)
    #         break
    print(pieces)
    for piece in pieces:
        potential_moves.append(CPUlegalMove(board,piece))
#If non-zero, run through potential_moves
    valid = potential_moves[0]
    #print(valid)
    #Move the piece, empty old space.
    decision = random.choice(valid)
    board[piece] = ' '
    board[decision] = 'O'
    #print(board)
    printBoard(board)

#Try lowest number first, then evaluate in bank.

printBoard(board)

CPUMove(board)