starting_values = {"1": "1", "2": "2", "3": "3",
                "4": "4", "5": "5", "6": "6",
                "7": "7", "8": "8", "9": "9"}

input_values = {"1": " ", "2": " ", "3": " ",
                "4": " ", "5": " ", "6": " ",
                "7": " ", "8": " ", "9": " "}


def display_board():
    print(" ---" * 3)
    print(f"| {starting_values['1']} | {starting_values['2']} | {starting_values['3']} |")
    print(" ---" * 3)
    print(f"| {starting_values['4']} | {starting_values['5']} | {starting_values['6']} |")
    print(" ---" * 3)
    print(f"| {starting_values['7']} | {starting_values['8']} | {starting_values['9']} |")
    print(" ---" * 3)


def board():
    print(" ---" * 3)
    print(f"| {input_values['1']} | {input_values['2']} | {input_values['3']} |")
    print(" ---" * 3)
    print(f"| {input_values['4']} | {input_values['5']} | {input_values['6']} |")
    print(" ---" * 3)
    print(f"| {input_values['7']} | {input_values['8']} | {input_values['9']} |")
    print(" ---" * 3)


def check_win(count):
    if count >= 5:
        if input_values['1'] == input_values['2'] == input_values['3'] != " ":
            return True
        if input_values['4'] == input_values['5'] == input_values['6'] != " ":
            return True
        if input_values['7'] == input_values['8'] == input_values['9'] != " ":
            return True
        if input_values['1'] == input_values['4'] == input_values['7'] != " ":
            return True
        if input_values['2'] == input_values['5'] == input_values['8'] != " ":
            return True
        if input_values['3'] == input_values['6'] == input_values['9'] != " ":
            return True
        if input_values['1'] == input_values['5'] == input_values['9'] != " ":
            return True
        if input_values['3'] == input_values['5'] == input_values['7'] != " ":
            return True
        if count == 9:
            return True


def game():
    count = 0
    tiles_selected = []
    display_board()
    game_start = input("Welcome to the Tic-Tac Toe Console. The boxes are numbered as so. Press enter to continue.\n")
    game_on = True
    board()
    player_1 = input("Player 1 please choose a square.\n")
    if input_values[player_1] == " ":
        input_values[player_1] = "X"
        tiles_selected.append(player_1)
    board()
    count += 1

    while game_on:
        player_2 = input("Player 2s turn\n")
        while player_2 in tiles_selected:
            player_2 = input("Square already taken. Choose another\n")
        input_values[player_2] = "O"
        tiles_selected.append(player_2)
        board()
        count += 1
        if check_win(count):
            if count == 9:
                game_on = False
                print("Its a tie!")
            else:
                game_on = False
                print("Player 2 wins!")
                break
        player_1 = input("Player 1s turn\n")
        while player_1 in tiles_selected:
            player_1 = input("Square already taken. Choose another\n")
        input_values[player_1] = "X"
        tiles_selected.append(player_1)
        board()
        count += 1
        if check_win(count):
            if count == 9:
                game_on = False
                print("Its a tie!")
            else:
                game_on = False
                print("Player 1 wins!")

    restart = input("Would you like to replay? y/n\n").lower()
    if restart == "y":
        game()


game()
