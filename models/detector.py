import json, time


def check_icons():
    sunny = "/static/media/sunny.gif"
    cloudy = "/static/media/cloudy.gif"
    storm = "/static/media/storm.gif"
    rain = "/static/media/rain.gif"
    clear = ""
    light_rain = "/static/media/light_shower.gif"
    with open('weather.txt', 'r') as checkicons:
        _data = json.loads(checkicons.read())
        _data_icons = _data['current']['condition']['text']
        if _data_icons in ['Partly cloudy', 'Cloudy']:
            return cloudy
        elif _data_icons in ['Sunny']:
            return sunny
        elif _data_icons in ['Storm']:
            return storm
        elif _data_icons in ['Rain']:
            return rain
        elif _data_icons in ['Clear']:
            return clear
        elif _data_icons in ['Light rain shower']:
            return light_rain
        else:
            return "https://i.imgur.com/M8VyA2h.png"


def check_day_night():
    sunrise = ""
    day = "/static/media/no_search/day.gif"
    night = "/static/media/no_search/night.gif"

    mytime = time.localtime()

    if 4 < mytime.tm_hour < 6:
        return sunrise
    elif 6 < mytime.tm_hour < 18:
        return day
    else:
        return night
