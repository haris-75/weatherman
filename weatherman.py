import sys
from parsers.weather_parser import WeatherParser
from utils.utils import Utils

def main():
    utils = Utils()

    if len(sys.argv) < 4:
        utils.invalid_format_provided()
        return

    directory_path = sys.argv[1]
    parser = WeatherParser(directory_path)
    readings = parser.parse_files()

    i = 2
    while i < len(sys.argv):
        option = sys.argv[i]
        date_arg = sys.argv[i + 1] if i + 1 < len(sys.argv) else None
        
        if not date_arg:
            utils.invalid_format_provided()
            return

        if '/' in date_arg:
            try:
                year, month = map(int, date_arg.split('/'))
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

        if month and (option == '-a' or option == '-c'):
            print(f"\nGenerating report for year {year} and month {month} with option {option}")
            utils.generate_report_for_month(year, month, readings, option)
        elif year and option == '-e' and month is None:
            print(f"\nGenerating report for year {year} with option {option}")
            utils.generate_report_for_year(year, readings)
        else:
            utils.invalid_format_provided()
            return

        i += 2

if __name__ == "__main__":
    main()
