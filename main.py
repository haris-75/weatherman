import sys

def main():
    if len(sys.argv) < 3:
        print("Usage: weatherman.py /path/to/files-dir -e <year>")
        return
    print("Hello I am weatherman")


if __name__ == "__main__":
    main()