
import argparse


class ArgumentParser:

    def __init__(self):
        self.parsed_arguments=[]
        parser = argparse.ArgumentParser(description='Weather Data Analysis Tool')
        parser.add_argument('directory', help='Directory path containing weather data files')
        
        parser.add_argument('-a', metavar='YEAR/MONTH', help='Generate average statistics for given year/month', action='append')
        parser.add_argument('-c', metavar='YEAR/MONTH', help='Generate bar chart for given year/month', action='append')
        parser.add_argument('-e', metavar='YEAR', help='Generate yearly statistics', action='append')
        self.parser=parser


    def parse_arguments(self):
        args = self.parser.parse_args()
        argv_style_args = ['weatherman', args.directory]
        
        if args.a:
            for date in args.a:
                argv_style_args.extend(['-a', date])
        if args.c:
            for date in args.c:
                argv_style_args.extend(['-c', date])
        if args.e:
            for date in args.e:
                argv_style_args.extend(['-e', date])

        self.argv_style_args = argv_style_args

    def get_argv_style_args(self):
        return self.argv_style_args
        

