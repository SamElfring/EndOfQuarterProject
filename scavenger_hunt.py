import scavenger_hunt_answers as sha

def print_game_rules():
    print(
"""\nThe rules are simple, we've scattered several objects around Enschede.
Every object has a code on it, which you'll have to add to the list.
When you've added every code to the list you're able to guess the password.
The team that guesses the password first wins the game.""")
    return

def guess_password(object_codes_list):
    print("""
Congratulations on making it this far!
You've entered every code and now you have to guess the password.

You can create the password by combining every code you've entered in a logical order""")

    while True:
        password_input = input("Enter the password: ")
        if password_input == sha.t1_password_input or password_input == sha.t2_password_input:
            victory()
            exit()
        else:
            print(f"Your guess is incorrect, please try again! \n\nReminder: {object_codes_list}")


def victory():
    print("Victory!")
    #add 1 point to the winning team

def scavenger_hunt_main():
    print("Welcome to the scavenger hunt!")
    print_game_rules()

    t1_object_codes_list = []
    t2_object_codes_list = []
    while True:
        try:
            menu_input = int(input("""
1. Show rules again
2. [Team 1] Add code to the list
3. [Team 1] Show obtained codes
4. [Team 2] Add code to the list
5. [Team 2] Show obtained codes
6. Attempt to guess the password
Please select an option: """))
        
        except:
            print("Enter a valid input")
        
        if menu_input == 1:
            print_game_rules()

        elif menu_input == 2:
            while True:
                t1_add_code = input("\nEnter the code written on the item you've hunted (enter 'exit' to return to the menu): ")

                if t1_add_code.lower() == "exit":
                    break

                if t1_add_code ==  sha.t1_add_code_1 or t1_add_code == sha.t1_add_code_2 or t1_add_code == sha.t1_add_code_3 or t1_add_code == sha.t1_add_code_4:
                    if t1_add_code in t1_object_codes_list:
                        print("\nThe code has already been added to the list!")
                        pass
                    t1_object_codes_list.append(t1_add_code)
                    print_obtained_codes = print(f"\nThese are the codes you've obtained so far: {t1_object_codes_list}")
                    
                    if len(t1_object_codes_list) == 4:
                        print("\nCongratulations Team 1, you've obtained and entered every code to the list, you are now able to guess the password!")
                        break

                else:
                    print("\nPlease correctly enter the code written on the object! (case sensitive)")

        elif menu_input == 3:
            oprint_obtained_codes = print(f"These are the codes you've obtained so far: {t1_object_codes_list}")
            if len(t1_object_codes_list) == 4:
                print("\nCongratulations Team 1, you've obtained and entered every code to the list, you are now able to guess the password!")
        
        elif menu_input == 4:
            while True:
                t2_add_code = input("\nEnter the code written on the item you've hunted (enter 'exit' to return to the menu): ")

                if t2_add_code.lower() == "exit":
                    break

                if t2_add_code ==  sha.t2_add_code_1 or t2_add_code == sha.t2_add_code_2 or t2_add_code == sha.t2_add_code_3 or t2_add_code == sha.t2_add_code_4:
                    if t2_add_code in t2_object_codes_list:
                        print("\nThe code has already been added to the list!")
                        pass
                    t2_object_codes_list.append(t2_add_code)
                    print_obtained_codes = print(f"\nThese are the codes you've obtained so far: {t2_object_codes_list}")
                    
                    if len(t2_object_codes_list) == 4:
                        print("\nCongratulations Team 2, you've obtained and entered every code to the list, you are now able to guess the password!")
                        break

                else:
                    print("\nPlease correctly enter the code written on the object! (case sensitive)")

        elif menu_input == 5:
            oprint_obtained_codes = print(f"These are the codes you've obtained so far: {t2_object_codes_list}")
            if len(t2_object_codes_list) == 4:
                print("\nCongratulations Team 2, you've obtained and entered every code to the list, you are now able to guess the password!")

        elif menu_input == 6:
            if len(t1_object_codes_list) == 4:
                guess_password(t1_object_codes_list)
            elif len(t2_object_codes_list) == 4:
                guess_password(t2_object_codes_list)
            else:
                print("\nNone of the lists are complete yet, please add all the codes to your team's list!")
scavenger_hunt_main()