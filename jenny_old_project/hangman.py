import random
import time

WORDS = ["overseas", "vacation", "simple", "countryside", "levitating",
         "thirsty", "engine", "librarian", "coffeemachine", "impossible", 
         "purpose", "seventeen", "dirty", "absolutely", "firetruck", "lunchbreak"]

def check_guessed(letter, letters_guessed):
    if letter in letters_guessed:
        print(f"You already guessed '{letter}', please guess a different letter")
        return True
    return False

def play_game(player1, player2, score_player1, score_player2):
    word = random.choice(WORDS)
    letters_guessed = []
    display = "_" * len(word)
    player1_turn = True
    all_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    while True:
        print(f"\nLetters already guessed: {' '.join(letters_guessed)}")
        print(f"Current word: {display} ({len(word)} letters long)")
        if player1_turn:
            guess = input(f"{player1}, please give a letter or try to guess the full word: ").lower()
        else:
            if player2 is not "CPU":
                guess = input(f"{player2}, please give a letter or try to guess the full word: ").lower()
            elif player2 == "CPU":
                print(f"\n{player2} is thinking....")
                time.sleep(2)
                remaining_letters = [letter for letter in all_letters if letter not in letters_guessed]
                if len(remaining_letters) == 0:
                    print("No letters left to guess")
                    return play_again(score_player1, score_player2)
                    break
                guess = random.choice(remaining_letters)                     
                print(f"{player2} guessed {guess}")
        if check_guessed(guess, letters_guessed):
            continue
        if guess in word and len(guess) < 2:
            print(f"\nThe letter '{guess}' was found in the word")
            display = "".join([char if char in letters_guessed + [guess] else "_" for char in word])
            letters_guessed.append(guess)
        elif guess == word:
            print(f"\nYou correctly guessed the word: '{guess}'")
            display = "".join([char if char in letters_guessed + [guess] else "_" for char in word])
        else:
            print(f"\nThe letter/word '{guess}' was not found")
            letters_guessed.append(guess)
        if "_" not in display or word == guess:
            winner = player1 if player1_turn else player2
            print(f"\nCongratulations, {winner} won! The word was: {word}")
            if player1_turn:
                score_player1 += 1
            else:
                score_player2 += 1
            return play_again(score_player1, score_player2)
            break
        player1_turn = not player1_turn



def play_again(score_player1, score_player2):
    while True:
        go_again = input("Would you like to play again? (yes/no): ").lower().strip() 
        if go_again == 'yes':
            print(f"\nThe current score: {player1}: {score_player1} {player2}: {score_player2}")
            letters_guessed = []
            play_game(player1, player2, score_player1, score_player2)
        elif go_again == 'no':
            print(f"\nThe Final Score = {player1}: {score_player1} {player2}: {score_player2}\n")
            time.sleep(1)
            if score_player1 > score_player2:
                print(f"Which means {player1} has won!")
            elif score_player2 > score_player1:
                print(f"Which means {player2} has won!")
            else:
                print(f"Which means that it's a draw!")
            print("Adding score to total scores...")
            time.sleep(3)
            print("Thank you for playing!")
            return
        else:
            print("That's not a valid response, try again:")


def main(players):
    print("Welcome to hangman!")

    play_game(players[0]['name'], players[1]['name'], players[0]['score'], players[1]['score'])

    return players

if __name__ == '__main__':
    player1 = 'Hans'
    play_vs = input("""Would you like to play with two users or against the computer (CPU)?
    1. With two users
    2. CPU
    Please choose an option (1 or 2): """)

    if play_vs == "1":
        player2 = 'Willem'
    elif play_vs == "2":
        player2 = "CPU"

    score_player1 = 0
    score_player2 = 0

    players = [{
        'name': player1,
        'score': score_player1
    }, {
        'name': player2,
        'score': score_player2
    }]

    main(players)