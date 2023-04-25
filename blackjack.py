from blessed import Terminal
import random

CARD_DECK = 4 * ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
DEFAULT_PLAYERS = [{
    'name': 'Frank',
    'score': 2
}, {
    'name': 'CPU',
    'score': 0
}]

def is_cpu(player_name: dict) -> bool:
    return 'CPU'.lower() in player_name.lower()

def main(players: list):
    display_title_screen()

    while game_loop(players):
        print()

    for player in players:
        del player['hand']

    print("Exiting game")
    return players

def take_random_card(card_deck: list) -> str:
    card = card_deck[rand(0, len(card_deck) - 1)]
    card_deck.remove(card)

    return card

def rand(min: int, max: int) -> int:
    return random.randint(min, max)

def count_cards(hand: list) -> int:
    count = 0

    for card in hand:
        if card.isdigit():
            count += int(card)
            continue
        
        if 'A' in card:
            hand_with_ace_card = hand.copy()
            hand_with_ace_card.remove('A')
            if count_cards(hand_with_ace_card) > 20:
                count += 1
                continue

            count += 11
            continue

        count += 10

    return count

def game_loop(players: list) -> bool:
    game_round_loop(players)

    # open_menu([["Yes"], ["No"]], "Would you like to play another?")

    print("Score:")
    for player in players:
        print(f"\t {player['name']}: {player['score']}")
    print()

    while True:
        selection = input("Would you like to play another? (Y/N): ")
        print()

        if selection.lower() == 'Y'.lower():
            return True

        if selection.lower() == 'N'.lower():
            return False

def game_round_loop(players: list):
    current_deck = CARD_DECK.copy()

    while True:
        input("Press a key to draw the cards")
        print()

        for player in players:
            player['hand'] = [take_random_card(current_deck), take_random_card(current_deck)]
            
            cards = []
            for card in player['hand']:
                cards.append(display_card(card))

            print(f"{' '.join(cards)} {count_cards(player['hand'])} points.")
    
        while True:
            if has_winner(players):
                    break

            for player in players:
                if has_winner(players):
                    break

                if is_cpu(player['name']):
                    selection = rand(1, 2)

                    if selection == 1:
                        new_card = take_random_card(current_deck)
                        print(f"{player['name']} pulled a {display_card(new_card)}")
                        player['hand'].append(new_card)
                    elif selection == 2:
                        print(f"{player['name']} passed their turn.")

                    print(f"{player['name']}, now have {count_cards(player['hand'])} points")
                else:
                    print(f"{player['name']}, you currently have {count_cards(player['hand'])} points")

                    while True:
                        selection = input("Would you like to draw another card? (Y/N/Exit): ")
                        print()

                        if selection.lower() == 'Y'.lower():
                            new_card = take_random_card(current_deck)
                            print(f"You pulled a {display_card(new_card)}")
                            player['hand'].append(new_card)

                            print(f"{player['name']}, you now have {count_cards(player['hand'])} points")
                            break

                        if selection.lower() == 'N'.lower():
                            print("You passed your turn.")
                            break

                        if selection.lower() == 'Exit'.lower():
                            print("You quit the game")
                            return

                print()

        get_winner(players)
        print()
        break

def has_winner(players: list) -> bool:
    for player in players:
        if count_cards(player['hand']) == 21:
            return True
            
        if count_cards(player['hand']) > 21:
            return True

    return False

def get_winner(players: list):
    winners = []
    for player in players:
        if count_cards(player['hand']) == 21:
            winners.append(player)

        if count_cards(player['hand']) > 21:
            print(f"Player {player['name']} went over 21!")
            winners = players.copy()
            winners.remove(player)

    if len(winners) == len(players):
        print("It's a tie!")
        return

    winners[0]['score'] += 1
    print(f"Player {winners[0]['name']} is the winner!")

def display_card(card: str) -> str:
    match card:
        case 'A':
            return '🂡'
        case '2':
            return '🂢'
        case '3':
            return '🂣'
        case '4':
            return '🂤'
        case '5':
            return '🂥'
        case '6':
            return '🂦'
        case '7':
            return '🂧'
        case '8':
            return '🂨'
        case '9':
            return '🂩'
        case '10':
            return '🂪'
        case 'J':
            return '🂫'
        case 'Q':
            return '🂭'
        case 'K':
            return '🂮'
        case other:
            return ''

def display_title_screen():
    print(Terminal().home + Terminal().clear + Terminal().move_y(Terminal().height // 4))
    print(Terminal().center('Blackjack'))
    print(Terminal().black_on_gray(Terminal().center('Press any key to start the game.')))

    with Terminal().cbreak(), Terminal().hidden_cursor():
        inp = Terminal().inkey()

    print(Terminal().clear)

if __name__ == '__main__':
    main(DEFAULT_PLAYERS)