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

choice = int(input("What do you want to choose? 0 for Rock, 1 for Paper, 2 for Scissors "))
options = [rock, paper, scissors]
comp = random.randint(0,2)

if choice == comp:
  print(f"You chose {options[choice]} \n Computer chose {options[comp]} \n YOU TIEDDDD!")
elif (choice == 0 and comp == 2) or (choice == 1 and comp == 0) or (choice == 2 and comp == 1):
  print(f"You chose {options[choice]} \n Computer chose {options[comp]} \n YOU WIN!")
elif (choice == 2 and comp == 0) or (choice == 0 and comp == 1) or (choice == 1 and comp == 2):
  print(f"You chose {options[choice]} \n Computer chose {options[comp]} \n YOU LOSE!")
else:
  print("That wasn't an option, you lose!")
