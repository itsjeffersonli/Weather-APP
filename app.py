from flask import Flask, render_template, request
from models.models import *
from models.detector import *
from models.get_ip import *
from api.weather_api import *
from api.ip_api import *

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main():
    ip = get_ip()
    location = ip_weather_locate(ip)
    get_weather(location)

    return render_template('main.html', icon=get_icon(), condition=get_condition(),
                           temperature=get_temperature(), wind_dir=get_wind_direction(),
                           rain=get_rain(), humidity=get_humidity(), city=get_city(), date=get_date(),
                           data=check_icons(), percent_condition=get_condition_percent(), color=white_black(),
                           comment=comment())


@app.route('/find', methods=['GET', 'POST'])
def find():
    if request.method == "POST":
        location = request.form["location"]
        get_weather(location)

        return render_template('find.html', icon=get_icon(), condition=get_condition(),
                               temperature=get_temperature(), wind_dir=get_wind_direction(),
                               rain=get_rain(), humidity=get_humidity(), city=get_city(), date=get_date(),
                               data=check_icons(), percent_condition=get_condition_percent(), color=white_black(),
                               comment=comment())
    else:
        new_ip = get_ip()
        location = ip_weather_locate(new_ip)
        get_weather(location)

        return render_template('main.html', icon=get_icon(), condition=get_condition(),
                               temperature=get_temperature(), wind_dir=get_wind_direction(),
                               rain=get_rain(), humidity=get_humidity(), city=new_ip, date=get_date(),
                               data=check_icons(), percent_condition=get_condition_percent(), color=white_black(),
                               comment=comment())


if __name__ == '__main__':
    app.run()
