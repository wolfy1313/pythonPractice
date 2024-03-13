acronyms = ['lol', 'idk', 'tbh']

acronyms.append('smh')

print(acronyms)

acronyms.append('ijs')

print(acronyms)
lol = 'lol'
if lol in acronyms:
  print('yes, ' + lol + ' is in there')
else:
  print('nah ' + lol + 'aint there')

acronyms.remove('lol')

print('removed one ' + str(acronyms))
del acronyms[2]
print('removed index 2 ' + str(acronyms))
if lol in acronyms:
  print('yes, ' + lol + ' is in there')
else:
  print('nah ' + lol + ' aint there')

  for i in acronyms:
    print(i)