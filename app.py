from flask import Flask, render_template, request, jsonify
from services.osrm_service import get_optimal_route
from services.emissions import calculate_emissions
from services.weather_service import get_weather_data

app = Flask(__name__)

# Emissions factors (kg CO2 per liter of fuel)
EMISSIONS_FACTORS = {
    "petrol": 2.31,  # Petrol: 2.31 kg CO2 per liter
    "diesel": 2.68,  # Diesel: 2.68 kg CO2 per liter
    "electric": 0.0  # Electric vehicles have no direct emissions
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/route', methods=['POST'])
def route():
    data = request.json
    origin = data.get('origin')  # Format: [latitude, longitude]
    destination = data.get('destination')  # Format: [latitude, longitude]
    vehicle_type = data.get('vehicle_type', 'car')  # Default vehicle type
    fuel_type = data.get('fuel_type', 'petrol')  # Default fuel type
    fuel_efficiency = data.get('fuel_efficiency', 15)  # Default fuel efficiency in km/l

    # Fetch route information from OSRM
    route_info = get_optimal_route(origin, destination)
    if route_info:
        # Calculate emissions based on route distance, fuel type, and fuel efficiency
        distance = route_info['distance']  # Distance in meters
        emissions = calculate_emissions(distance, vehicle_type, fuel_type, fuel_efficiency)

        # Fetch weather data for origin and destination
        origin_weather = get_weather_data(origin)
        destination_weather = get_weather_data(destination)

        return jsonify({
            "route": route_info,
            "emissions": emissions,
            "origin_weather": origin_weather.get('data', {}).get('forecast', {}),
            "destination_weather": destination_weather.get('data', {}).get('forecast', {})
        })
    else:
        return jsonify({"error": "Could not calculate route"}), 500


if __name__ == '__main__':
    app.run(debug=True)
