
from models.weather_statistics import YearlyStatistics, MonthlyStatistics

class WeatherCalculator:
    def __init__(self, readings):
        self.readings = readings

    def calculate_yearly_statistics(self):
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
    
    def calculate_monthly_statistics(self):
        total_max_temp = total_min_temp = total_mean_humidity = 0
        count = len(self.readings)

        for reading in self.readings:
            total_max_temp += reading.max_temp
            total_min_temp += reading.min_temp
            total_mean_humidity += reading.mean_humidity

        avg_highest_temp = total_max_temp // count
        avg_lowest_temp = total_min_temp // count
        avg_mean_humidity = total_mean_humidity // count

        stats = MonthlyStatistics()
        stats.avg_highest_temp = avg_highest_temp
        stats.avg_lowest_temp = avg_lowest_temp
        stats.avg_mean_humidity = avg_mean_humidity
        return stats
    
    def calculate_daily_temperatures(self):
        daily_stats = []
        for reading in self.readings:
            if reading.max_temp is not None and reading.min_temp is not None:
                daily_stats.append({
                    'date': reading.date,
                    'max_temp': reading.max_temp,
                    'min_temp': reading.min_temp
                })
        return daily_stats
 