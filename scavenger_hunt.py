import scavenger_hunt_answers as sha
import os
import subprocess


sh_title ="""
 _____                                             _   _             _   
/  ___|                                           | | | |           | |  
\ `--.  ___ __ ___   _____ _ __   __ _  ___ _ __  | |_| |_   _ _ __ | |_ 
 `--. \/ __/ _` \ \ / / _ \ '_ \ / _` |/ _ \ '__| |  _  | | | | '_ \| __|
/\__/ / (_| (_| |\ V /  __/ | | | (_| |  __/ |    | | | | |_| | | | | |_ 
\____/ \___\__,_| \_/ \___|_| |_|\__, |\___|_|    \_| |_/\__,_|_| |_|\__|
                                  __/ |                                  
                                 |___/                                   
"""

def print_game_rules():
    print(
"""\nThe rules are simple, we've scattered several objects around Enschede.
Every object has a code on it, which you'll have to add to the list.
When you've added every code to the list you're able to guess the password.
The team that guesses the password first wins the game.""")
    return

def guess_password(object_codes_list):
    attempts = 3
    print("""
Congratulations on making it this far!
You've entered every code and now you have to guess the password.

You can create the password by combining every code you've entered in a logical order.
You have 3 attempts, if you've failed all attempts, your list will be cleared.""")

    while True:
        password_input = input("Enter the password: ")
        if password_input == sha.t1_password_input or password_input == sha.t2_password_input:
            victory()
            exit()
        else:
            print(f"\nYour guess is incorrect, {attempts -1} attempt(s) left ")
            if attempts > 0:
                print(f"\nReminder: {object_codes_list}")

            attempts -= 1
            if attempts == 0:
                print("""
Too many failed attempts, your list will be cleared now.

IT'S THE OPPOSING TEAM'S TURN NOW! (if they're present)""")
                attempts = 3
                failed_attempt = 1
                return failed_attempt
                

def victory():
    print("Victory!")
    #TODO add 1 point to the winning team




def scavenger_hunt_main(team1, team2):
    subprocess.Popen(
    ['xdg-open', "SH_Locations.png"],
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL)
    print(sh_title)
    print("Welcome to the scavenger hunt!")
    print_game_rules()

    t1_object_codes_list = []
    t2_object_codes_list = []

    while True:
        try:
            menu_input = int(input("""
1. Show rules again
2. Open image again
3. [Team 1] Add code to the list
4. [Team 1] Show obtained codes
5. [Team 2] Add code to the list
6. [Team 2] Show obtained codes
7. Attempt to guess the password
Please select an option: """))
        
        except:
            print("Enter a valid input")
        
        if menu_input == 1:
            print_game_rules()

        elif menu_input == 2:
            subprocess.Popen(
            ['xdg-open', "SH_Locations.png"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL)

        elif menu_input == 3:
            t1_add_code_attempts = 3

            while True:
                t1_add_code = input("""
Enter the code written on the item you've hunted [case sensitive]
(enter 'exit' to return to the menu): """)

                if t1_add_code.lower() == "exit":
                    break

                if t1_add_code ==  sha.t1_add_code_1 or t1_add_code == sha.t1_add_code_2 or t1_add_code == sha.t1_add_code_3 or t1_add_code == sha.t1_add_code_4:
                    if t1_add_code in t1_object_codes_list:
                        print(f"\nThe code has already been added to the list!\n{t1_add_code_attempts-1} attempt(s) left!")
                        t1_add_code_attempts -= 1
                        if t1_add_code_attempts == 0:
                            print("""
Too many failed attempts.

IT'S THE OPPOSING TEAM'S TURN NOW! (if they're present)""")
                            t1_add_code_attempts = 3
                            break
                        continue
                    t1_object_codes_list.append(t1_add_code)
                    print_obtained_codes = print(f"\nThese are the codes you've obtained so far: {t1_object_codes_list}")
                    
                    if len(t1_object_codes_list) == 4:
                        print("\nCongratulations Team 1, you've obtained and entered every code to the list, you are now able to guess the password!")
                        break

                else:
                    print(f"""
\nPlease correctly enter the code written on the object! [case sensitive]
{t1_add_code_attempts-1} attempt(s) left!""")
                    t1_add_code_attempts -= 1
                    if t1_add_code_attempts == 0:
                        print("""
Too many failed attempts.

IT'S THE OPPOSING TEAM'S TURN NOW! (if they're present)""")
                        t1_add_code_attempts = 3
                        break

        elif menu_input == 4:
            print_obtained_codes = print(f"These are the codes you've obtained so far: {t1_object_codes_list}")
            if len(t1_object_codes_list) == 4:
                print("\nCongratulations Team 1, you've obtained and entered every code to the list, you are now able to guess the password!")
        
        elif menu_input == 5:
            t2_add_code_attempts = 3

            while True:
                t2_add_code = input("""
Enter the code written on the item you've hunted [case sensitive]
(enter 'exit' to return to the menu): """)

                if t2_add_code.lower() == "exit":
                    break

                if t2_add_code ==  sha.t2_add_code_1 or t2_add_code == sha.t2_add_code_2 or t2_add_code == sha.t2_add_code_3 or t2_add_code == sha.t2_add_code_4:
                    if t2_add_code in t2_object_codes_list:
                        print(f"\nThe code has already been added to the list!\n{t2_add_code_attempts-1} attempt(s) left!")
                        t2_add_code_attempts -= 1
                        if t2_add_code_attempts == 0:
                            print("""
Too many failed attempts.

IT'S THE OPPOSING TEAM'S TURN NOW! (if they're present)""")
                            t2_add_code_attempts = 3
                            break
                        continue
                    t2_object_codes_list.append(t2_add_code)
                    print_obtained_codes = print(f"\nThese are the codes you've obtained so far: {t2_object_codes_list}")
                    
                    if len(t2_object_codes_list) == 4:
                        print("\nCongratulations Team 2, you've obtained and entered every code to the list, you are now able to guess the password!")
                        break

                else:
                    print(f"""
\nPlease correctly enter the code written on the object! [case sensitive]
{t2_add_code_attempts-1} attempt(s) left!""")
                    t2_add_code_attempts -= 1
                    if t2_add_code_attempts == 0:
                        print("""
Too many failed attempts.

IT'S THE OPPOSING TEAM'S TURN NOW! (if they're present)""")
                        t2_add_code_attempts = 3
                        break

        elif menu_input == 6:
            print_obtained_codes = print(f"These are the codes you've obtained so far: {t2_object_codes_list}")
            if len(t2_object_codes_list) == 4:
                print("\nCongratulations Team 2, you've obtained and entered every code to the list, you are now able to guess the password!")

        elif menu_input == 7:
            if len(t1_object_codes_list) == 4:
                t1_attempt = guess_password(t1_object_codes_list)
                if t1_attempt == 1:
                    t1_object_codes_list.clear()
                    t1_attempt = 0
            elif len(t2_object_codes_list) == 4:
                t2_attempt = guess_password(t2_object_codes_list)
                if t2_attempt == 1:
                    t2_object_codes_list.clear()
                    t2_attempt = 0
            else:
                print("\nNone of the lists are complete yet, please add all the codes to your team's list!")