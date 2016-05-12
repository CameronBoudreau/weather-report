class Conditions():
    def __init__(self, data):
        self.location = data['display_location']['full']
        self.time = data['observation_time']
        self.weather = data['weather']
        self.temp = data['temperature_string']
        self.humidity = data['relative_humidity']
        self.wind_spd = data['wind_mph']
        self.pressure = data['pressure_mb']
        self.pressure_trend = data['pressure_trend']
        self.precip = data['precip_today_string']

    def display_conditions(self):
        print('Current conditions in ' + self.location)
        print(self.time)
        print('*' * 40)
        print('Temperature: ', self.temp)
        print('Conditions: ' + self.weather)
        print('Humidity: ', self.humidity)
        print('Wind Speed :', self.wind_spd)
        print('Barometric Pressure: ', self.pressure, self.pressure_trend)
        print('Precipitation: ' + self.precip)
