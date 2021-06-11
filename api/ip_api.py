import requests
import json

api = "02366002f1704fa8aa692640210706"


def ip_weather_locate():
    request_url = "http://api.weatherapi.com/v1/ip.json?key={0}&q=auto:ip".format(api)
    response = json.loads(requests.get(request_url).text)
    response_city = response['city']
    response_country = response['country_name']

    new_response = "{0}, {1}".format(response_city, response_country)

    return new_response
