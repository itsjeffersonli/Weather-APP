from self_api.models.models import *


result = show_data()

def ret_data():
    data = {
        'current_weather' : {
            'condition' : {
                'icon' : result.get_icon(),
                'cloud_percentage' : result.get_cloud_percent(),
                'weather_condition' : result.get_condition()
            },
            'temperature' : {
                'real_temp' : result.get_real_temp(),
                'temp_c' : result.get_temperature_c(),
                'temp_f' : result.get_temperature_f()
            },
            'rain' : {
                'humidity' : result.get_humidity(),
                'precipitation_in' : result.precipitation_in(),
                'precipitation_mm' : result.precipitation_mm()
            },
            'wind' : {
                'wind_degree' : result.wind_degree(),
                'gust_kph' : result.get_gust_kph(),
                'gust_mph' : result.get_gust_mph(),
                'wind_kph' : result.get_wind_kph(),
                'wind_mph' : result.get_wind_mph()
            },
            'additionals' : {
                'pressure' : result.get_pressure(),
                'uv' : result.get_uv(),
                'visibility_km' : result.vision_km(),
                'visibility_mi' : result.vision_miles()
            }
        },
        'location' : {
            'city' : result.get_location(),
            'country' : result.get_country(),
            'complete_c_c' : result.full_country(),
            'latitude' : result.get_lattitude(),
            'longitude' : result.get_longtitude(),
            'time' : result.get_time(),
            'timezone' : result.get_timezone()
        }
    }
    return data
