import tkinter  # Stands for tk interface which is the user interface

# game setup
player_x = "X"
player_o = "O"
player_turn = player_x
game_over = False
turn = 0

board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]


def check_win():
    global turn, game_over
    # horizontal check
    for r in range(3):
        if (
            board[r][0]["text"] == board[r][1]["text"] == board[r][2]["text"]
            and board[r][0]["text"]
            != ""  # forgot ["text"] so it was checking board[r][0] which prints Button widget
        ):
            display_turn["text"] = "Game is over!"
            game_over = True
        elif ( #Do not use elif here, elif is only reach if the first if does not pass as true.
            board[0][r]["text"] == board[1][r]["text"] == board[2][r]["text"]
            and board[0][r]["text"] != ""
        ):
            display_turn["text"] = "Game is over!"
            game_over = True
    if (board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"] and board[0][0]["text"] !="") or (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"] and board[0][2]["text"]!= ""):
            display_turn["text"] = "Game is over!"
            game_over = True
    if turn == 9:
            display_turn["text"] = "Tie Game!"
            game_over = True
    # vertical Check


def set_tile(r, c):
    global player_turn, turn, game_over  # Python interprets player_turn locally, since player_turn is a global var, we have to tell python to refer to the global var with this, not the local one in func
    # We only use global when we want to modify a value

    if not game_over:
        if board[r][c]["text"] == "":
            board[r][c]["text"] = player_turn
            if (
                player_turn == player_x
            ):  # e.g we access player_x to check but we don't actually modify it
                player_turn = player_o
            else:
                player_turn = player_x  # Here we modify player_turn
            display_turn["text"] = f"Player {player_turn}'s Turn: Turn{turn}"
            turn += 1
            check_win()
        else:
            display_turn["text"] = f"This spot is already taken"


def new_game():
    global player_turn, game_over, turn
    turn = 0
    game_over = False
    player_turn = player_x
    display_turn["text"] = f"Player {player_turn}'s Turn"
    for row in range(3):
        for column in range(3):
            board[row][column] = tkinter.Button(
                frame,
                text="",
                font=("Consolas", 50, "bold"),
                width=4,
                height=1,
                command=lambda r=row, c=column: set_tile(r, c),
            )  # use command=lambda because we need to pass arguments!
            board[row][column].grid(row=row + 1, column=column)


# window setup
window = tkinter.Tk()  # create game window
window.title("Tic Tac Toe")
window.resizable(False, False)

frame = tkinter.Frame(window)  # create a frame inside the var window
display_turn = tkinter.Label(
    frame, text=f"Player {player_turn}'s Turn", font=("Consolas", 20)
)
display_turn.grid(
    row=0, column=0, columnspan=3
)  # colspan =3 because zero based indexing stops just before 3

for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(
            frame,
            text="",
            font=("Consolas", 50, "bold"),
            width=4,
            height=1,
            command=lambda r=row, c=column: set_tile(r, c),
        )  # use command=lambda because we need to pass arguments!
        board[row][column].grid(row=row + 1, column=column)

restart_button = tkinter.Button(
    frame, text="Restart Game", font=("Consolas", 20), command=new_game
)  # pass function in command if we dont need to pass args
restart_button.grid(row=4, column=0, columnspan=3, sticky="EW")
frame.pack()  # .pack() is used to display the widgets (display_turn inside frame and frame inside window) and arrange how it is placed.


window.mainloop()  # Keep the window active until the user click x to close
