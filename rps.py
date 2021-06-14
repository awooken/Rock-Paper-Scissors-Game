import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
user_choice = input("Choose either 'rock' 'paper' or 'scissors'. \n")

choices = [rock, paper, scissors]
bot_choice = random.choice(choices)

if user_choice == "rock":
    print(rock)
    if bot_choice == rock:
        print(f"Bot chose: \n {bot_choice}\n It's a draw!")
    elif bot_choice == paper:
        print(f"Bot chose: \n {bot_choice}\n You lost!")
    else:
        print(f"Bot chose: \n {bot_choice}\n You won!")
elif user_choice == paper:
    print(paper)
    if bot_choice == rock:
        print(f"Bot chose: \n {bot_choice}\n You won!")
    elif bot_choice == paper:
        print(f"Bot chose: \n {bot_choice}\n It's a draw!")
    else:
        print(f"Bot chose: \n {bot_choice}\n You lost!")
elif user_choice == scissors:
    print(scissors)
    if bot_choice == rock:
        print(f"Bot chose: \n {bot_choice}\n You lost!!")
    elif bot_choice == paper:
        print(f"Bot chose: \n {bot_choice}\n You won!")
    else:
        print(f"Bot chose: \n {bot_choice}\n It's a draw!")
else:
    print("Invalid option.")
