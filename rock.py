import random

print("\nWelcome to Rock, Paper, Scissors game. Type 0 for Rock, 1 for Paper, 2 for Scissors")

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
game_img = [rock,paper,scissors]
user_input = int(input()) #Enter 0 or 1 or 2
print(f"\nYou chose {user_input}")
print(game_img[user_input])

num = random.randint(0,2)
print(f"\nComputer chooses {num}")
print(game_img[num])

if user_input == 0 and num == 2:
    print("\nRock beats Scissors. You win.")
elif user_input == 0 and num == 0:
    print("\nYou lose")
elif user_input == 0 and num == 1:
    print("\nYou lose")
elif user_input == num:
    print("\nIts a draw")


if user_input == 1 and num == 0:
    print("\nPaper holds rock. You win.")
elif user_input == 1 and num == 1:
    print("\nYou lose")
elif user_input == 1 and num == 2:
    print("\nYou lose")   

if user_input == 2 and num == 1:
    print("\nScissor cuts paper you win.") 
elif user_input == 2 and num == 0:
    print("\nYou lose")
elif user_input == 2 and num == 2:
    print("\nYou lose")
    