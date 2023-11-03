from flask import Flask, request, jsonify

app = Flask(__name__)

weather_data = {
    'San Francisco': {'temperature': 14, 'weather': 'Cloudy'},
    'New York': {'temperature': 20, 'weather': 'Sunny'},
    'Los Angeles': {'temperature': 24, 'weather': 'Sunny'},
    'Seattle': {'temperature': 10, 'weather': 'Rainy'},
    'Austin': {'temperature': 32, 'weather': 'Hot'},
}

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/weather/<string:city>/', methods=['GET'])
def get_weather(city):
    weather_city = weather_data.get(city)
    if weather_city:
        return jsonify(weather_city)
    else:
        return jsonify({'error': 'City not found'}), 404

@app.route('/weather/', methods=['POST'])
def add_weather():
    data = request.get_json()
    city = data.get('city')
    temperature = data.get('temperature')
    weather = data.get('weather')
    if city and temperature is not None and weather:
        weather_data[city] = {'temperature': temperature, 'weather': weather}
        return jsonify({'message': f'Weather data for {city} added successfully'}), 201
    else:
        return jsonify({'error': 'Invalid data provided'}), 400

@app.route('/weather/<string:city>/', methods=['PUT'])
def update_weather(city):
    data = request.get_json()
    temperature = data.get('temperature')
    weather = data.get('weather')
    if city in weather_data:
        if temperature is not None:
            weather_data[city]['temperature'] = temperature
        if weather:
            weather_data[city]['weather'] = weather
        return jsonify({'message': f'Weather data for {city} updated successfully'}), 200
    else:
        return jsonify({'error': 'City not found'}), 404

@app.route('/weather/<string:city>/', methods=['DELETE'])
def delete_weather(city):
    if city in weather_data:
        del weather_data[city]
        return jsonify({'message': f'Weather data for {city} deleted successfully'}), 200
    else:
        return jsonify({'error': 'City not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
