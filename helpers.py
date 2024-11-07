

def invalid_format_provided(message="Invalid format provided"):
    print(message)
    print("Usage:")
    print("  For yearly report: python3 weatherman.py /path/to/files-dir -e <year>")
    print("  For monthly report: python3 weatherman.py /path/to/files-dir -a <year/month>")
    print("  For console bar charts: python3 weatherman.py /path/to/files-dir -c <year/month>")

