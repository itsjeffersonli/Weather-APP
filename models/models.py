import json
from datetime import datetime
from pytz import timezone


def date_converter(_timezone):
    _timezone = str(_timezone)
    format = "%H:%M - %m/%d/%Y"
    now = datetime.now(timezone('UTC'))
    _get_utc_time = now.strftime(format)

    now_timezone = now.astimezone(timezone(_timezone))
    final_date = now_timezone.strftime(format)

    return final_date


def get_icon():
    with open('weather.txt', 'r') as icon:
        _data = json.loads(icon.read())
        _data_icon = _data['current']['condition']['icon']
        icon_link = "https:{0}".format(_data_icon)
        return icon_link


# Sunny Cloudy Something like that
def get_condition():
    with open('weather.txt', 'r') as condition:
        _data = json.loads(condition.read())
        _data_condition = _data['current']['condition']['text']

        return _data_condition


def get_condition_percent():
    with open('weather.txt', 'r') as condition_percent:
        _data = json.loads(condition_percent.read())
        _data_condition_percent = _data['current']['cloud']

        return _data_condition_percent


def get_temperature():
    with open('weather.txt', 'r') as temperature:
        _data = json.loads(temperature.read())
        _data_temperature = _data['current']['temp_c']
        _data_temperature = str(_data_temperature)
        return _data_temperature


def get_wind_direction():
    with open('weather.txt', 'r') as windir:
        _data = json.loads(windir.read())
        _data_windir = _data['current']['wind_dir']

        return _data_windir


def get_rain():
    with open('weather.txt', 'r') as rain:
        _data = json.loads(rain.read())
        _data_rain = _data['current']['precip_mm']
        _rain_ = "{0} mm".format(_data_rain)
        return _rain_


def get_humidity():
    with open('weather.txt', 'r') as humidity:
        _data = json.loads(humidity.read())
        _data_humidity = _data['current']['humidity']

        return _data_humidity


def get_city():
    with open('weather.txt', 'r') as city:
        _data = json.loads(city.read())
        _city = _data['location']['name']
        _country = _data['location']['country']

        _data_combine = "{0}, {1}".format(_city, _country)

        return _data_combine


def get_date():
    with open('weather.txt', 'r') as date:
        _data = json.loads(date.read())
        _date = _data['location']['tz_id']

        date_convert = date_converter(_date)

        return date_convert
