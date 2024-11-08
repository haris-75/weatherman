
from weatherman import Weatherman
from parsers.argument_parser import ArgumentParser

def main():

    argument_parser = ArgumentParser()
    argument_parser.parse_arguments()
    argv_style_args = argument_parser.get_argv_style_args()
    weatherman = Weatherman(argv_style_args)
    weatherman.driver()

if __name__ == "__main__":
    main()
