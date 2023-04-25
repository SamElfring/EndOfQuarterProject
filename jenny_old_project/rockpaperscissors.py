import random
import getpass

OPTIONS = {
    "Rock" : "1",
    "Paper" : "2",
    "Scissors": "3"
}


exit = False


def returnToMenu(Players):
    return Players


def playRound(choices):
    match choices[0]+choices[1]:
        case "11" | "22" | "33":
            return 2
        case "13" | "21" | "32":
            return 0
        case "31" | "12" | "23":
            return 1


def getChoice(name):
    option = ''
    if name.lower() == "computer" or name.lower() == "cpu":
        option = str(random.randint(1, 3))
        print(f"{name} has: {list(OPTIONS.keys())[list(OPTIONS.values()).index(option)]}")
    else:
        while True:
            userInput = getpass.getpass(f"{name} pick an option of type Exit to stop: ")
            if userInput.capitalize() in OPTIONS:
                option = OPTIONS[userInput.capitalize()]
                break
            elif userInput.lower() == 'exit':
                exit = True
                return
    return option


def main(Players):
    while not exit:
        choices = []
        for player in Players:
            name = player['name']
            choices.append(getChoice(name))
            if choices == [None]:
                return
            if len(choices) == 2 and choices[1] == None:
                return
        result = playRound(choices)
        try:
            print(f"{Players[result]['name']} has won!")
        except IndexError:
            print("It's a draw!")
        try:
            Players[result]['score'] += 1
        except IndexError:
            pass
        for player in Players:
            print(f"Score of {player['name']} = {player['score']}")
            continue