from flask import Flask, render_template, request
from models.models import *
from models.detector import *
from api.weather_api import *

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def main():
    country = random_country()
    get_weather(country)

    return render_template('main.html', icon=get_icon(), condition=get_condition(),
                           temperature=get_temperature(), wind_dir=get_wind_direction(),
                           rain=get_rain(), humidity=get_humidity(), city=get_city(), date=get_date(),
                           data=check_icons(), percent_condition=get_condition_percent(), color=white_black(),
                           comment=comment(), say_time=say_time())


@app.route('/find', methods=['GET', 'POST'])
def find():
    if request.method == "POST":
        location = request.form["location"]

        if location == "":
            return render_template("")
        else:
            get_weather(location)

            return render_template('find.html', icon=get_icon(), condition=get_condition(),
                                   temperature=get_temperature(), wind_dir=get_wind_direction(),
                                   rain=get_rain(), humidity=get_humidity(), city=get_city(), date=get_date(),
                                   data=check_icons(), percent_condition=get_condition_percent(), color=white_black(),
                                   comment=comment(), say_time=say_time())
    else:
        country = random_country()
        get_weather(country)

        return render_template('main.html', icon=get_icon(), condition=get_condition(),
                               temperature=get_temperature(), wind_dir=get_wind_direction(),
                               rain=get_rain(), humidity=get_humidity(), city=get_city(), date=get_date(),
                               data=check_icons(), percent_condition=get_condition_percent(), color=white_black(),
                               comment=comment(), say_time=say_time())


if __name__ == '__main__':
    app.run()
