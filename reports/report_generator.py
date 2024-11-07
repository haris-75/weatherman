from models.weather_statistics import YearlyStatistics, MonthlyStatistics
from constants import RED_COLOR, GREEN_COLOR, RESET_COLOR
import calendar


class WeatherReportGenerator:
    def generate_yearly_report(self, stats: YearlyStatistics):
        print(f"Highest: {stats.highest_temp}C on {stats.highest_temp_day.strftime('%B %d')}")
        print(f"Lowest: {stats.lowest_temp}C on {stats.lowest_temp_day.strftime('%B %d')}")
        print(f"Humidity: {stats.highest_humidity}% on {stats.humid_day.strftime('%B %d')}")
    
    def generate_monthly_report(self, stats: MonthlyStatistics):
        print(f"Highest Average: {int(stats.avg_highest_temp)}C")
        print(f"Lowest Average: {int(stats.avg_lowest_temp)}C")
        print(f"Average Mean Humidity: {int(stats.avg_mean_humidity)}%")

    def generate_console_bar_chart(self, daily_stats, year, month, combined=True):
        print(f"\n{calendar.month_name[month]} {year}")
        for stats in daily_stats:
            day = stats['recorded_date'].day
            max_temp = stats['max_temp']
            min_temp = stats['min_temp']
            
            max_bar = self._get_bars(max_temp)
            min_bar = self._get_bars(min_temp)

            if combined:
                print(f"{day:02d} {RED_COLOR}{min_bar}{RESET_COLOR} {GREEN_COLOR}{max_bar}{RESET_COLOR} {min_temp}C - {max_temp}C")
            else:
                print(f"{day:02d} {GREEN_COLOR}{max_bar}{RESET_COLOR} {max_temp}C")
                print(f"{day:02d} {RED_COLOR}{min_bar}{RESET_COLOR} {min_temp}C")

    def _get_bars(self, temprature):
        return '+' * temprature if temprature >= 0 else '-' * abs(temprature)