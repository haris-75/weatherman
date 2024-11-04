
from models.weather_reading import WeatherReading
from models.weather_statistics import YearlyStatistics

class WeatherCalculator:
    def __init__(self, readings):
        self.readings = readings

    def calculate_yearly(self):
        stats = YearlyStatistics()
        for reading in self.readings:
            if stats.highest_temp is None or reading.max_temp > stats.highest_temp:
                stats.highest_temp = reading.max_temp
                stats.highest_temp_day = reading.date

            if stats.lowest_temp is None or reading.min_temp < stats.lowest_temp:
                stats.lowest_temp = reading.min_temp
                stats.lowest_temp_day = reading.date

            if stats.highest_humidity is None or reading.humidity > stats.highest_humidity:
                stats.highest_humidity = reading.humidity
                stats.humid_day = reading.date
        return stats
 