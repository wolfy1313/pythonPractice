computerChoice = "scissors"

userChoice = input("Do you want rock, paper, or scissors?")

if computerChoice == userChoice:
  print('TIE')
elif userChoice == 'rock' and computerChoice == 'scissors':
  print('WIN')
elif userChoice == 'paper' and computerChoice == 'rock':
  print('WIN')
elif userChoice == 'scissors' and computerChoice == 'paper':
  print('WIN')
else:
  print("you lose you loser")