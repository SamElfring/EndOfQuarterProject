import random

hl_title = """ 
  _    _ _       _                 _                            
 | |  | (_)     | |               | |                           
 | |__| |_  __ _| |__   ___ _ __  | |     _____      _____ _ __ 
 |  __  | |/ _` | '_ \ / _ \ '__| | |    / _ \ \ /\ / / _ \ '__|
 | |  | | | (_| | | | |  __/ |    | |___| (_) \ V  V /  __/ |   
 |_|  |_|_|\__, |_| |_|\___|_|    |______\___/ \_/\_/ \___|_|   
            __/ |                                               
           |___/                                                


"""
# Define categories in a dictionary
categories = {
	"Instagram Followers": {"Eminem": 39, "Adidas":  25,},
    "Instagram Followers ": {"Katy Perry": 121, "Miley Cyrus":  138,},
    "Episodes": {"Friends": 236, "The Office": 201},
    "Episodes ": {"Breaking Bad": 62, "Narcos": 50},
    "Population": {"Russia": 143, "Japan": 126},
    "Population ": {"Thailand": 72, "Turkey": 85},
    "Height": {"Chrysler Building": 319, "Petronas Towers": 452},
    "Height ": {"Lotte World Tower": 555, "One World Trade Center": 541},
    "Weight": {"Moose": 380, "Polar bear": 450},
    "Weight ": {"Hippo ": 1500, "Rhino": 1600},
}

# Define a function to play the Higher/Lower game between two teams
def play_higher_lower(team1, team2):
    print(hl_title)
    # Initialize scores and current team
    team1_score = 0
    team2_score = 0
    current_team = 1
    
    # Loop through each category and ask the teams to guess the higher option
    for category, options in categories.items():
        print(f"\n{team1['name']} vs {team2['name']}: Which/Who has more {category}?")
        for option, value in options.items():
            print(option)
        guess = input(f"\nTeam {current_team}, enter your guess: ")
        # Get the correct option
        correct_option = max(options, key=options.get)
        # If the guess is correct, update the score and print Correct!
        if guess == correct_option:
            if current_team == 1:
                team1_score += 1
            else:
                team2_score += 1
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is {correct_option}.")
        # Print the current scores
        print(f"\n{team1['name']}: {team1_score} | {team2['name']}: {team2_score}")
        # Switch to the other team
        current_team = 1 if current_team == 2 else 2
    
    # Print the final scores and the winner
    if team1_score > team2_score:
        print(f"\n{team1['name']} wins with a score of {team1_score} to {team2_score}!")
    elif team2_score > team1_score:
        print(f"\n{team2['name']} wins with a score of {team2_score} to {team1_score}!")
    else:
        print(f"\nThe game ended in a tie with a score of {team1_score} to {team2_score}!")

    team1["points"] += team1_score
    team2["points"] += team2_score
    return
