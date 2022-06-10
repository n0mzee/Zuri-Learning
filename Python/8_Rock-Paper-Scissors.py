import random

def circleBack():
    while True:
        user_input = input("Enter your choice: ")
        if user_input in smallLetter:
            print("Choice need to be in capital letters. \n Ensure to enter R for Rock, P for Paper and S for Scissors")
            continue

        elif not user_input in possible_options:
            print("Wrong Input. Please try again. \n Ensure to enter R for Rock, P for Paper and S for Scissors")
        
            continue
    
        else:
            computer_action = random.choice(possible_options)
            print(f"\nYou chose {user_input}, computer chose {computer_action}.\n")
            #Correct input found.
            
            return (user_input)


print("Welcome to Nomzee Rock, Paper, Scissors Game. \n Please enter R for Rock, P for Paper and S for Scissors")
possible_options = ["R","P","S"]
smallLetter = ["r", "p", "s"]
while True:
    user_input = input("Enter your choice: ")
    if user_input in smallLetter:
        print("Choice need to be in capital letters. \n Ensure to enter R for Rock, P for Paper and S for Scissors")
        continue

    elif not user_input in possible_options:
        print("Wrong Input. Please try again. \n Ensure to enter R for Rock, P for Paper and S for Scissors")
    
        continue
    
    else:
        #Correct input found.
        break

computer_action = random.choice(possible_options)
print(f"\nYou chose {user_input}, computer chose {computer_action}.\n")

if user_input == computer_action:
        print(f"Both players selected {user_input}. It's a tie!")
        circleBack()

if user_input == "R":
    if computer_action == "S":
        print("Rock smashes Scissors! You win!")
    else:
        print("Paper covers Rock! Computer wins!")
elif user_input == "P":
    if computer_action == "R":
        print("Paper covers Rock! You win!")
    else:
        print("Scissors cuts Paper! Computer wins!")
elif user_input == "S":
    if computer_action == "P":
        print("Scissors cuts Paper! You win!")
    else:
        print("Rock smashes Scissors! Computer wins!")