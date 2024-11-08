from datetime import date, datetime

class WeatherReading:
    def __init__(self, reading_date: date, max_temprature: str, min_temprature: str, humidity: str, mean_humidity: str):
        self.recorded_date = datetime.strptime(reading_date, '%Y-%m-%d').date()
        self.max_temprature = int(max_temprature)
        self.min_temprature = int(min_temprature)
        self.humidity = int(humidity)
        self.mean_humidity = int(mean_humidity)
