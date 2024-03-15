acronyms = {
  'LOL': 'laugh out loud',
  'IDK': "I don't know",
  'TBH': "To be honest"
}

acronyms['BF'] = 'buttfucker'

print(acronyms)

# acronyms['TBH'] = 'honestly'

print(acronyms)

sentence = 'IDK' + ' what happened ' + 'TBH'
translation = acronyms.get('IDK') + ' what happened ' + acronyms.get('TBH')
print(sentence, translation)