def greeting(name):
  print('Hello', name)

name1 = input('Enter your name:\n')
greeting(name1)
name2 = input('Enter your name:\n')
greeting(name2)


def addition(a,b):
  return a+b

num1 = int(input('enter your 1st number:\n'))
num2 = int(input('enter your 2nd number:\n'))

result = addition(num1,num2)
print('the result is:', result)