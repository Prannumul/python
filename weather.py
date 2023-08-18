import requests
city=input('please enter city: ')
weather_url = "http://api.weatherapi.com/v1/current.json?key=f7c0420dab204bc0a20213419230807&q={0}&aqi=no".format(city)
response = requests.get(weather_url)
weather_json = response.json()

temp = weather_json.get('current').get('temp_f')
desc = weather_json.get('current').get('condition').get('text')

print("Todays weather in "+ city + " is " + desc + " and temperature is " + str(temp))
#print(weather_json)
