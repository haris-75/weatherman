
from statistics import mean
from models.weather_statistics import YearlyStatistics, MonthlyStatistics

class WeatherCalculator:
    def __init__(self, temprature_readings):
        self.temprature_readings = temprature_readings

    def _calculate_highest_temperature_and_day(self):
        highest_temp = None
        highest_temp_day = None
        for reading in self.temprature_readings:
            if not highest_temp or reading.max_temp > highest_temp:
                highest_temp = reading.max_temp
                highest_temp_day = reading.recorded_date
        return highest_temp, highest_temp_day
    
    def _calculate_lowest_temperature_and_day(self):
        lowest_temp = None
        lowest_temp_day = None
        for reading in self.temprature_readings:
            if not lowest_temp or reading.min_temp < lowest_temp:
                lowest_temp = reading.min_temp
                lowest_temp_day = reading.recorded_date
        return lowest_temp, lowest_temp_day
    
    def _calculate_highest_humidity_and_day(self):
        highest_humidity = None
        highest_humidity_day = None
        for reading in self.temprature_readings:
            if not highest_humidity or reading.humidity > highest_humidity:
                highest_humidity = reading.humidity
                highest_humidity_day = reading.recorded_date
        return highest_humidity, highest_humidity_day


    def calculate_yearly_statistics(self):
        stats = YearlyStatistics()
        stats.highest_temp, stats.highest_temp_day = self._calculate_highest_temperature_and_day()
        stats.lowest_temp, stats.lowest_temp_day = self._calculate_lowest_temperature_and_day()
        stats.highest_humidity, stats.humid_day = self._calculate_highest_humidity_and_day()
        return stats
    
    def calculate_monthly_statistics(self):

        max_temps = list(map(lambda reading: reading.max_temp, self.temprature_readings))
        min_temps = list(map(lambda reading: reading.min_temp, self.temprature_readings))
        mean_humidities = list(map(lambda reading: reading.mean_humidity, self.temprature_readings))

        avg_highest_temp = mean(max_temps)
        avg_lowest_temp = mean(min_temps)
        avg_mean_humidity = mean(mean_humidities)

        stats = MonthlyStatistics()
        stats.avg_highest_temp = avg_highest_temp
        stats.avg_lowest_temp = avg_lowest_temp
        stats.avg_mean_humidity = avg_mean_humidity
        return stats
    
    def calculate_daily_temperatures(self):
        daily_stats = []
        for reading in self.temprature_readings:
            if reading.max_temp is not None and reading.min_temp is not None:
                daily_stats.append({
                    'recorded_date': reading.recorded_date,
                    'max_temp': reading.max_temp,
                    'min_temp': reading.min_temp
                })
        return daily_stats
 