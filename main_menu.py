import connect_four
import higher_lower
import quiz
import scavenger_hunt

TITLE = """
 _____       _    _____ ___    _____             _              _____           _         _   
|   __|___ _| |  |     |  _|  |     |_ _ ___ ___| |_ ___ ___   |  _  |___ ___  |_|___ ___| |_ 
|   __|   | . |  |  |  |  _|  |  |  | | | .'|  _|  _| -_|  _|  |   __|  _| . | | | -_|  _|  _|
|_____|_|_|___|  |_____|_|    |__  _|___|__,|_| |_| |___|_|    |__|  |_| |___|_| |___|___|_|  
                                    |__|                                        |___|            
Made By:
    - Thijs Bakker
    - Jeremy de Groot
    - Jenny Nalband
    - Sam Elfring   
"""

RESULTS = """\n
  _______ _            _____                 _ _       
 |__   __| |          |  __ \               | | |      
    | |  | |__   ___  | |__) |___  ___ _   _| | |_ ___ 
    | |  | '_ \ / _ \ |  _  // _ \/ __| | | | | __/ __|
    | |  | | | |  __/ | | \ \  __/\__ \ |_| | | |_\__ \\
    |_|  |_| |_|\___| |_|  \_\___||___/\__,_|_|\__|___/
"""

MANUAL = """\nOur project consist out of 4 small minigames.
These minigames are
    - Higher Lower (1 point per answer)
    - Connect Four (5 points for the winner)
    - Scavenger Hunt (5 points for the winner)
    - Quiz (1 point per answer)

The two teams will play each other for points,
the team with the most points at the end is the winner!    
"""

def main():
    print(TITLE)
    print("Team 1:")
    team1 = create_team()
    print("\nTeam 2:")
    team2 = create_team()

    print(MANUAL)

    # Start games
    next_game("Higher Lower")
    higher_lower.play_higher_lower(team1, team2)

    next_game("Connect Four")
    connect_four.play(team1, team2)

    next_game("Scavenger Hunt")
    scavenger_hunt.scavenger_hunt_main(team1, team2)

    print("This round is only for team " + team1["name"])
    next_game("Quiz")
    team1["points"] += quiz.run_quiz()

    print("This round is only for team " + team2["name"])
    next_game("Quiz")
    team2["points"] += quiz.run_quiz()

    # Print Winner
    print(RESULTS)
    print("\nAll games have concluded!")
    print("And the winner is:\n")
    if team1["points"] > team2["points"]:
        print(team1["name"])
    elif team1["points"] < team2["points"]:
        print(team2["name"])
    else:
        print("It is a draw!")

    print("\nResults:")
    print(f"Team: {team1['name']} ended with {team1['points']} total points!")
    print(f"Team: {team2['name']} ended with {team2['points']} total points!")


def next_game(name):
    input(
        f"\nThe next game is {name}! " +
        "\nPress Enter to start"
    )


def create_team():
    team = {
        "name": "",
        "members": [],
        "points": 0
    }
    while True:
        team_name = input("\nWhat is the name of your team? ")
        if not team_name:
            print("Error: Name must be 1 character or longer")
            continue
        team["name"] = team_name
        break

    while True:
        amount_of_team_members = input("How many members does your team have? ")

        try:
            amount_of_team_members = int(amount_of_team_members)
        except ValueError:
            print("Error: That is not a number")
            continue

        if amount_of_team_members <= 0:
            print("Error: Team must have 1 or more members")
            continue
        if amount_of_team_members > 5:
            print("Error: Team cannot contain more than 5 members")
            continue
        break

    for i in range(amount_of_team_members):
        team["members"].append(input(f"What is the name of member {i + 1}? "))
    
    return team


main()