expenses = []

total = 0

for i in range(7):
  expenses.append(float(input("Enter an expense: ")))
  
print("you spent $", total, sep = "")