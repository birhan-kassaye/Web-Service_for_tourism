from flask import Flask, render_template, request, jsonify
import json
import requests

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    if request.args:
        city = request.args.get('city_name')
        if city:
            with open('static/file.json') as f:
                data = json.load(f)

            for i in data.values():
                if i['__class__'] == 'City':
                    if i['name'] == city:
                        return render_template("city_specific.html", city=city)
                    else:
                        pass
                else:
                    pass
            return jsonify({'error': "not found"})
        else:
            return jsonify({'error': 'not found'})

    else:
        return render_template("index.html")

@app.route("/<city>", methods=["GET"])
def get_city_info(city):
    if city:
        with open('static/file.json') as f:
            data = json.load(f)

        for i in data.values():
            if i['__class__'] == 'City':
                if i['name'] == city: 
                    return render_template("city_specific.html", city=city)
                else:
                    pass
            else:
                pass
        return jsonify({'error': 'not found'})

    else:
        return jsonify({'error': 'not found'})


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
