import connect_four
import higher_lower

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

def main():
    print(TITLE)
    print("Team 1:")
    team1 = create_team()
    print("\nTeam 2:")
    team2 = create_team()

    # TODO: Print manual

    # Start games
    input(
        "\nThe next game is Connect Four! " +
        "\nPress any key to start"
    )
    connect_four.play(team1, team2)

    input(
        "\nThe next game is Higher Lower! " +
        "\nPress any key to start"
    )
    higher_lower.play_higher_lower(team1, team2)

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


def create_team():
    team = {
        "name": "",
        "members": [],
        "points": 0
    }
    team["name"] = input("\nWhat is the name of your team? ")
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
        break

    for i in range(amount_of_team_members):
        team["members"].append(input(f"What is the name of member {i + 1}? "))
    
    return team


main()