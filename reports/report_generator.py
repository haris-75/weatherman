from models.weather_statistics import WeatherStatistics

class WeatherReportGenerator:
    def generate_report(self, stats: WeatherStatistics):
        print(f"Highest: {stats.highest_temp}C on {stats.highest_temp_day.strftime('%B %d')}")
        print(f"Lowest: {stats.lowest_temp}C on {stats.lowest_temp_day.strftime('%B %d')}")
        print(f"Humidity: {stats.highest_humidity}% on {stats.humid_day.strftime('%B %d')}")
