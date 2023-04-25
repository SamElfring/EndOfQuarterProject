import random

STARTINGCHIPS = 10
BETWIN = 35


def playRoulette(playerList):
    betList = []
    for player in playerList:
        choices = []
        print(f"{player['name']} je hebt {player['chips']} chips!")
        while player['chips'] > 0:
            number = input()
            if number == "STOP":
                break
            elif number == "EXIT":
                exit()
            else:
                try:
                    number = int(number)
                    if number < 37:
                        choices.append(number)
                        player['chips'] -= 1
                    else:
                        print("Ingevoerde nummer is te hoog. Kies een nummer tussen 1 en 36")
                except ValueError:
                    quit()
        betList.append(choices)
    return betList


def getResult(playerList, bettings):
    outcome = random.randint(1, 1)
    for i in range(len(bettings)):
        correctBets = bettings[i].count(outcome)
        playerList[i]['chips'] += correctBets * BETWIN
    print(playerList)

# TODO zorgen dat ie continu blijft doorspelen met het juiste aantal chips


def main(Players):
    playerList = []
    for Player in Players:
        playerList.append(
            {
                'name' : Player['name'],
                'chips' : STARTINGCHIPS
            }
        )
    bettings = playRoulette(playerList)
    getResult(playerList, bettings)



Players = [
    {
        'name' : 'Nick',
        'score' : 0
    },
    {
        'name' : 'Jack',
        'score' : 0
    }
]


main(Players)