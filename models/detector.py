import json
import time
from datetime import datetime
from pytz import timezone

# Normal Weather
clear = "/static/media/sunny.gif"
sunny = "/static/media/sunny.gif"
cloudy = "/static/media/cloudy.gif"
overcast = "/static/media/overcast.gif"
mist = "/static/media/mist.gif"
fog = "/static/media/fog.gif"
freezing_fog = "/static/media/freezing_fog.gif"

# Rain
patchy_rain = "/static/media/patchy_rain.gif"
light_rain = "/static/media/light_shower.gif"
patchy_thunder = "/static/media/patchy_thunder.gif"
moderate_rain = "/static/media/moderate_rain.gif"
heavy_rain = "/static/media/heavy_rain.gif"
torrential_rain = "/static/media/torrential_rain.gif"
storm = "/static/media/storm.gif"
thunder_outbreak = "/static/media/thunder_outbreak.gif"

# Rain part 2
patchy_drizzle = "/static/media/drizzle.gif"
drizzle = "/static/media/drizzle.gif"
freezing_drizzle = "/static/media/drizzle.gif"
heavy_drizzle = "/static/media/heavy_drizzle.gif"
light_freezing_rain = "/static/media/freezing_rain.gif"
moderate_freezing = "/static/media/freezing_rain.gif"

# Snow
patchy_snow = "/static/media/light_snow.gif"
light_snow = "/static/media/light_snow.gif"
moderate_snow = "/static/media/moderate_snow.gif"
heavy_snow = "/static/media/heavy_snow.gif"
blowing_snow = "/static/media/heavy_snow.gif"
blizzard = "/static/media/blizzard.gif"
light_snow_with_thunder = "/static/media/light_snow.gif"
heavy_snow_with_thunder = "/static/media/blizzard.gif"

# Sleet
patchy_sleet = "/static/media/light_sleet.gif"
light_sleet = "/static/media/light_sleet.gif"
moderate_sleet = "/static/media/moderate_sleet.gif"

# Hail
hail = "/static/media/hail.gif"
heavy_hail = "/static/media/hail.gif"


def check_icons():
    with open('weather.txt', 'r') as checkicons:
        _data = json.loads(checkicons.read())
        _data_icons = _data['current']['condition']['text']
        if _data_icons in ['Clear']:
            return clear
        elif _data_icons in ['Sunny']:
            return sunny
        elif _data_icons in ['Partly cloudy', 'Cloudy']:
            return cloudy
        elif _data_icons in ['Overcast']:
            return overcast
        elif _data_icons in ['Mist']:
            return mist
        elif _data_icons in ['Fog']:
            return fog
        elif _data_icons in ['Freezing Fog']:
            return freezing_fog

        # Rain
        elif _data_icons in ['Patchy rain possible']:
            return patchy_rain
        elif _data_icons in ['Light rain shower', 'Light rain', 'Patchy light rain']:
            return light_rain
        elif _data_icons in ['Patchy light rain with thunder']:
            return patchy_thunder
        elif _data_icons in ['Moderate rain at times', 'Moderate or heavy rain shower', 'Moderate rain']:
            return moderate_rain
        elif _data_icons in ['Heavy rain at times', 'Heavy rain']:
            return heavy_rain
        elif _data_icons in ['Torrential rain shower']:
            return torrential_rain
        elif _data_icons in ['Moderate or heavy rain with thunder']:
            return storm
        elif _data_icons in ['Thundery outbreaks possible']:
            return thunder_outbreak

        # Rain part 2
        elif _data_icons in ['Patchy freezing drizzle possible']:
            return patchy_drizzle
        elif _data_icons in ['Patchy light drizzle', 'Light drizzle']:
            return drizzle
        elif _data_icons in ['Freezing drizzle']:
            return freezing_drizzle
        elif _data_icons in ['Heavy freezing drizzle']:
            return heavy_drizzle
        elif _data_icons in ['Light freezing rain']:
            return light_freezing_rain
        elif _data_icons in ['Moderate or heavy freezing rain']:
            return moderate_freezing

        # Snow
        elif _data_icons in ['Patchy snow possible', 'Patchy light snow']:
            return patchy_snow
        elif _data_icons in ['Light snow', 'Light snow showers']:
            return light_snow
        elif _data_icons in ['Patchy moderate snow', 'Moderate snow']:
            return moderate_snow
        elif _data_icons in ['Moderate or heavy snow showers','Patchy heavy snow', 'Heavy snow']:
            return heavy_snow
        elif _data_icons in ['Blowing snow']:
            return blowing_snow
        elif _data_icons in ['Blizzard']:
            return blizzard
        elif _data_icons in ['Patchy light snow with thunder']:
            return light_snow_with_thunder
        elif _data_icons in ['Moderate or heavy snow with thunder']:
            return heavy_snow_with_thunder

        # Sleet
        elif _data_icons in ['Patchy sleet possible']:
            return patchy_sleet
        elif _data_icons in ['Light sleet']:
            return light_sleet
        elif _data_icons in ['Moderate or heavy sleet']:
            return moderate_sleet

        # Hail
        elif _data_icons in ['Ice pellets', 'Light sleet showers', 'Light showers of ice pellets']:
            return hail
        elif _data_icons in ['Moderate or heavy sleet showers', 'Moderate or heavy showers of ice pellets']:
            return heavy_hail

        else:
            return "https://i.imgur.com/M8VyA2h.png"


def white_black():
    white = "#FFFFFF"
    grey_color = "#696969"
    dirty_white = "#C0C0C0"
    with open('weather.txt', 'r') as checkicons:
        _data = json.loads(checkicons.read())
        _data_icons = _data['current']['condition']['text']

        if _data_icons in ['Freezing Fog', 'Blizzard']:
            return grey_color
        elif _data_icons in ['Moderate or heavy rain shower', 'Moderate rain']:
            return dirty_white
        else:
            return white


def comment():
    videvo = "Image By https://www.videvo.net/"
    gifter = "Image By https://gifer.com/"
    make_gif = "Image By https://makeagif.com/"

    with open('weather.txt', 'r') as checkicons:
        _data = json.loads(checkicons.read())
        _data_icons = _data['current']['condition']['text']

        if _data_icons in ['Clear', 'Sunny', 'Partly cloudy', 'Cloudy', 'Overcast', 'Mist', 'Fog', 'Freezing Fog',
                           'Patchy rain possible', 'Light rain shower', 'Light rain', 'Patchy light rain',
                           'Patchy light rain with thunder', 'Moderate rain at times', 'Moderate or heavy rain shower',
                           'Moderate rain', 'Heavy rain at times', 'Heavy rain', 'Torrential rain shower',
                           'Moderate or heavy rain with thunder', 'Thundery outbreaks possible',
                           'Patchy freezing drizzle possible', 'Patchy light drizzle', 'Light drizzle',
                           'Freezing drizzle']:
            videvo_final = videvo.replace('"', '', 2)

            return videvo_final

        elif _data_icons in ['Light freezing rain', 'Moderate or heavy freezing rain']:
            gifter_final = gifter.replace('"', '', 2)
            return gifter_final
        elif _data_icons in ['Ice pellets', 'Light sleet showers', 'Light showers of ice pellets',
                             'Moderate or heavy sleet showers', 'Moderate or heavy showers of ice pellets']:
            make_gif_final = make_gif.replace('"', '', 2)
            return make_gif_final
        else:
            videvo_final = videvo.replace('"', '', 2)
            return videvo_final


# noinspection PyChainedComparisons
def say_time():

    with open('weather.txt', 'r') as time_zone:
        _data = json.loads(time_zone.read())
        _data = _data['location']['tz_id']
        _format = "%H"
        now = datetime.now(timezone('UTC'))
        _get_utc_time = now.strftime(_format)
        now_timezone = now.astimezone(timezone(_data))
        final_time = now_timezone.strftime(_format)

        _time = int(final_time)
        if _time > 21 and _time < 6:
            return "Good Night"
        elif _time > 6 and _time < 12:
            return "Good Morning"
        elif _time > 12 and _time < 17:
            return "Good Afternoon"
        elif _time > 17 and _time < 21:
            return "Good Evening"
        else:
            return "Noon"