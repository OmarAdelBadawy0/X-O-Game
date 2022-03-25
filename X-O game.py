board_play = [1,2,3,4,5,6,7,8,9]

def desply_board():
    print('\n\n | ' , board_play[0],' | ' , board_play[1],' | ' , board_play[2],' | ')
    print("  -----------------")
    print(' | ' , board_play[3],' | ' , board_play[4],' | ' , board_play[5],' | ')
    print("  -----------------")
    print(' | ' , board_play[6],' | ' , board_play[7],' | ' , board_play[8],' | ')
    print("  -----------------")

def X_tern(massage = "X tern ,\n Select were place you want to play in it : "):
    global board_play
    desply_board()
    check_winner()
    selection_X = int(input(massage))
    avalable_placeX(selection_X)
    board_play[selection_X-1] = 'X'
    desply_board()
    check_winner()


def O_tern(massage = "O tern ,\n Select were place you want to play in it : "):
    global board_play
    selection_O = int(input(massage))
    avalable_placeO(selection_O)
    board_play[selection_O-1] = 'O'


def avalable_placeX(place):
    global board_play

    if place < 1 or place > 9:
        X_tern("NO exixt place!! please choose number between 1 and 9 :")

    elif board_play[place-1] == "X" or board_play[place-1] == "O":
        X_tern("This place has been chosen!! try again :")

def avalable_placeO(place):
    global board_play

    if place < 1 or place > 9:
        O_tern("NO exixt place!! please choose number between 1 and 9 :")

    elif board_play[place-1] == "X" or board_play[place-1] == "O":
        O_tern("This place has been chosen!! try again")

def check_winner():
    global board_play

    if (board_play[0] == board_play[1] == board_play[2] == "X" or board_play[3] == board_play[4] == board_play[5] == "X" or board_play[6] == board_play[7] == board_play[8]=="X"
    or  board_play[0] == board_play[3] == board_play[6] == "X" or board_play[1] == board_play[4] == board_play[7] == "X" or board_play[2] == board_play[5] == board_play[8]=="X"
    or  board_play[2] == board_play[4] == board_play[6] == "X" or board_play[0] == board_play[4] == board_play[8] == "X"):

        print("Player X Win !!!!!")
        quit()

    elif (board_play[0] == board_play[1] == board_play[2] == "O" or board_play[3] == board_play[4] == board_play[5] == "O" or board_play[6] == board_play[7] == board_play[8]=="O"
    or  board_play[0] == board_play[3] == board_play[6] == "O" or board_play[1] == board_play[4] == board_play[7] == "O" or board_play[2] == board_play[5] == board_play[8]=="O"
    or  board_play[2] == board_play[4] == board_play[6] == "O" or board_play[0] == board_play[4] == board_play[8] == "O"):

        print("Player O Win !!!!!")
        quit()
    


for i in range(5):
    X_tern()
    if i == 4 :
        break
    O_tern()
print("Draw !!!!")