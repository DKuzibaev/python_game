title = 'Welcome to Crosses and Noughts!\n'
print(title.upper())

def create_game_field():
    field_width = int(input("Enter the dimensions of the playing field: standards 3x3, 6x6, 12x12 \n"))
    if field_width > 6:
        print("Invalid field value")
        return
    else:
        game_field = [[0 for i in range(field_width)] for j in range(field_width)]
        print("The playing field has been successfully created!")
        return game_field

def character_selection():
    while True:
        player_one = input('Choose a character of player one: X or O\n').lower()
        player_two = input('Choose a character of player two: X or O\n').lower()
        if player_one.lower() == player_two.lower():
            print("Error: You can't choose the same characters.")
            continue
        elif (player_one != "x" and player_one != "o") or (player_two != "x" and player_two != "o"):
            print("Error: You have chosen a non-existent character.")
            continue
        else:
            return player_one.upper(), player_two.upper()

def print_field():
    for i in field:
        print(i)

field = create_game_field()

player_one, player_two= character_selection()
print(f'Player One => {player_one}', f'Player Two => {player_two}\n', sep='\n')

print('Your playing field looks like this..\n')
print_field()

def game_logic(char):
    x, y = int(input('Enter number of column - ')), int(input('Enter number of row - '))

    for col in range(len(field)):
        if col == x:
            for row in range(len(field[col])):
                if row == y and row == 0:
                    field[col][row] = char

game_logic(player_one)
print_field()
