from models.weather_statistics import YearlyStatistics, MonthlyStatistics

class WeatherReportGenerator:
    def generate_yearly_report(self, stats: YearlyStatistics):
        print(f"Highest: {stats.highest_temp}C on {stats.highest_temp_day.strftime('%B %d')}")
        print(f"Lowest: {stats.lowest_temp}C on {stats.lowest_temp_day.strftime('%B %d')}")
        print(f"Humidity: {stats.highest_humidity}% on {stats.humid_day.strftime('%B %d')}")
    
    def generate_monthly_report(self, stats: MonthlyStatistics):
        print(f"Highest Average: {stats.avg_highest_temp}C")
        print(f"Lowest Average: {stats.avg_lowest_temp}C")
        print(f"Average Mean Humidity: {stats.avg_mean_humidity}%")