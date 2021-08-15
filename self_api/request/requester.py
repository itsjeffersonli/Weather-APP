import requests
import json

key = "02366002f1704fa8aa692640210706"

def generate_data(city):
    city = str(city)
    url = "https://api.weatherapi.com/v1/current.json?key={0}&q={1}".format(key, city)
    response = requests.get(url)
    _data = response.json()
    with open('apiv1.txt', 'w+') as weather:
        json.dump(_data, weather, indent=4, sort_keys=True)