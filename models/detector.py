import json, time

clear = ""
sunny = "/static/media/sunny.gif"
cloudy = "/static/media/cloudy.gif"
overcast = ""
mist = ""
fog = ""
freezing_fog = ""

# Rain
patchy_rain = ""
light_rain = "/static/media/light_shower.gif"
patchy_thunder = ""
moderate_rain = "/static/media/moderate.gif"
heavy_rain = ""
torrential_rain = ""
storm = "/static/media/storm.gif"
thunder_outbreak = ""

# Rain part 2
patchy_drizzle = ""
drizzle = ""
freezing_drizzle = ""
heavy_drizzle = ""
light_freezing_rain = ""
moderate_freezing = ""

# Snow
patchy_snow = ""
light_snow = ""
moderate_snow = ""
heavy_snow = ""
blowing_snow = ""
blizzard = ""
light_snow_with_thunder = ""
heavy_snow_with_thunder = ""

# Sleet
patchy_sleet = ""
light_sleet = ""
moderate_sleet = ""

# Hail
hail = ""
heavy_hail = ""


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
        elif _data_icons in ["Patchy rain possible"]:
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
