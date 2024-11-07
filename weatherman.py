
from validator.validator import Validator
from parsers.weather_parser import WeatherParser

from calculators.weather_calculator import WeatherCalculator
from reports.report_generator import WeatherReportGenerator

from helpers import invalid_format_provided

class Weatherman:

    def __init__(self, arguments):
        validator = Validator(arguments)
        self.validator = validator
        self.arguments = arguments
        self.directory_path = arguments[1]

    def driver(self):
        parser = WeatherParser(self.directory_path)
        temprature_readings = parser.parse_files()

        for i in range(2, len(self.arguments), 2):
            valid, result = self.validator.validate_option_and_date(i)
            if not valid:
                invalid_format_provided(result)
                return

            option, year, month = result
            if month and (option == '-a' or option == '-c'):
                print(f"\nGenerating report for year {year} and month {month} with option {option}")
                self._generate_report_for_month(year, month, temprature_readings, option)
            elif year and option == '-e' and month is None:
                print(f"\nGenerating report for year {year} with option {option}")
                self._generate_report_for_year(year, temprature_readings)
            else:
                invalid_format_provided("Invalid combination of option and date.")
                return

    def _generate_report_for_year(self, year, temprature_readings):
        report_generator = WeatherReportGenerator()
        yearly_readings = [r for r in temprature_readings if r.recorded_date.year == year]
            
        if not yearly_readings:
            print(f"No data available for the year {year}.")
            return

        calculator = WeatherCalculator(yearly_readings)
        stats = calculator.calculate_yearly_statistics()
        report_generator.generate_yearly_report(stats)

    def _generate_report_for_month(self, year, month, temprature_readings, option):
        report_generator = WeatherReportGenerator()
        monthly_readings = [r for r in temprature_readings if r.recorded_date.year == year and r.recorded_date.month == month] 
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

