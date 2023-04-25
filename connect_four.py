TITLE = """\n
  ___  __   __ _  __ _  ____  ___  ____    ____  __   _  _  ____ 
 / __)/  \ (  ( \(  ( \(  __)/ __)(_  _)  (  __)/  \ / )( \(  _ \\
( (__(  O )/    //    / ) _)( (__   )(     ) _)(  O )) \/ ( )   /
 \___)\__/ \_)__)\_)__)(____)\___) (__)   (__)  \__/ \____/(__\_)
"""
RULES = """\nRULES:
    1. Players must connect 4 of the same characters (X or O) in a row to win.
    2. Only one piece is played at a time.
    3. The game ends when there is a 4-in-a-row or a stalemate.
    
    Team 1 is: X
    Team 2 is: O"""
BOARD_WIDTH = 7
BOARD_HEIGHT = 6

def play(team1, team2):
    print(TITLE)
    print(RULES)
    print("\nThe board looks like this:")
    board = [[' ' for i in range(BOARD_WIDTH)] for i in range(BOARD_HEIGHT)]
    draw_board(board)
    
    current_turn = 0
    while True:
        current_team = team1 if current_turn % 2 == 0 else team2
        char = 'X' if current_team["name"] == team1["name"] else 'O'
        accepted_values = [i + 1 for i in range(len(board[0]))]

        row = select_turn(current_team, accepted_values)
        while board[0][row] != ' ':
            print("This column is full")
            row = select_turn(current_team, accepted_values)

        for column in reversed(board):
            if column[row] == ' ':
                column[row] = char
                break

        draw_board(board)
        if current_turn > 3 and check_win(board, char):
            print("\nWe have a winner")
            print(f"{current_team['name']} has won!")
            current_team["points"] += 1
            break
        current_turn += 1


def check_win(board, char):
    for w in range(BOARD_WIDTH):
        for h in range(BOARD_HEIGHT):
            # Check horizontal
            try:
                if board[h][w] == char and board[h][w + 1] == char and board[h][w + 2] == char and board[h][w + 3] == char:
                    return True
            except IndexError:
                pass
            # Check vertical
            try:
                if board[h][w] == char and board[h + 1][w] == char and board[h + 2][w] == char and board[h + 3][w] == char:
                    return True
            except IndexError:
                pass

    # Check diagonal from left to right
    for h in range(BOARD_HEIGHT - 3):
        for w in range(BOARD_WIDTH - 3):
            try:
                if board[h][w] == char and board[h+1][w+1] == char and board[h+2][w+2] == char and board[h+3][w+3] == char:
                    return True
            except IndexError:
                pass

    # Check diagonal from right to left
    for h in range(BOARD_HEIGHT - 3):
        for w in range(3, BOARD_WIDTH):
            try:
                if board[h][w] == char and board[h+1][w-1] == char and board[h+2][w-2] == char and board[h+3][w-3] == char:
                    return True
            except IndexError:
                pass


def select_turn(team, accepted_values):
    while True:
        turn = input(f"\n{team['name']} please enter a row number: ")
        try:
            turn = int(turn)
        except ValueError:
            print("Error: That is not a number")
            continue
        
        if turn not in accepted_values:
            print("Error: Input must be in", [value for value in accepted_values])
            continue
        return turn - 1


def draw_board(board):
    print(" ___" * len(board[0]))
    for row in board:
        line = "|"
        for column in row:
            line += f" {column if column != None else ' '} |"
        print(line)
    print(" ‾‾‾" * len(board[0]))
    numbers = ""
    for i in range(len(board[0])):
        numbers += f"  {i + 1} "
    print(numbers)