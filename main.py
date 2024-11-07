import sys
from validator.validator import Validator
from weatherman import Weatherman
from helpers import invalid_format_provided


def main():
    validator = Validator(sys.argv)

    valid, message = validator.validate_arguments()
    if not valid:
        invalid_format_provided(message)
        return

    weatherman=Weatherman(sys.argv)
    weatherman.driver()

if __name__ == "__main__":
    main()
