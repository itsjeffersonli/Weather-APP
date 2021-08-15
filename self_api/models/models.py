# -*- coding: utf-8 -*-
import json
import threading
from realtime.models.detector import date_converter

class show_data:
    def __init__(self):
        threading.Thread.__init__(self)
        self.file = 'apiv1.txt'

    # Current
    # Start Nested Dictionary

    def get_icon(self):
        with open(self.file, 'r') as icon:
            _data = json.loads(icon.read())
            _data_icon = _data['current']['condition']['icon']
            icon_link = "https:{0}".format(_data_icon)
            return icon_link
    
    def get_condition(self):
        with open(self.file, 'r') as condition:
            _data = json.loads(condition.read())
            _data_condition = _data['current']['condition']['text']
            return _data_condition
    
    # Stop Nested Dictionary
    def get_cloud_percent(self):
        with open(self.file, 'r') as cloud_percent:
            _data = json.loads(cloud_percent.read())
            _data_cloud_percent = _data['current']['cloud']
            return "{0}%".format(_data_cloud_percent)
            
    # Temperature
    def get_real_temp(self):
        with open(self.file, 'r') as real_temp:
            _data = json.loads(real_temp.read())
            _data_real_temp = _data['current']['temp_c']
            return u"{0}°C".format(_data_real_temp)

    def get_temperature_c(self):
        with open(self.file, 'r') as temperature_c:
            _data = json.loads(temperature_c.read())
            _data_temperature_c = _data['current']['feelslike_c']
            return "{0}°C".format(_data_temperature_c)

    def get_temperature_f(self):
        with open(self.file, 'r') as temperature_f:
            _data = json.loads(temperature_f.read())
            _data_temperature_f = _data['current']['feelslike_f']
            return "{0}°F".format(_data_temperature_f)
    # Rain
    def get_humidity(self):
        with open(self.file, 'r') as humidity:
            _data = json.loads(humidity.read())
            _data_humidity = _data['current']['humidity']
            return "{0}%".format(_data_humidity)

    def precipitation_in(self):
        with open(self.file, 'r') as precipitation:
            _data = json.loads(precipitation.read())
            _data_precipitation = _data['current']['precip_in']
            return "{0} in".format(_data_precipitation)

    def precipitation_mm(self):
        with open(self.file, 'r') as precipitation:
            _data = json.loads(precipitation.read())
            _data_precipitation_mm = _data['current']['precip_mm']
            return "{0} mm".format(_data_precipitation_mm)
    # Wind
    def wind_degree(self):
        with open(self.file, 'r') as wind_degree:
            _data = json.loads(wind_degree.read())
            _data_wind_degree = _data['current']['wind_degree']
            return "{0}°".format(_data_wind_degree)
    
    def get_gust_kph(self):
        with open(self.file, 'r') as wind_kph:
            _data = json.loads(wind_kph.read())
            _data_wind_kph = _data['current']['gust_kph']
            return "{0} kph".format(_data_wind_kph)

    def get_gust_mph(self):
        with open(self.file, 'r') as wind_mph:
            _data = json.loads(wind_mph.read())
            _data_wind_mph = _data['current']['gust_mph']
            return "{0} mph".format(_data_wind_mph)

    def get_wind_kph(self):
        with open(self.file, 'r') as wind_kph:
            _data = json.loads(wind_kph.read())
            _data_wind_kph = _data['current']['wind_kph']
            return "{0} kph".format(_data_wind_kph)

    def get_wind_mph(self):
        with open(self.file, 'r') as wind_mph:
            _data = json.loads(wind_mph.read())
            _data_wind_mph = _data['current']['wind_mph']
            return "{0} mph".format(_data_wind_mph)

    # Additional Data
    def get_pressure(self):
        with open(self.file, 'r') as pressure:
            _data = json.loads(pressure.read())
            _data_pressure_mb = _data['current']['pressure_mb']            
            return _data_pressure_mb
    
    def get_uv(self):
        with open(self.file, 'r') as uv:
            _data = json.loads(uv.read())
            _data_uv = _data['current']['uv']
            return "{0}".format(_data_uv)
    
    def vision_km(self):
        with open(self.file, 'r') as vision_km:
            _data = json.loads(vision_km.read())
            _data_vision_km = _data['current']['vis_km']
            return "{0} km".format(_data_vision_km)
    
    def vision_miles(self):
        with open(self.file, 'r') as vision_miles:
            _data = json.loads(vision_miles.read())
            _data_vision_miles = _data['current']['vis_miles']
            return "{0} miles".format(_data_vision_miles)

    # Location
    def get_location(self):
        with open(self.file, 'r') as location:
            _data = json.loads(location.read())
            _data_location = _data['location']['name']
            return _data_location

    def get_country(self):
        with open(self.file, 'r') as location:
            _data = json.loads(location.read())
            _data_country = _data['location']['country']
            return _data_country

    def full_country(self):
        with open(self.file, 'r') as location_full:
            _data = json.loads(location_full.read())
            _data_city = _data['location']['name']
            _data_country = _data['location']['country']
            return "{0}, {1}".format(_data_city, _data_country)
    
    def get_time(self):
        with open(self.file, 'r') as time:
            _data = json.loads(time.read())
            _data_time = _data['location']['localtime']
            return str(_data_time)
            
    def get_lattitude(self):
        with open(self.file, 'r') as lattitude:
            _data = json.loads(lattitude.read())
            _data_lattitude = _data['location']['lat']
            return _data_lattitude

    def get_longtitude(self):
        with open(self.file, 'r') as longtitude:
            _data = json.loads(longtitude.read())
            _data_longtitude = _data['location']['lon']
            return _data_longtitude

    def get_timezone(self):
        with open(self.file, 'r') as timezone:
            _data = json.loads(timezone.read())
            _data_timezone = _data['location']['tz_id']
            return _data_timezone
