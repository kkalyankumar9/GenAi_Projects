from flask import Flask, jsonify
import unittest

app = Flask(__name__)

weather_data = {
    'San Francisco': {'temperature': 14, 'weather': 'Cloudy'},
    'New York': {'temperature': 20, 'weather': 'Sunny'},
    'Los Angeles': {'temperature': 24, 'weather': 'Sunny'},
    'Seattle': {'temperature': 10, 'weather': 'Rainy'},
    'Austin': {'temperature': 32, 'weather': 'Hot'},
}

@app.route('/weather/<string:city>/', methods=['GET'])
def get_weather(city):
    city_weather = weather_data.get(city)
    if city_weather:
        return jsonify(city_weather)
    else:
        return jsonify({'error': 'City not found'}), 404

class TestWeatherApp(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_valid_city(self):
        response = self.app.get('/weather/San Francisco/')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['temperature'], 14)
        self.assertEqual(data['weather'], 'Cloudy')

    def test_invalid_city(self):
        response = self.app.get('/weather/InvalidCity/')
        data = response.get_json()
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['error'], 'City not found')

if __name__ == '__main__':
    unittest.main()
