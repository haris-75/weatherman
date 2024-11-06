from models.weather_statistics import YearlyStatistics, MonthlyStatistics
import calendar


class WeatherReportGenerator:
    def generate_yearly_report(self, stats: YearlyStatistics):
        print(f"Highest: {stats.highest_temp}C on {stats.highest_temp_day.strftime('%B %d')}")
        print(f"Lowest: {stats.lowest_temp}C on {stats.lowest_temp_day.strftime('%B %d')}")
        print(f"Humidity: {stats.highest_humidity}% on {stats.humid_day.strftime('%B %d')}")
    
    def generate_monthly_report(self, stats: MonthlyStatistics):
        print(f"Highest Average: {stats.avg_highest_temp}C")
        print(f"Lowest Average: {stats.avg_lowest_temp}C")
        print(f"Average Mean Humidity: {stats.avg_mean_humidity}%")

    def generate_console_bar_chart(self, daily_stats, year, month, combined=True):
        print(f"\n{calendar.month_name[month]} {year}")
        for stats in daily_stats:
            day = stats['date'].day
            max_temp = stats['max_temp']
            min_temp = stats['min_temp']
            
            max_bar = '+' * max_temp if max_temp >= 0 else '-' * abs(max_temp)
            min_bar = '+' * min_temp if min_temp >= 0 else '-' * abs(min_temp)

            if combined:
                print(f"{day:02d} \033[1;31m{min_bar}\033[0m \033[1;32m{max_bar}\033[0m {min_temp}C - {max_temp}C")
            else:
                print(f"{day:02d} \033[1;32m{max_bar}\033[0m {max_temp}C")
                print(f"{day:02d} \033[1;31m{min_bar}\033[0m {min_temp}C")