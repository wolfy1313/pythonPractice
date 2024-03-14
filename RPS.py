import random

computerChoice = random.choice(['rock', 'paper', 'scissors'])

userChoice = input("Do you want rock, paper, or scissors?")

if computerChoice == userChoice:
  print('TIE')
elif userChoice == 'rock' and computerChoice == 'scissors':
  print('WIN'+ str(computerChoice))
elif userChoice == 'paper' and computerChoice == 'rock':
  print('WIN'+ str(computerChoice))
elif userChoice == 'scissors' and computerChoice == 'paper':
  print('WIN'+ str(computerChoice))
else:
  print("you lose you loser, the computer rolled a " + str(computerChoice))