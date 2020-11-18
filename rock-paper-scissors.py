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

images = [rock, paper, scissors]

print("Let's have a game of Rock, Paper, Scissors!")

user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer = random.randint(0, 2)

if user > 2 or user < 0:
  print("You typed an invalid number, you lose!")
  exit(0)
else:
  print("You chose:")
  print(images[user])
  print("Computer chose:")
  print(images[computer])

# if user > 2 or user < 0:
  # print("")
if user == 0 and computer == 2:
  print("You win!")
elif computer == 0 and user == 2:
  print("You lose!")
elif computer > user:
  print("You lose!")
elif user > computer:
  print("You win!")
elif computer == user:
  print("It's a draw")