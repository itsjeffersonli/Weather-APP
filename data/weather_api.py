import requests, json

api = "02366002f1704fa8aa692640210706"


def get_weather(city):
    city = str(city)
    url = "http://api.weatherapi.com/v1/current.json?key={0}&q={1}".format(api, city)
    response = requests.get(url)
    _data = response.json()
    with open('weather.txt', 'w+') as weather:
        json.dump(_data, weather, indent=4, sort_keys=True)

