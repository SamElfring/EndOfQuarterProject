import random
import time

board = [" " for x in range(9)]
# Global variables that keep track of the user name and score, they are global so that they don't change

def print_board():
   row1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
   row2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
   row3 = "| {} | {} | {} |".format(board[6], board[7], board[8])

   print(f"\n -----------\n{row1}\n -----------")
   print(f"{row2}\n -----------")
   print(f"{row3}\n -----------\n")


def player_move(icon):
    
    while True:
        choice = input("Enter your move (1-9): ").strip()
        if not choice.isdigit():
            print("that's not a number, please choose a number from 1-9")
            continue
        choice = int(choice)
        if choice < 1 or choice > 9:
            print("that's not a number from 1 to 9")
        elif board[choice - 1] == " ":
            board[choice - 1] = icon
            break
        else:
            print("\nThat space is already taken!")
    
def play_game_cpu(icon):

    if icon == "X":
        while True:
            choice = input("Enter your move (1-9): ").strip()
            if not choice.isdigit():
                print("that's not a number, please choose a number from 1-9")
                continue
            choice = int(choice)
            if choice < 1 or choice > 9:
                print("that's not a number from 1 to 9")
            elif board[choice - 1] == " ":
                board[choice - 1] = icon
                break
            else:
                print("\nThat space is already taken!")
    elif icon == "O":
        print("Computer is thinking...")
        time.sleep(1)
        CPU_move(icon)

def CPU_move(icon):

    while True:
        choice = random.randint(1, 9)
        if board[choice - 1] == " ":
            board[choice - 1] = icon
            break

def is_victory(icon):
   win_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
       [0, 3, 6], [1, 4, 7], [2, 5, 8],
       [0, 4, 8], [2, 4, 6]]
   for combination in win_combinations:
       if board[combination[0]] == icon and board[combination[1]] == icon and board[combination[2]] == icon:
           return True
   return False

def play_game(player1, player2, player1_score, player2_score):
    global board
    print("\n Welcome to Tic-Tac-Toe!")
    print_board()
    print()

    while True:
        print(f"{player1}'s turn (X)")
        if player2 != "CPU":
            player_move("X")
            print_board()
            if is_victory("X"):
                player1_score += 1
                print(f"{player1} wins! Congratulations!")
                print(f"Current Score: {player1}: {player1_score} {player2}: {player2_score}")
                return play_again(player1, player2, player1_score, player2_score)
            elif " " not in board:
                print("It's a draw!")
                print(f"Current Score: {player1}: {player1_score} {player2}: {player2_score}")
                return play_again(player1, player2, player1_score, player2_score)

            print(f"{player2}'s turn (O)")
            player_move("O")
            print_board()
            if is_victory("O"):
                player2_score += 1
                print(f"{player2} wins! Congratulations!")            
                print(f"Current Score: {player1}: {player1_score} {player2}: {player2_score}")
                return play_again(player1, player2, player1_score, player2_score)
        else:
            play_game_cpu("X")
            print_board()
            if is_victory("X"):
                player1_score += 1
                print(f"{player1} wins! Congratulations!")
                print(f"Current Score: {player1}: {player1_score} {player2}: {player2_score}")
                return play_again(player1, player2, player1_score, player2_score)
            elif " " not in board:
                print("It's a draw!")
                print(f"Current Score: {player1}: {player1_score} {player2}: {player2_score}")
                return play_again(player1, player2, player1_score, player2_score)

            print(f"{player2}'s turn (O)")
            play_game_cpu("O")
            print_board()
            if is_victory("O"):
                player2_score += 1
                print(f"{player2} wins! Congratulations!")            
                print(f"Current Score: {player1}: {player1_score} {player2}: {player2_score}")
                return play_again(player1, player2, player1_score, player2_score)

def play_again(player1, player2, player1_score, player2_score):
    global board
    board = [" " for x in range(9)]
    while True:
        go_again = input("Would you like to play again? (yes/no) ").lower().strip()
        if go_again == 'yes':
            play_game(player1, player2, player1_score, player2_score)
        elif go_again == 'no':
            print("Thank you for playing!")
            print(f"Final Score: {player1}: {player1_score} {player2}: {player2_score}")
            return
        else:
            print("That's not a valid response, try again:")


def main(players):    
    play_game(players[0]['name'], players[1]['name'], players[0]['score'], players[1]['score'])

    return players

if __name__ == '__main__':
    player1= 'Hans'
    play_vs = input("""Would you like to play with two users or against the computer (CPU)?
 1. With two users
 2. CPU
Please choose an option (1 or 2): """)

    if play_vs == "1":
        player2 = 'Willem'

    elif play_vs == "2":
        player2 = "CPU"

    player1_score = 0
    player2_score = 0

    players = [{
        'name': player1,
        'score': player1_score
    }, {
        'name': player2,
        'score': player2_score
    }]

    main(players)


