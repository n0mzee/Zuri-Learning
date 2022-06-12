import random

print("Welcome to Nomzee Rock, Paper, Scissors Game. \n Please enter R for Rock, P for Paper and S for Scissors")
possible_options = ["R","P","S"]
smallLetter = ["r", "p", "s"]
rps_dict = {"R":"Rock", "P":"Paper", "S":"Scissors"}
while True:
    user_input = input("Enter your choice: ")
    computer_action = random.choice(possible_options)
    
    if user_input in smallLetter:
        print("Choice need to be in capital letters. \n Ensure to enter R for Rock, P for Paper and S for Scissors")
        continue

    elif not user_input in possible_options:
        print("Wrong Input. Please try again. \n Ensure to enter R for Rock, P for Paper and S for Scissors")
    
        continue
        
    print(f"\nYou chose {rps_dict[user_input]}, computer chose {rps_dict[computer_action]}.\n")

    if user_input == computer_action:
            print(f"Both players selected {user_input}. It's a tie!")

    elif user_input == "R":
        if computer_action == "S":
            print("Rock smashes Scissors! You win!")
        else:
            print("Paper covers Rock! Computer wins!")
        break

    elif user_input == "P":
        if computer_action == "R":
            print("Paper covers Rock! You win!")
        else:
            print("Scissors cuts Paper! Computer wins!")
        break

    elif user_input == "S":
        if computer_action == "P":
            print("Scissors cuts Paper! You win!")
        else:
            print("Rock smashes Scissors! Computer wins!")
        break
