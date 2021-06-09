from flask import Flask, render_template, request
from models.models import *
from models.detector import *
from data.weather_api import *

app = Flask(__name__)

@app.route('/')
def main():
    night_day = check_day_night()
    return render_template('main.html', night_day=night_day)


@app.route('/find', methods=['GET', 'POST'])
def find():
    if request.method == "POST":
        location = request.form["location"]
        get_weather(location)

        data = check_icons()
        icon = get_icon()
        condition = get_condition()
        percent_condition = get_condition_percent()
        temperature = get_temperature()
        wind_dir = get_wind_direction()
        rain = get_rain()
        humidity = get_humidity()
        city = get_city()
        _date = get_date()

        return render_template('find.html', icon=icon, condition=condition,
                               temperature=temperature, wind_dir=wind_dir,
                               rain=rain, humidity=humidity, city=city, date=_date,
                               data=data, percent_condition=percent_condition)
    else:
        return render_template('main.html')


if __name__ == '__main__':
    app.run()
