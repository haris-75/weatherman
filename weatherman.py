import sys

from parsers.weather_parser import WeatherParser
from calculators.weather_calculator import WeatherCalculator
from reports.report_generator import WeatherReportGenerator

def main():
    if len(sys.argv) < 4:
        print("Usage: python3 weatherman.py /path/to/files-dir -e <year>")
        return

    directory_path = sys.argv[1]
    option = sys.argv[2]

    parser = WeatherParser(directory_path)
    readings = parser.parse_files()

    if option == '-e': 
        year = int(sys.argv[3])
        yearly_readings = [r for r in readings if r.date.year == year]
        
        if not yearly_readings:
            print(f"No data available for the year {year}.")
            return

        calculator = WeatherCalculator(yearly_readings)
        stats = calculator.calculate_yearly_statistics()

        report_generator = WeatherReportGenerator()
        report_generator.generate_yearly_report(stats)

    elif option == '-a': 
        try:
            year, month = map(int, sys.argv[3].split('/'))
        except ValueError:
            print("Invalid format for year/month. Please use the format 'YYYY/MM', e.g., '2004/6'.")
            return

        monthly_readings = [r for r in readings if r.date.year == year and r.date.month == month]
        
        if not monthly_readings:
            print(f"No data available for {year}/{month}.")
            return

        calculator = WeatherCalculator(monthly_readings)
        stats = calculator.calculate_monthly_statistics()

        report_generator = WeatherReportGenerator()
        report_generator.generate_monthly_report(stats)



if __name__ == "__main__":
    main()