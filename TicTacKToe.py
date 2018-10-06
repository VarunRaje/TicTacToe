import random

from IPython.display import clear_output
def displayBoard(board):

    print(board[7] + "|" + board[8] + "|" + board[9])
    print("--------")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print("--------")
    print(board[1] + "|" + board[2] + "|" + board[3])


def player_input():

    marker = ""

    while marker != 'X' and marker != 'O':
        marker =  input("Please Choose Marker Player 1:- ").upper()

    if(marker == 'X'):
        return ('X', 'O')
    else:
        return ('O', 'X')


def check_winner(board, mark):

    return((board[1] == board[2] == board[3] == mark) or
           (board[4] == board[5] == board[6] == mark) or
           (board[7] == board[8] == board[9] == mark) or
           (board[1] == board[4] == board[7] == mark) or
           (board[2] == board[5] == board[8] == mark) or
           (board[3] == board[6] == board[9] == mark) or
           (board[1] == board[5] == board[9] == mark) or
           (board[7] == board[5] == board[3] == mark)
        )

def space_check(board, postion):

    return board[postion] == ' '

def full_board_check(board):

    for i in range(1,10):
        if(space_check(board, i)):
            return False

    return True

def player_choice(board):

    position = 0

    while position not in range(1, 10) and not(space_check(board, position)):
        position = int(input("Please  choose a position 1-9 : "))

    return position


def place_marker(board, marker, position):

    #position = int(input("Player1, Please choose position for marker 1-9:- "))

    board[position] = marker

   # displayBoard(board)

    #position = int(input("Player2, Please choose position for marker 1-9:- "))

    #board[position] = player2

   # displayBoard(board)

def choose_first():

    flip = random.randint(0,1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'




if __name__ == '__main__':

    board = ['  ']*10
    displayBoard(board)

    player1, player2 = player_input()

    print("Player1 will play with " + player1)
    print("Player2 will play with " + player2)

    turn = choose_first();

    print(turn + "Will Play first")

    play_game = input("Let's Start Playing y or n? ")

    if play_game == 'y' :
        game_on = True
    else:
        game_on = False

    while game_on:

        if turn == 'Player 1':
            displayBoard(board)
            position = player_choice(board)
            place_marker(board,player1,position)
            displayBoard(board)
            if check_winner(board, player1):
                displayBoard(board)
                print("Player 1 is te winner")
                game_on = False
            else:
                if not full_board_check(board):
                    displayBoard(board)
                    print("Its Tie")
                    game_on = False
                    #break;
                else:
                    turn = "Player 2"

        else:
            displayBoard(board)
            position = player_choice(board)
            place_marker(board, player2, position)
            displayBoard(board)
            if check_winner(board, player2):
                displayBoard(board)
                print("Player 2 is the winner")
                game_on = False

            else:
                if not full_board_check(board):
                    displayBoard(board)
                    print("Its Tie")
                    game_on = False
                else:
                    turn = 'Player 1'