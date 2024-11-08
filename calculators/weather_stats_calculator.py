
from statistics import mean
from models.weather_statistics import YearlyStatistics, MonthlyStatistics


class WeatherStatsCalculator:
    def __init__(self, temprature_readings):
        self.temprature_readings = temprature_readings

    def _calculate_highest_temperature_and_day(self):
        highest_temprature = None
        highest_temprature_day = None
        for reading in self.temprature_readings:
            if not highest_temprature or reading.max_temprature > highest_temprature:
                highest_temprature = reading.max_temprature
                highest_temprature_day = reading.recorded_date
                
        return highest_temprature, highest_temprature_day
    
    def _calculate_lowest_temperature_and_day(self):
        lowest_temprature = None
        lowest_temprature_day = None
        for reading in self.temprature_readings:
            if not lowest_temprature or reading.min_temprature < lowest_temprature:
                lowest_temprature = reading.min_temprature
                lowest_temprature_day = reading.recorded_date

        return lowest_temprature, lowest_temprature_day
    
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
        stats.highest_temprature, stats.highest_temprature_day = self._calculate_highest_temperature_and_day()
        stats.lowest_temprature, stats.lowest_temprature_day = self._calculate_lowest_temperature_and_day()
        stats.highest_humidity, stats.humid_day = self._calculate_highest_humidity_and_day()
        return stats
    
    def calculate_monthly_statistics(self):
        max_tempratures = list(map(lambda reading: reading.max_temprature, self.temprature_readings))
        min_tempratures = list(map(lambda reading: reading.min_temprature, self.temprature_readings))
        mean_humidities = list(map(lambda reading: reading.mean_humidity, self.temprature_readings))

        avg_highest_temprature = mean(max_tempratures)
        avg_lowest_temprature = mean(min_tempratures)
        avg_mean_humidity = mean(mean_humidities)

        stats = MonthlyStatistics()
        stats.avg_highest_temprature = avg_highest_temprature
        stats.avg_lowest_temprature = avg_lowest_temprature
        stats.avg_mean_humidity = avg_mean_humidity
        return stats
    
    def calculate_daily_temperatures(self):
        daily_stats = []
        for reading in self.temprature_readings:
            if reading.max_temprature is not None and reading.min_temprature is not None:
                daily_stats.append({
                    'recorded_date': reading.recorded_date,
                    'max_temprature': reading.max_temprature,
                    'min_temprature': reading.min_temprature
                })
                
        return daily_stats
 
 
 