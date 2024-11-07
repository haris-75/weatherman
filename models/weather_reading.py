from datetime import date, datetime

class WeatherReading:
    def __init__(self, reading_date: date, max_temp: str, min_temp: str, humidity: str, mean_humidity: str):
        self.recorded_date = datetime.strptime(reading_date, '%Y-%m-%d').date()
        self.max_temp = int(max_temp)
        self.min_temp = int(min_temp)
        self.humidity = int(humidity)
        self.mean_humidity = int(mean_humidity)
