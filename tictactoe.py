import random


#Player is X, computer is O
#Describe moves in term of position:
def printBoard(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('\n')    

#Define a move
def move(board,letter,play):
    board[play] = letter

# #Check if winning
def win(b, l): #b=board, l=letter
    return (
    (b[1] == l and b[2] == l and b[3] == l) or #Top row
    (b[4] == l and b[5] == l and b[6] == l) or #Middle row
    (b[7] == l and b[8] == l and b[9] == l) or #Bottom row
    (b[1] == l and b[4] == l and b[7] == l) or #First column
    (b[2] == l and b[5] == l and b[8] == l) or #Second column
    (b[3] == l and b[6] == l and b[9] == l) or #Third column
    (b[1] == l and b[5] == l and b[9] == l) or #First diagonal
    (b[3] == l and b[5] == l and b[7] == l) #Second diagonal
    )

#Artificial opponent generation
#CPU opponent reads current position, then makes choice of move based off winning and then not losing.

# def copy(board):
#     basis = []
#     for cell in board:
#         basis.append(cell)
#     return basis

def copy(board):
    basis = board.copy()
    return basis



def openSpace(board, play):
    return board[play] == ' '

#Check if space is free, done through function, will want to do with checking in place instead.



def playerMove(board):
    humanPlay = ''
    moves = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    # moves = {'1','2','3','4','5','6','7','8','9'}
    while (humanPlay not in moves) or (openSpace(board, humanPlay) == False):
        humanPlay = int(input(" What is your move? "))
    return int(humanPlay)

def noMoves(board):
    #If a space is open, then there are moves available, so returns False. If no space returns False, then there are no moves, so True.
    for num in range(1,10):
        if openSpace(board, num) == True:
            return False
    return True


def randomMove(board, moveList):
    potential = []
    for play in moveList:
        if openSpace(board,play):
            potential.append(play)
    
    if len(potential) != 0:
        return random.choice(potential)

    else:
        return None

def CPUPlay(board):
    #If computer wins with a move, take that move
    for num in range(1,10):
        print(num)
        print(board)
        duplicate = copy(board)
        print(duplicate)
        if openSpace(duplicate, num):
            move(duplicate, 'O', num)
            if win(duplicate, 'O'):
                return num

    #If player will win with a move, block that move
    for num in range(1,10):
        duplicate =copy(board)
        if openSpace(duplicate, num):
            move(duplicate, 'X', num)
            if win(duplicate, 'X'):
                return num

    #If there is not automatic win/loss, take a corner
    corners = {1,3,7,9}
    for num in corners:
        if openSpace(duplicate, num):
            return num

    #If not possible, take the center
    if openSpace(duplicate, 5):
        return 5
    
    #All else fails, take a side
    sides = {2,4,6,8}
    for num in sides:
        if openSpace(duplicate,num):
            return num

#The game itself.

# running = True
# while running:
board = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}
first = input(' Would you like to go first? y/n')
if first == 'y':
    turn = 'player'
else: 
    turn = 'computer'

playing = True

while playing:
    #Player makes move, game checks if player wins/draws and then switches to computer.
    if turn == 'player':
        printBoard(board)
        play = playerMove(board)
        move(board, 'X', play)
        # printBoard(board)
        # print("Move successful.")

        if win(board, 'X'):
            print('You win!')
            printBoard(board)
            playing = False

        elif noMoves(board) == True:
            print('You draw.')
            printBoard(board)
            playing = False
        
        else:
            turn = 'computer'

    if turn == 'computer':
        print(board)
        play = CPUPlay(board)
        move(board, 'O', play)

        if win(board, 'O'):
            print('Computer wins.')
            printBoard(board)
            playing = False

        elif noMoves(board) == True:
            print('Draw.')
            printBoard(board)
            playing = False

        else:
            turn = 'player'