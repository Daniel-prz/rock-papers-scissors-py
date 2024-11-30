import random
print('Welcome to Rock Paper Scissors !')
user_choice = int(input("Type '0' for Rock, '1' for Scissors, or '2' for Paper\n"))
computer_input = random.randint(0,2)
choice_list = ['Rock', 'Scissors', 'Paper']
print(f'You chose {choice_list[user_choice]}')
print((f"Computer chose {choice_list[computer_input]}"))
if user_choice == 0 and computer_input == 0:
    print("Rock vs Rock, No winner.")
elif user_choice == 0 and computer_input == 1:
    print("Rock beats Scissors, You Win !")
elif user_choice == 0 and computer_input == 2:
    print("Rock gets beat by Paper, You Lose.")
if user_choice == 1 and computer_input == 0:
    print("Scissors gets beat by Rock, You Lose.")
elif user_choice == 1 and computer_input == 1:
    print("Scissors vs Scissors, No winner.")
elif user_choice == 1 and computer_input == 2:
    print("Scissors beats Paper, You Win ! ")
if user_choice == 2 and computer_input == 0:
    print("Paper beats Rock, You Win ! ")
elif user_choice == 2 and computer_input == 1:
    print("Paper gets beat by Scissors, You Lose.")
elif user_choice == 2 and computer_input == 2:
    print("Paper vs Paper, No winner.")