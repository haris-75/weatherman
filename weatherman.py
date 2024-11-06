import sys

from parsers.weather_parser import WeatherParser
from utils.utils import Utils

def main():
    utils = Utils()
    
    if len(sys.argv) < 4:
        utils.invalid_format_provided()
        return

    directory_path = sys.argv[1]
    option = sys.argv[2]
    date_arg = sys.argv[3]

    if '/' in date_arg:
        try:
            year, month = date_arg.split('/')
            year = int(year)
            month = int(month)
        except ValueError:
            utils.invalid_format_provided()
            return
    else:
        try:
            year = int(date_arg)
            month = None
        except ValueError:
            utils.invalid_format_provided()
            return

    parser = WeatherParser(directory_path)
    readings = parser.parse_files()

    if month and (option=='-a' or option=='-c'):
        print(f"Generating report for year {year} and month {month}")
        utils.generate_report_for_month(year, month, readings, option)
    elif year and option=='-e' and month is None :
        print(f"Generating report for year {year}")
        utils.generate_report_for_year(year, readings)
    else:
        utils.invalid_format_provided()

if __name__ == "__main__":
    main()