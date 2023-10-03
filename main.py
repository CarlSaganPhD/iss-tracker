from flask import Flask, jsonify, render_template
import requests
import os

app = Flask(__name__)

@app.route('/')
def index():
    app.logger.info("Index route accessed.")
    return render_template('index.html')

@app.route('/iss_location')
def iss_location():
    response = requests.get('https://api.wheretheiss.at/v1/satellites/25544')
    app.logger.info(f"Fetching ISS location: Latitude {response.json().get('latitude')} Longitude {response.json().get('longitude')}")
    return jsonify(response.json())

port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)