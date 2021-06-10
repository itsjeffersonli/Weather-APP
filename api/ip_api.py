import requests
import json


def ip_weather_locate(ip):
    ip = str(ip)
    request_url = "http://ip-api.com/json/{0}".format(ip)
    response = json.loads(requests.get(request_url).text)
    response_city = response['city']
    response_country = response['country']

    new_response = "{0}, {1}".format(response_city, response_country)

    return new_response

