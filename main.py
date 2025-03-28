title = 'Welcome to Crosses and Noughts!\n'
print(title.upper())


def create_game_field():
    while True:
        try:
            field_width = int(input("Enter the dimensions of the playing field (3, 6 or 12): "))
            if field_width in [3, 6, 12]:
                game_field = [[' ' for _ in range(field_width)] for _ in range(field_width)]
                print("The playing field has been successfully created!")
                return game_field
            else:
                print("Invalid field size. Please choose 3, 6 or 12.")
        except ValueError:
            print("Please enter a valid number!")

def character_selection():
    while True:
        player_one = input('Choose a character of player one (X or O): ').upper()
        if player_one not in ['X', 'O']:
            print("Error: Please choose either X or O.")
            continue

        player_two = 'O' if player_one == 'X' else 'X'
        print(f"Player Two will be {player_two}")
        return player_one, player_two


def print_field(field):
    size = len(field)
    # Print column numbers
    print("   " + "  ".join(str(i) for i in range(size)))
    # Print separator line
    print("  " + "+---" * size + "+")

    for i, row in enumerate(field):
        print(f"{i} | " + " | ".join(cell if cell != ' ' else ' ' for cell in row) + " |")
        print("  " + "+---" * size + "+")


def is_winner(field, player):
    size = len(field)

    # Check rows and columns
    for i in range(size):
        if all(cell == player for cell in field[i]):  # Check row
            return True
        if all(field[j][i] == player for j in range(size)):  # Check column
            return True

    # Check diagonals
    if all(field[i][i] == player for i in range(size)):  # Main diagonal
        return True
    if all(field[i][size - 1 - i] == player for i in range(size)):  # Anti-diagonal
        return True

    return False


def is_draw(field):
    return all(cell != ' ' for row in field for cell in row)


def game_loop():
    field = create_game_field()
    player_one, player_two = character_selection()
    current_player = player_one
    print('\nYour playing field looks like this:')
    print_field(field)

    while True:
        print(f"\nPlayer {current_player}'s turn")
        while True:
            try:
                x = int(input('Enter column number (0 to {}): '.format(len(field) - 1)))
                y = int(input('Enter row number (0 to {}): '.format(len(field) - 1)))

                if x < 0 or x >= len(field) or y < 0 or y >= len(field):
                    print("Coordinates out of bounds! Try again.")
                elif field[y][x] != ' ':
                    print("This cell is already taken! Try again.")
                else:
                    break
            except ValueError:
                print("Please enter valid numbers!")

        field[y][x] = current_player
        print_field(field)

        if is_winner(field, current_player):
            print(f"\nPlayer {current_player} wins! Congratulations!")
            break

        if is_draw(field):
            print("\nIt's a draw! The field is full.")
            break

        current_player = player_two if current_player == player_one else player_one

    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        game_loop()
    else:
        print("Thanks for playing!")


# Start the game
game_loop()