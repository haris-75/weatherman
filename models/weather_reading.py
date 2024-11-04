from datetime import date

class WeatherReading:
    def __init__(self, reading_date: date, max_temp: int, min_temp: int, humidity: int, mean_humidity: int):
        self.date = reading_date
        self.max_temp = max_temp
        self.min_temp = min_temp
        self.humidity = humidity
        self.mean_humidity = mean_humidity
