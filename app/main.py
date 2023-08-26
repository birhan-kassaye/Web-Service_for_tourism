from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/get_country_info", methods=["POST"])
def get_country_info():
    country_name = request.form.get("country_name")
    
    if country_name:
        
        data = response.json()
        
        if data:
            country_info = data[0]
            return jsonify(country_info)
    
    return jsonify({"error": "Country not found."})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
