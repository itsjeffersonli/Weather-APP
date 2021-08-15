import json
import random
import threading
from realtime.models.detector import date_converter

class gather_data:
    def __init__(self):
        self.file = 'weather.txt'
        threading.Thread.__init__(self)

    def get_icon(self):
        with open(self.file, 'r') as icon:
            _data = json.loads(icon.read())
            _data_icon = _data['current']['condition']['icon']
            icon_link = "https:{0}".format(_data_icon)
            return icon_link


    # Sunny Cloudy Something like that
    def get_condition(self):
        with open(self.file, 'r') as condition:
            _data = json.loads(condition.read())
            _data_condition = _data['current']['condition']['text']

            return _data_condition


    def get_condition_percent(self):
        with open(self.file, 'r') as condition_percent:
            _data = json.loads(condition_percent.read())
            _data_condition_percent = _data['current']['cloud']

            return _data_condition_percent


    def get_temperature(self):
        with open(self.file, 'r') as temperature:
            _data = json.loads(temperature.read())
            _data_temperature = _data['current']['temp_c']
            _data_temperature = str(_data_temperature)
            return _data_temperature


    def get_wind_direction(self):
        with open(self.file, 'r') as windir:
            _data = json.loads(windir.read())
            _data_windir = _data['current']['wind_dir']

            return _data_windir


    def get_rain(self):
        with open(self.file, 'r') as rain:
            _data = json.loads(rain.read())
            _data_rain = _data['current']['precip_mm']
            _rain_ = "{0} mm".format(_data_rain)
            return _rain_


    def get_humidity(self):
        with open(self.file, 'r') as humidity:
            _data = json.loads(humidity.read())
            _data_humidity = _data['current']['humidity']

            return _data_humidity


    def get_city(self):
        with open(self.file, 'r') as city:
            _data = json.loads(city.read())
            _city = _data['location']['name']
            _country = _data['location']['country']

            _data_combine = "{0}, {1}".format(_city, _country)

            return _data_combine


    def get_date(self):
        with open(self.file, 'r') as date:
            _data = json.loads(date.read())
            _date = _data['location']['tz_id']

            date_convert = date_converter(_date)

        return date_convert

def random_country():
    _get_random_country = open('data/country.txt').read().splitlines()
    _get_random_country = random.choice(_get_random_country)

    return _get_random_country
