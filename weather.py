import requests

API_KEY = "38611f50f48033c6d4ab8f604c92cbed"

endpoint = "https://api.openweathermap.org/data/2.5/weather" # from https://openweathermap.org/current
payload = {"q": "London,UK", "units": "metric",  "appid": API_KEY}

response = requests.get(endpoint, params=payload)

print response.url
print response.status_code
#print (response.headers[]

data = response.json()
temperature = data["main"]["temp"]
name = data["name"]
weather = data ["weather"][0]["main"]
print "It's {} in {}, with {} degrees celsius".format(weather, name, temperature )

if temperature <= 10:
    print("Wear a coat!")
else:
    print("What a nice day :)")
