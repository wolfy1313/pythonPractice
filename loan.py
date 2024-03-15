#Get details of loan
money_owed = float(input("How much money do you owe, in dollars?\n"))
apr = float(input('What is the annual percentage rate of the loan?\n'))
payment = float(input('how much will you pay off each month in dollars?\n'))
months = int(input('how many months do you want to see the results for?\n'))


monthly_rate = apr/100/12

for i in range(months):
  interest_paid = money_owed*monthly_rate
  money_owed = money_owed + interest_paid

  if (money_owed - payment <0):
    print('the last payment is', money_owed)
    print('you paid of the loan in', (i+1), 'months')
    break

  money_owed = money_owed - payment
  
  print('paid', payment, 'of which', round(interest_paid, 2), 'was interest', end=" ")
  print('now you owe', round(money_owed, 2))