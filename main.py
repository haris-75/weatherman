import sys

from parsers.weather_parser import WeatherParser

from calculators.weather_calculator import WeatherCalculator
from reports.report_generator import WeatherReportGenerator

def main():
    if len(sys.argv) < 4:
        print("Usage: python3 main.py /path/to/files-dir -e <year>")
        return

    directory_path = sys.argv[1]
    year = sys.argv[3]
    parser = WeatherParser(directory_path)
    readings = parser.parse_files()

    filtered_readings = [r for r in readings if r.date.year == int(year)]

    if not filtered_readings:
        print(f"No data available for the year {year}.")
        return
    
    calculator = WeatherCalculator(filtered_readings)
    stats = calculator.calculate_statistics()

    report_generator = WeatherReportGenerator()
    report_generator.generate_report(stats)


if __name__ == "__main__":
    main()