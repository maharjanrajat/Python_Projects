#display board

from IPython.display import clear_output
import IPython

# Use while loops and functions to run game
print("Welcome to TIC TAC TOE")

def display_board(board):
    clear_output()
    
    print(board[7]+'   | '+board[8]+' |   '+board[9])
    print('____|_ _|____')
    print(board[4]+'   | '+board[5]+' |   '+board[6])
    print('____|_ _|____')
    print(board[1]+'   | '+board[2]+' |   '+board[3])
    print('    |   |    ')
    

# take player input and assign as X or O.
def player_input():
    
    '''
    OUTPUT = (Player 1 marker, Player 2 marker)
    '''
   
    
    marker = ''
    
    # Keep asking player 1 to choose X or O
    
    while marker != 'X' and marker != 'O':
        marker = input('Player 1: choose X or O: ').upper()
    
    # Assign player 2 as the opposite marker
    player1 = marker
    
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
        
    return (player1,player2)

player1_marker, player2_marker = player_input()

# Take X or O and a desired position(1-9) and assign it to the board
def place_marker(board,marker,position):
    
    board[position]=marker
    
# Take board and mark(X or O) and then check to see if that mark has won.
def win_check(board,mark):
    
    # Win tic tac toe?
    return(
    # All rows are same mark
    (board[7] == board[8] == board[9] == mark) or
    (board[4] == board[5] == board[6] == mark) or
    (board[1] == board[2] == board[3] == mark) or
    
    # All columns are same mark
    (board[7] == board[4] == board[1] == mark) or
    (board[8] == board[5] == board[2] == mark) or
    (board[9] == board[6] == board[3] == mark) or
     
    # All diagonals are same mark
    (board[7] == board[5] == board[3] == mark) or
    (board[9] == board[5] == board[1] == mark)
    )
    
# To decide which player goes first.
import random

def choose_first():
    
    flip = random.randint(0,1)
    
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'
    
# To check if the position on board is freely available or not.
def space_check(board,position):
    
    return board[position] == ' '
# To check if the board is full. True if Full False otherwise.
def full_board_check(board):
    
    for i in range(1,10):
        if space_check(board,i):
            return False
        
    # Board is full if True
    return True

# Ask for next position (1-9) and check if free or not. If free return the position for later use.
def player_choice(board):
    
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        
        position = int(input('Choose a position: (1-9)'))
        
    return position

# Ask if they want to play again
def replay():
    
    choice = input("Play again? Enter Yes or No")
    
    return choice == 'Yes'



while True:
    # Reset the board
    the_board = [' ']*10
    player1_marker,player2_marker = player_input()
    
    turn = choose_first()
    print(turn+ ' will go first.')
    
    play_game = input("Are you ready to play? Enter Yes or No:")
    
    if play_game == 'Yes':
        game_on = True
    else:
        game_on = False
        
    # Actual game play
    while game_on:
        if turn == 'Player 1':
            
            #Player1's turn
            
            # show the board
            display_board(the_board)
            
            # choose a position
            position = player_choice(the_board)
            
            # place the marker on position
            place_marker(the_board,player1_marker,position)
            
            # check if they won
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print("Congratulations! Player 1 have won the game!")
                game_on = False
            else:
                # check if there is a tie
                if full_board_check(the_board):
                    display_board(the_board)
                    print("It's a Tie!")
                    break
                else:
                    turn = 'Player 2'
            
        else:
            #player2's turn
            
            # show the board
            display_board(the_board)
            
            # choose a position
            position = player_choice(the_board)
            
            # place the marker on position
            place_marker(the_board,player2_marker,position)
            
            # check if they won
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print("Congratulations! Player 2 have won the game!")
                game_on = False
            else:
                # check if there is a tie
                if full_board_check(the_board):
                    display_board(the_board)
                    print("It's a Tie!")
                    break
                else:
                    turn = 'Player 1'
                    
                    
           
        
    # break out of the while loop               
    if not replay():
        break
    

