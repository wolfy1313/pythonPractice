import requests

response = requests.get('http://api.open-notify.org/astros.json')

json = response.json()

print("da people in space rn are: ")

for person in json['people']:
  print(person['name'])