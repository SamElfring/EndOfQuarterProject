import requests, random, time

score_player1 = 0
score_player2 = 0


def play_game(player1, player2, score_player1, score_player2):

    questions = requests.api.get("https://the-trivia-api.com/api/questions?limit=50&difficulty=easy").json()
    amount_of_rounds = 0

    while True:
        round_amount = int(input("\nHow many rounds would you like to play? (3 - 20): "))
        if round_amount < 3 or round_amount > 20:
            print("The requested round count was either too low or too high")
        else:
            amount_of_rounds += round_amount
            break

    player1_turn = True
    for index, item in enumerate(questions):
        if player1_turn:
            print(f"\n{player1}'s turn, {amount_of_rounds} rounds left")
        else:
            print(f"\n{player2}'s turn, {amount_of_rounds} rounds left")        

        print(f"""Question {(index + 1)}: {item['question']}""")
        possible_answers = [item['correctAnswer']]
        possible_answers.extend(item['incorrectAnswers'])
        random.shuffle(possible_answers)

        for index, pos_answer in enumerate(possible_answers):
            print(f""" {index + 1}: {pos_answer}""")

        if player1_turn:
            while True:
                try:
                    answer = int(input("Please give your answer (1-4): "))
                    if answer < 1 or answer > 4:
                        print("That's not a number from 1-4")
                    else:
                        break
                except ValueError:
                    print("That's not a number, Try again.")
        else:
            if player2 is not "CPU":
                answer = int(input("Please give your answer (1-4): "))
            elif player2 == "CPU":
                print(f"\n{player2} is thinking....")
                time.sleep(2)
                answer = random.randint(1, 4)
                print(f"The CPU guessed: {answer}")
                
        if possible_answers[answer -1] == item['correctAnswer']:
            print(f"\nCorrect Answer!")
            amount_of_rounds -= 1
            if player1_turn:
                score_player1 += 1
            else:
                score_player2 += 1
            print(f"{player1}: {score_player1}  |  {player2}: {score_player2}")
        else:
            print(f"""\nIncorrect answer!
The correct answer is {item['correctAnswer']} """)
            print(f"Current score: {player1}: {score_player1}  |  {player2}: {score_player2}")

            amount_of_rounds -= 1
        player1_turn = not player1_turn
        check_round_over(player1, player2, score_player1, score_player2, amount_of_rounds)


def play_again(player1, player2):

    while True:
        go_again = input("\nWould you like to go again? (yes/no): ").lower()
        if go_again == 'yes':
            play_game(player1, player2, score_player1, score_player2)
        elif go_again == 'no':
            exit()
        else:
            print("That's not an option please type yes or no")


def check_round_over(player1, player2, score_player1, score_player2, amount_of_rounds):

    if amount_of_rounds == 1:
        print("\nLast round!!")
    if amount_of_rounds == 0:
        print(f"\nGame over, the final score is: {player1}: {score_player1}  |  {player2}: {score_player2}")
        if score_player1 > score_player2:
            print(f"This means that {player1} has won! Better luck next time {player2}!")
        elif score_player2 > score_player1:
            print(f"This means that {player2} has won! Better luck next time {player1}!")
        else: 
            print("Which means it is a draw, seems like you both have the same level of intelligence")
        play_again(player1, player2)

def main(score_player1, score_player2):

    print("""\n**Hello there welcome to the quiz game**
    In this game you will be tasked to answer some questions all these questions are multiple choice. 
    You can answer them by choosing the number that is infront of the respective answer.
    \nGood luck and have fun!\n""")

    player1 = 'Hans'
    play_vs = input("""Would you like to play with two users or against the computer (CPU)?
 1. With two users
 2. CPU
Please choose an option (1 or 2): """)

    if play_vs == "1":
        player2 = 'Willem'
    elif play_vs == "2":
        player2 = "CPU"
            
    play_game(player1, player2, score_player1, score_player2)