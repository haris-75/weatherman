

def invalid_format_provided(message="Invalid format provided"):
    print(message)
    print("Usage:")
    print("  For yearly report: python3 weatherman.py /path/to/files-dir -e <year>")
    print("  For monthly report: python3 weatherman.py /path/to/files-dir -a <year/month>")
    print("  For console bar charts: python3 weatherman.py /path/to/files-dir -c <year/month>")

def validate_date(date_arg):
    if '/' in date_arg:
        try:
            year, month = map(int, date_arg.split('/'))
            return True, (year, month)
        except ValueError:
            return False, f"Invalid date format: {date_arg}"
    else:
        try:
            year = int(date_arg)
            return True, (year, None)
        except ValueError:
            return False, f"Invalid year format: {date_arg}"