import datetime

class WeatherReading:
    def __init__(self, date: datetime.date, temperature_high: int, temperature_low: int, humidity: int):
        self.date = date
        self.temperature_high = temperature_high
        self.temperature_low = temperature_low
        self.humidity = humidity