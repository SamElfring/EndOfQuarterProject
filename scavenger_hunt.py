def print_game_rules():
    print(
"""\nThe rules are simple, we've scattered several objects around Enschede.
Every object has a code on it, which you'll have to add to the list.
When you've added every code to the list you're able to guess the password.
The team that guesses the password first wins the game.""") #condition: you need to find all 4 objects to guess the password
    return

def guess_password(object_codes_list):
    print("""
Congratulations on making it this far!
You've entered every code and now you have to guess the password.
Read carefully!

You can create the password by combining every code you've entered.
The password is a sentence and the spaces are replaced by underscores('_').""")

    while True:
        password_input = input("Enter the password: ")
        if password_input == "Welcome_to_SD42!": #in module?
            victory()
            exit()
        else:
            print(f"Your guess is incorrect! \nPlease try again! \nReminder: {object_codes_list}")


def victory():
    print("Victory!")

def scavenger_hunt_main():
    print("Welcome to the scavenger hunt!")
    print_game_rules()

    object_codes_list = []
    while True:
        #print rules
        #add code to list
        #print obtained codes
        #Guess the password
        try:
            menu_input = int(input("""
1. Show rules again
2. Add code to the list
3. Show obtained codes
4. Attempt to guess the password
Please select an option: """))
        
        except:
            print("Enter a valid input")
        
        if menu_input == 1:
            print_game_rules()

        elif menu_input == 2:
            #Have it so you can only add the precise codes
            while True:
                add_code = input("\nEnter the code written on the item you've hunted (enter 'exit' to return to the menu): ")

                if add_code.lower() == "exit":
                    break

                if add_code ==  "o_S" or add_code == "ome_t" or add_code == "Welc" or add_code == "D42!": #in een module?
                    if add_code in object_codes_list:
                        print("\nThe code has already been added to the list!")
                        pass
                    object_codes_list.append(add_code)
                    print_obtained_codes = print(f"\nThese are the codes you've obtained so far: {object_codes_list}")
                    
                    if len(object_codes_list) == 4:
                        print("\nCongratulations, you've obtained and entered every code to the list, you are now able to guess the password!")
                        break

                    add_code_again = input("Do you want to enter another code? [y/n] ")
                    
                    if add_code_again.lower() == "y":
                        continue
                    elif add_code_again.lower() == "n":
                        break
                    else:
                        print("Please enter a valid input!")
                else:
                    print("\nPlease correctly enter the code written on the object!")

        elif menu_input == 3:
            oprint_obtained_codes = print(f"These are the codes you've obtained so far: {object_codes_list}")
            if len(object_codes_list) == 4:
                print("\nCongratulations, you've obtained and entered every code to the list, you are now able to guess the password!")
        
        elif menu_input == 4:
            if len(object_codes_list) == 4:
                guess_password(object_codes_list)
            else:
                print("\nThe list isn't complete yet, please add all the codes to the list!")
scavenger_hunt_main()