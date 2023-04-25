from blessed import Terminal
import rockpaperscissors
import blackjack
import tictactoe

# Hangman & Quiz game were removed because they were not finished in time to work.

menu = [
    {
        'title': 'Blackjack',
        'module': blackjack
    },
    {
        'title': 'Rock Paper Scissors',
        'module': rockpaperscissors
    },
    {
        'title': 'Tic Tac Toe',
        'module': tictactoe
    },
    {
        'title': 'Exit'
    }
]

Players = [
    {
        'name': 'Player',
        'score': 0
    },
    {
        'name': 'CPU',
        'score': 0
    }
]


def display_screen(selection):
    term = Terminal()
    print(term.home + term.clear)
    print(term.center("""
 __   __  __   __  ___    _______  ___  _______  _______  __   __  _______ 
|  |_|  ||  | |  ||   |  |       ||   ||       ||   _   ||  |_|  ||       |
|       ||  | |  ||   |  |_     _||   ||    ___||  |_|  ||       ||    ___|
|       ||  |_|  ||   |    |   |  |   ||   | __ |       ||       ||   |___ 
|       ||       ||   |___ |   |  |   ||   ||  ||       ||       ||    ___|
| ||_|| ||       ||       ||   |  |   ||   |_| ||   _   || ||_|| ||   |___ 
|_|   |_||_______||_______||___|  |___||_______||__| |__||_|   |_||_______|




    """))

    for (idx, m) in enumerate(menu):
        if idx == selection:
            print(term.bold_gray_reverse(term.center(f"{m['title']}")))
        else:
            print(term.normal + term.center(f"{m['title']}"))


def run_selection(selection):
    # print(term.green_reverse(term.center(menu[selection]['title'])))
    if menu[selection]['title'].lower() == 'exit':
        print(term.clear())
        exit()
    print(term.clear())
    menu[selection]['module'].main(Players)


if __name__ == '__main__':
    term = Terminal()
    while True:
        with term.fullscreen(), term.hidden_cursor():
            selection = 0
            display_screen(selection)
            selection_inprogress = True
            with term.cbreak():
                while selection_inprogress:
                    key = term.inkey()
                    if key.is_sequence:
                        if key.name == 'KEY_TAB':
                            selection += 1
                        if key.name == 'KEY_DOWN':
                            selection += 1
                        if key.name == 'KEY_UP':
                            selection -= 1
                        if key.name == 'KEY_ENTER':
                            selection_inprogress = False
                    elif key:
                        print("got {0}.".format(key))

                    selection = selection % len(menu)

                    display_screen(selection)
        run_selection(selection)