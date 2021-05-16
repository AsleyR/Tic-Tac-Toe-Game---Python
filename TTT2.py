from tkinter import *

#Note: Add choice to be X or O for PvC

new_gamemode = False
play_as_O = False
player = ""
computer = "X"
x = 0 #General purpose variable for operations

board = {0: " ", 2: " ", 3: " ",
         4: " ", 5: " ", 6: " ",
         7: " ", 8: " ", 9: " "}

def turn():
    global computer
    global player
    global x
    x = x + 1

    if new_gamemode == False:
        if (x % 2) == 0:
            player = "O"
        else:
            player = "X"
    
    elif new_gamemode == True and play_as_O == False:
        computer = "O"
        player = "X"
    
    elif new_gamemode == True and play_as_O == True:
        computer = "X"
        player = "O"

    return player

#Left as a debug tool
def print_board():
    print(board[0] + "|" + board[2] + "|" + board[3])
    print("-+-+-")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print("-+-+-")
    print(board[7] + "|" + board[8] + "|" + board[9])
    print("\n")

def free_space(position):
    if board[position] == " ":
        return True
    else:
        return False

def place_mark(position, mark):
    if free_space(position) == True:
        board[position] = mark
        print_board()

        if check_win() and who_won(mark):
            if winner_label["text"] == "":
                winner_label["text"] = mark + " Wins!"
                print(mark + " WINS!")

        if check_draw() == True:
            if winner_label["text"] == "":
                winner_label["text"] = "Draw!"
            print("DRAW!")
        
    else:
        print("Space is used.")

def check_draw():
    for key in board.keys():
        if (board[key] == " "):
            return False
    return True

def check_win():
    #Check horizontal
    if board[0] == board[2] and board[0] == board[3] and board[0] != " ":
        return True
    elif board[4] == board[5] and board[4] == board[6] and board[4] != " ":
        return True
    elif board[7] == board[8] and board[7] == board[9] and board[7] != " ":
        return True
    
    #Check vertical
    elif board[0] == board[4] and board[0] == board[7] and board[0] != " ":
        return True
    elif board[2] == board[5] and board[2] == board[8] and board[2] != " ":
        return True
    elif board[3] == board[6] and board[3] == board[9] and board[3] != " ":
        return True

    #Check diagonal
    elif board[0] == board[5] and board[0] == board[9] and board[0] != " ":
        return True
    elif board[3] == board[5] and board[3] == board[7] and board[3] != " ":
        return True

    else:
        return False

def who_won(mark):
    #Check horizontal
    if board[0] == board[2] and board[0] == board[3] and board[0] == mark:
        return True
    elif board[4] == board[5] and board[4] == board[6] and board[4] == mark:
        return True
    elif board[7] == board[8] and board[7] == board[9] and board[7] == mark:
        return True
    
    #Check vertical
    elif board[0] == board[4] and board[0] == board[7] and board[0] == mark:
        return True
    elif board[2] == board[5] and board[2] == board[8] and board[2] == mark:
        return True
    elif board[3] == board[6] and board[3] == board[9] and board[3] == mark:
        return True

    #Check diagonal
    elif board[0] == board[5] and board[0] == board[9] and board[0] == mark:
        return True
    elif board[3] == board[5] and board[3] == board[7] and board[3] == mark:
        return True
    
    else:
        return False

#I don't know why, but board is sorted like 0, 2, 3, 4.... Had to rename board[1] to board[0] 
# to avoid KeyErrors
def computer_move():
    best_score = -800
    best_move = 0
    for key in board.keys():
        if (free_space(key) == True):
            board[key] = computer
            score = minimax(0, False)
            board[key] = " "
            if (score > best_score):
                best_score = score
                best_move = key

    if best_move == 0 and free_space(best_move) == True:
        btn1.config(text=computer, bg="grey70", state=DISABLED)
    elif best_move == 2 and free_space(best_move) == True:
        btn2.config(text=computer, bg="grey70", state=DISABLED)
    elif best_move == 3 and free_space(best_move) == True:
        btn3.config(text=computer, bg="grey70", state=DISABLED)
    elif best_move == 4 and free_space(best_move) == True:
        btn4.config(text=computer, bg="grey70", state=DISABLED)
    elif best_move == 5 and free_space(best_move) == True:
        btn5.config(text=computer, bg="grey70", state=DISABLED)
    elif best_move == 6 and free_space(best_move) == True:
        btn6.config(text=computer, bg="grey70", state=DISABLED)
    elif best_move == 7 and free_space(best_move) == True:
        btn7.config(text=computer, bg="grey70", state=DISABLED)
    elif best_move == 8 and free_space(best_move) == True:
        btn8.config(text=computer, bg="grey70", state=DISABLED)
    elif best_move == 9 and free_space(best_move) == True:
        btn9.config(text=computer, bg="grey70", state=DISABLED)

    place_mark(best_move, computer)

    return


def minimax(depth, isMaximizing):
    if (who_won(computer)):
        return 1
    elif (who_won(player)):
        return -1
    elif (check_draw()):
        return 0

    if (isMaximizing):
        best_score = -800
        for key in board.keys():
            if (free_space(key) == True):
                board[key] = computer
                score = minimax(depth + 1, False)
                board[key] = " "
                if (score > best_score):
                    best_score = score
        return best_score

    else:
        best_score = 800
        for key in board.keys():
            if (free_space(key) == True):
                board[key] = player
                score = minimax(depth + 1, True)
                board[key] = " "
                if (score < best_score):
                    best_score = score
        return best_score


def comp_turn():
    if new_gamemode == True:
        computer_move()
        

def reset():
    global x
    x = 0
    for i in board.keys(): #i is a random variable
        board[i] = " "
    print_board()
    winner_label["text"] = ""

    btn1.config(text="", bg="lightgrey", state=NORMAL)
    btn2.config(text="", bg="lightgrey", state=NORMAL)
    btn3.config(text="", bg="lightgrey", state=NORMAL)
    btn4.config(text="", bg="lightgrey", state=NORMAL)
    btn5.config(text="", bg="lightgrey", state=NORMAL)
    btn6.config(text="", bg="lightgrey", state=NORMAL)
    btn7.config(text="", bg="lightgrey", state=NORMAL)
    btn8.config(text="", bg="lightgrey", state=NORMAL)
    btn9.config(text="", bg="lightgrey", state=NORMAL)

def click1():
    turn()
    if new_gamemode == True:
        place_mark(0, player)
        comp_turn()
    else:
        place_mark(0, player)

    btn1["text"] = player
    btn1["state"] = DISABLED
    btn1["bg"] = "grey70"

def click2():
    turn()
    if new_gamemode == True:
        place_mark(2, player)
        comp_turn()
    else:
        place_mark(2, player)

    btn2["text"] = player
    btn2["state"] = DISABLED
    btn2["bg"] = "grey70"

def click3():
    turn()
    if new_gamemode == True:
        place_mark(3, player)
        comp_turn()
    else:
        place_mark(3, player)

    btn3["text"] = player
    btn3["state"] = DISABLED
    btn3["bg"] = "grey70"

def click4():
    turn()
    if new_gamemode == True:
        place_mark(4, player)
        comp_turn()
    else:
        place_mark(4, player)

    btn4["text"] = player
    btn4["state"] = DISABLED
    btn4["bg"] = "grey70"

def click5():
    turn()
    if new_gamemode == True:
        place_mark(5, player)
        comp_turn()
    else:
        place_mark(5, player)

    btn5["text"] = player
    btn5["state"] = DISABLED
    btn5["bg"] = "grey70"

def click6():
    turn()
    if new_gamemode == True:
        place_mark(6, player)
        comp_turn()
    else:
        place_mark(6, player)

    btn6["text"] = player
    btn6["state"] = DISABLED
    btn6["bg"] = "grey70"

def click7():
    turn()
    if new_gamemode == True:
        place_mark(7, player)
        comp_turn()
    else:
        place_mark(7, player)
        
    btn7["text"] = player
    btn7["state"] = DISABLED
    btn7["bg"] = "grey70"

def click8():
    turn()
    if new_gamemode == True:
        place_mark(8, player)
        comp_turn()
    else:
        place_mark(8, player)

    btn8["text"] = player
    btn8["state"] = DISABLED
    btn8["bg"] = "grey70"

def click9():
    turn()
    if new_gamemode == True:
        place_mark(9, player)
        comp_turn()
    else:
        place_mark(9, player)

    btn9["text"] = player
    btn9["state"] = DISABLED
    btn9["bg"] = "grey70"

def new_game():
    reset()
    if play_as_O == True:
        pvc2()

def pvp():
    global new_gamemode
    global play_as_O
    new_gamemode = False
    play_as_O = False
    reset()

#Player go first and plays as X
def pvc1():
    global new_gamemode
    global play_as_O
    new_gamemode = True
    play_as_O = False
    reset()

#Player go second and plays as O
def pvc2():
    global new_gamemode
    global play_as_O
    reset()
    new_gamemode = True
    play_as_O = True
    turn()
    comp_turn()

print_board()

window = Tk()
window.title("Tic Tac Toe")
window.geometry("300x300")
window.resizable(False, False)
window.columnconfigure(0, weight=1)

main_label = Label(text="Tic Tac Toe", pady= 10, font=("Helvetica", 15))
main_label.pack()

frameM = Frame(window)
frameM.pack()
frame1 = Frame(window)
frame1.pack()
frame2 = Frame(window)
frame2.pack()
frame3 = Frame(window)
frame3.pack()

btn1 = Button(frame1, text="", bg="lightgrey", width= 8, pady= 15, font=("Helvetica", 10), command=click1)
btn1.pack(side=LEFT)
btn2 = Button(frame1, text="", bg="lightgrey", width= 8, pady= 15, font=("Helvetica", 10), command=click2)
btn2.pack(side=LEFT)
btn3 = Button(frame1, text="", bg="lightgrey", width= 8, pady= 15, font=("Helvetica", 10), command=click3)
btn3.pack(side=LEFT)

btn4 = Button(frame2, text="", bg="lightgrey", width= 8, pady= 15, font=("Helvetica", 10), command=click4)
btn4.pack(side=LEFT)
btn5 = Button(frame2, text="", bg="lightgrey", width= 8, pady= 15, font=("Helvetica", 10), command=click5)
btn5.pack(side=LEFT)
btn6 = Button(frame2, text="", bg="lightgrey", width= 8, pady= 15, font=("Helvetica", 10), command=click6)
btn6.pack(side=LEFT)

btn7 = Button(frame3, text="", bg="lightgrey", width= 8, pady= 15, font=("Helvetica", 10), command=click7)
btn7.pack(side=LEFT)
btn8 = Button(frame3, text="", bg="lightgrey", width= 8, pady= 15, font=("Helvetica", 10), command=click8)
btn8.pack(side=LEFT)
btn9 = Button(frame3, text="", bg="lightgrey", width= 8, pady= 15, font=("Helvetica", 10), command=click9)
btn9.pack(side=LEFT)

winner_label = Label(text="", fg="red", pady= 10, font=("Helvetica", 13))
winner_label.pack()

menu_bar  = Menu(frameM)
window.config(menu = menu_bar)

game_menu = Menu(menu_bar, tearoff=0)
option_menu = Menu(menu_bar, tearoff=0)
change_sign_menu = Menu(option_menu, tearoff=0)

menu_bar.add_cascade(label="Game", menu=game_menu)
menu_bar.add_cascade(label="Options", menu=option_menu)

game_menu.add_command(label="New Game", command=new_game)
game_menu.add_separator()
game_menu.add_command(label="Exit", command=window.quit)

option_menu.add_command(label="PvP", command=pvp)
option_menu.add_cascade(label="PVC", menu=change_sign_menu)

change_sign_menu.add_command(label="Play as X", command=pvc1)
change_sign_menu.add_command(label="Play as O", command=pvc2)


window.mainloop()