import connect_four

def main():
    title = """
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
    print(title)

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

    # TODO: Print winner


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