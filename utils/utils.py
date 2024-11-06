
from calculators.weather_calculator import WeatherCalculator
from reports.report_generator import WeatherReportGenerator

class Utils:
    def generate_report_for_year(self, year, readings):
        report_generator = WeatherReportGenerator()
        yearly_readings = [r for r in readings if r.date.year == year]
            
        if not yearly_readings:
            print(f"No data available for the year {year}.")
            return

        calculator = WeatherCalculator(yearly_readings)
        stats = calculator.calculate_yearly_statistics()
        report_generator.generate_yearly_report(stats)

    def generate_report_for_month(self, year, month, readings, option):
        report_generator = WeatherReportGenerator()
        monthly_readings = [r for r in readings if r.date.year == year and r.date.month == month] 
        if not monthly_readings:
            print(f"No data available for {year}/{month}.")
            return
        
        calculator = WeatherCalculator(monthly_readings)

        if option == '-a': 
            stats = calculator.calculate_monthly_statistics()
            report_generator.generate_monthly_report(stats)

        elif option == '-c':
            daily_stats = calculator.calculate_daily_temperatures()
            report_generator.generate_console_bar_chart(daily_stats, year, month)

    def invalid_format_provided(self):
        print("Usage:")
        print("  For yearly report: python3 weatherman.py /path/to/files-dir -e <year>")
        print("  For monthly report: python3 weatherman.py /path/to/files-dir -a <year/month>")
        print("  For console bar charts: python3 weatherman.py /path/to/files-dir -c <year/month>")
