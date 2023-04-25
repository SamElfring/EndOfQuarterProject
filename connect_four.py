RULES = """\nRULES:
    1. Players must connect 4 of the same characters (X or O) in a row to win.
    2. Only one piece is played at a time.
    3. The game ends when there is a 4-in-a-row or a stalemate.
    
    Team 1 is: X
    Team 2 is: O"""
WIDTH = 7
HEIGHT = 6

def connect_four(team1, team2):
    print("\nConnect Four")
    print(RULES)
    print("\nThe board looks like this:")
    board = [[' ' for i in range(WIDTH)] for i in range(HEIGHT)]
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
            break
        current_turn += 1


def check_win(board, char):
    for w in range(WIDTH):
        for h in range(HEIGHT):
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


connect_four({
        "name": "Team1",
        "members": ["Henk", "Jan"],
        "points": 0
    },
    {
        "name": "Team2",
        "members": ["Pieter", "Joost"],
        "points": 0
    })