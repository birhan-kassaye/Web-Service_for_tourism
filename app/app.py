import json
import requests
from flask import Flask, render_template, request, jsonify
from connection import baseUrl

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    places = []
    if request.args:
        city = request.args.get('city_name')
        if city:
            response = requests.get(baseUrl + '/all')
            data = response.json()
            
            if response.status_code == 404:
                return

            for i in data:
                if i['__class__'] == 'City' and i['name'] == city:
                        region = i['region']
                        weather = i['weather']
                        population = i['population']
                        ids = i['id']
                        for j in data:
                            if j['__class__'] == 'TouristSite' and j['city_id'] == ids:
                                    places.append(j['name'])

                        return render_template("city_specific.html",
                                               city=city,
                                               region=region,
                                               weather=weather,
                                               population=population,
                                               ids=ids,
                                               places=places)
            return jsonify({'error': "not found"})
    return render_template("index.html")

@app.route("/<city>", methods=["GET"], strict_slashes=False)
def get_city_info(city):
    places = []
    if city:
        response = requests.get(baseUrl + '/all')
        data = response.json()

        if data: 
            for i in data:
                if i['__class__'] == 'City' and i['name'] == city: 
                    region = i['region']
                    weather = i['weather']
                    population = i['population']
                    ids = i['id']
                    for j in data:
                        if j['__class__'] == 'TouristSite' and j['city_id'] == ids:
                            places.append(j['name'])
                    return render_template("city_specific.html", 
                                                city=city,
                                                region=region,
                                                weather=weather,
                                                population=population,
                                                ids=ids,
                                                places=places)
        return jsonify({'error': 'not found'})
    return jsonify({'error': 'not found'})


@app.route("/<city>/<site>", methods=["GET"])
def getsiteinfo(city, site):
    if city and site:
        response = requests.get(baseUrl + '/all')
        data = response.json()
        for i in data:
            if i['__class__'] == 'City' and i['name'] == city:
                for j in data:
                    if j['__class__'] == 'TouristSite' and j['name'] == site:
                            return render_template('places_specific.html',
                                                    site=site,
                                                    city=city)
        return jsonify({'error': 'not found'})
    return jsonify({'error': 'not found'})


@app.route("/contribute", methods=["GET"])
def contribute():
    return render_template("contribute.html")


@app.route('/add_city', methods=["GET"])
def add_city():
    requests.post(baseUrl, headers={})
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
