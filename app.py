from flask import Flask, render_template, request, jsonify
# Get Data
from realtime.models.models import *
from realtime.models.detector import *
from realtime.api.weather_api import *
# Self API
from self_api.api_server.weather_api_v1 import *
from self_api.request.requester import *
from self_api.api_generator.generator import generate

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def main():
    country = random_country()
    get_weather(country)
    model = gather_data()
    print(country)
    if requests.status_codes == 500:
        return render_template('error.html')
    else:
        return render_template('main.html', icon=model.get_icon(), condition=model.get_condition(),
                        temperature=model.get_temperature(), wind_dir=model.get_wind_direction(),
                        rain=model.get_rain(), humidity=model.get_humidity(), city=model.get_city(), date=model.get_date(),
                        data=check_icons(), percent_condition=model.get_condition_percent(), color=white_black(),
                        comment=comment(), say_time=say_time())


@app.route('/find', methods=['POST', 'GET'])
def find():
    if request.method == "POST":
        location = request.form["location"]
        location = location.replace("[^A-Za-z]","");

        if requests.status_codes == 500:
            return render_template('error.html')
        else:
            if location == "":
                country = random_country()
                get_weather(country)
                model = gather_data()
                return render_template('main.html', icon=model.get_icon(), condition=model.get_condition(),
                            temperature=model.get_temperature(), wind_dir=model.get_wind_direction(),
                            rain=model.get_rain(), humidity=model.get_humidity(), city=model.get_city(), date=model.get_date(),
                            data=check_icons(), percent_condition=model.get_condition_percent(), color=white_black(),
                            comment=comment(), say_time=say_time())
            else:
                get_weather(location)
                model = gather_data()
                return render_template('find.html', icon=model.get_icon(), condition=model.get_condition(),
                            temperature=model.get_temperature(), wind_dir=model.get_wind_direction(),
                            rain=model.get_rain(), humidity=model.get_humidity(), city=model.get_city(), date=model.get_date(),
                            data=check_icons(), percent_condition=model.get_condition_percent(), color=white_black(),
                            comment=comment(), say_time=say_time())
    else:
        if requests.status_codes == 500:
            return render_template("error.html")
        else:
            country = random_country()
            get_weather(country)
            model = gather_data()
            return render_template('main.html', icon=model.get_icon(), condition=model.get_condition(),
                            temperature=model.get_temperature(), wind_dir=model.get_wind_direction(),
                            rain=model.get_rain(), humidity=model.get_humidity(), city=model.get_city(), date=model.get_date(),
                            data=check_icons(), percent_condition=model.get_condition_percent(), color=white_black(),
                            comment=comment(), say_time=say_time())


# API

@app.route('/api', methods=['POST', 'GET'])
def show_api():
    return render_template('api_manual/index.html')

@app.route('/api/v1/weather/generate', methods=['POST', 'GET'])
def generate_key():
    username = request.args.get('username')
    f = open('self_api/database/api_user.txt', 'r')
    info = f.read()
    if username in info:
        return jsonify({"status": "error", "message": "Username already exists"})
    f.close()
    # Generate API key
    generated_api = generate()
    f = open('self_api/database/api_user.txt', 'a')
    info = "{0} {1}\n".format(username, generated_api)
    f.write(info)

    return """Username: {0}
            \n API_KEY: {1}""".format(username, generated_api)



@app.route('/api/v1/weather', methods=['POST', 'GET'])
def api():
    username = request.args.get('user')
    api_key = request.args.get('api_key')
    city = request.args.get('city')

    f = open('self_api/database/api_user.txt', 'r')
    info = f.read()
    info = info.split()
    if username in info:
        index = info.index(username) + 1
        user_api_key = info[index]
        if api_key == user_api_key:
            city = str(city)
            generate_data(city)
            show_data()
            dataset = ret_data()
            dataset = json.dumps(dataset, indent=4)
            return "{0}".format(dataset)
        else:
            return jsonify({"status": "error", "message": "API KEY is Invalid"})
    else:
        return jsonify({"status": "error", "message": "Username is Invalid"})


if __name__ == '__main__':
    app.run()
