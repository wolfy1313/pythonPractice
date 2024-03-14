import random

roll = random.randint(1,6)

# print ("the computer rolled a " + str(roll))

guess = int(input('Guess the dice roll:\n'))

if guess == roll:
  print('you right they rolled a ' + str(roll))
else:
  print('nope, the computer rolled a ' + str(roll))