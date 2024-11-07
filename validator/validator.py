
from constants import MINIMUM_ARGUMENTS

class Validator:
    def __init__(self, args):
        self.args = args

    def validate_arguments(self):
        if len(self.args) < MINIMUM_ARGUMENTS:
            return False, "Insufficient arguments provided."

        return True, ""

    def validate_option_and_date(self, index):
        if index >= len(self.args) - 1:
            return False, "Invalid format: Option flag and date are required."

        option = self.args[index]
        date_arg = self.args[index + 1]

        if option not in ['-a', '-c', '-e']:
            return False, f"Invalid option: {option}"

        if '/' in date_arg:
            try:
                year, month = map(int, date_arg.split('/'))
                return True, (option, year, month)
            except ValueError:
                return False, f"Invalid date format: {date_arg}"
        else:
            try:
                year = int(date_arg)
                return True, (option, year, None)
            except ValueError:
                return False, f"Invalid year format: {date_arg}"
