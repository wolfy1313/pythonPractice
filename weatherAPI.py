import requests

city = 'London'

url = 'http://api.weatherapi.com/v1/current.json?key=d1fc8702867944bbbc4213006242603&q='+city+'&aqi=no'

response = requests.get(url)

weather_json = response.json()

temp = weather_json.get('current').get('temp_f')
condition = weather_json.get('current').get('condition').get('text')
location = weather_json.get('location').get('name')

print("Today's weather in", city, "is", condition.lower(), "and", temp, "degrees.")

# for temp, condition in weather_json['current']:
#   print(temp['temp_f'], condition['condition'] )