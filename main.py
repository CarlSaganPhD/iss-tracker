from flask import Flask, jsonify, render_template
import requests
import os

app = Flask(__name__)

# Check if running in development or production
if os.environ.get("FLASK_ENV") == "development":
    app.debug = True
else:
    app.debug = False

@app.route('/')
def index():
    app.logger.info("Index route accessed.")
    return render_template('index.html')

@app.route('/iss_location')
def iss_location():
    response = requests.get('https://api.wheretheiss.at/v1/satellites/25544')
    iss_data = response.json()
    app.logger.info(f"Fetching ISS location: Latitude {iss_data.get('latitude')} Longitude {iss_data.get('longitude')}")
    return jsonify({
        'latitude': iss_data.get('latitude'),
        'longitude': iss_data.get('longitude'),
        'altitude': iss_data.get('altitude'),  # Altitude of the ISS in kilometers
        'velocity': iss_data.get('velocity'),  # Velocity of the ISS in kilometers per hour
        'visibility': iss_data.get('visibility'),  # Whether the ISS is in daylight or nighttime
        'footprint': iss_data.get('footprint'),  # Diameter of the ground area which the ISS can be seen from
        'timestamp': iss_data.get('timestamp')  # Timestamp of the data
    })

# Use the PORT environment variable or default to 5000
port = int(os.environ.get("PORT", 5000))

if __name__ == "__main__":
    # Run the Flask app using the built-in development server
    app.run(host="0.0.0.0", port=port)