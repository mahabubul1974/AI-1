#TicTacToe by Naim Istiak Masum

playing_board=["_" , "_" , "_",
               "_" , "_" , "_",
               "_" , "_" , "_"]

game_going_or_not=True
current_player = "x"
winner = None
print("1. I want to play with Computer(Bot)")
print("2. I want to play with my friend")
user_right_choice=True
while user_right_choice:
    user_choise_bot=int(input("Please select whitch type of system you want to play (1 or 2) : "))
    if user_choise_bot==1 or user_choise_bot==2:
        user_right_choice=False
    else:
        print("please select 1 or 2")
        user_right_choice=True
warning_for_last_stage=0
def play_the_game():
    global winner
    global game_going_or_not
    global user_choise_bot
    global warning_for_last_stage

    display_playing_board()

    while game_going_or_not:

        handle_the_turn()

        change_player()

        if user_choise_bot==1:
            tictactoe_bot(current_player)

        check_the_winner()
        if user_choise_bot==1 and winner==None:
            if warning_for_last_stage==4:
                position_taken = False
                while not position_taken:
                    print("Warnig!!!")
                    position=int(input("you are in last stage!!! please select the position for final result (1-9) : "))
                    position=position-1
                    try:
                        if playing_board[position] != "_":
                            print("Position already taken!!!!")
                            position_taken = False
                        else:
                            position_taken = True
                    except:
                        print("Wrong position selection!!!!")

                playing_board[position] = "x"
                display_playing_board()
                check_the_winner()

        if winner=="x" or winner=="o":
            print(winner+ " won")
            game_going_or_not=False

def handle_the_turn():
    global current_player
    global user_choise_bot
    global warning_for_last_stage
    position_taken=False
    while not position_taken:
        print(current_player,"Term")
        position = int(input("Please select your position from (1-9) : "))
        position = position - 1
        try:
            if playing_board[position]!="_":
                print("Position already taken!!!!")
                position_taken=False
            else:
                position_taken=True
                warning_for_last_stage=warning_for_last_stage+1
        except:
            print("Wrong position selection!!!!")
    playing_board[position] = current_player
    if user_choise_bot==2:
        display_playing_board()


def check_for_tie():
    global  game_going_or_not
    if "_" not in playing_board:
        game_going_or_not=False
        print("tie")


def check_the_winner():
    global winner
    row_winner=check_the_rows()
    collumn_winner=check_the_collumn()
    diagonal_winner=check_the_diagonals()
    if row_winner == None and collumn_winner == None and diagonal_winner == None:
        check_for_tie()
    if row_winner=="x" or row_winner=="o":
        winner=row_winner
    elif collumn_winner=="x" or collumn_winner=="o":
        winner=collumn_winner
    elif diagonal_winner=="x" or diagonal_winner=="o":
        winner=diagonal_winner

def check_the_diagonals():
    if playing_board[0] == playing_board[4] == playing_board[8] != "-":
        return playing_board[0]
    elif playing_board[2] == playing_board[4] == playing_board[6] != "-":
        return playing_board[2]
    else:
        return None

def check_the_rows():

    if playing_board[0] == playing_board[1] == playing_board[2] != "-":
        return playing_board[0]
    elif playing_board[3] == playing_board[4] == playing_board[5] != "-":
        return playing_board[3]
    elif playing_board[6] == playing_board[7] == playing_board[8] != "-":
        return playing_board[6]
    else:
        return None

def check_the_collumn():
    if playing_board[0] == playing_board[3] == playing_board[6] != "-":
        return playing_board[0]
    elif playing_board[1] == playing_board[4] == playing_board[7] != "-":
        return playing_board[1]
    elif playing_board[2] == playing_board[5] == playing_board[8] != "-":
        return playing_board[2]
    else:
        return None

def change_player():
    global current_player

    if current_player=="x":
        current_player="o"
    elif current_player=="o":
        current_player="x"

def tictactoe_bot(current):
    from random import randint
    bot_place_free=True
    while bot_place_free:
        bot_play=randint(0,8)
        if playing_board[bot_play]=="_":
            playing_board[bot_play]=current
            bot_place_free=False
        else:
            bot_place_free=True
    change_player()
    display_playing_board()

def display_playing_board():
  print("\n")
  print(playing_board[0] + " || " + playing_board[1] + " || " + playing_board[2] + "     1 || 2 || 3")
  print(playing_board[3] + " || " + playing_board[4] + " || " + playing_board[5] + "     4 || 5 || 6")
  print(playing_board[6] + " || " + playing_board[7] + " || " + playing_board[8] + "     7 || 8 || 9")
  print("\n")


play_the_game()
