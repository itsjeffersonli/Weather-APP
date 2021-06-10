import requests


def get_ip():
    ip = requests.get('https://api.ipify.org/').text

    return ip
