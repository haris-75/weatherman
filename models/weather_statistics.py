from datetime import date

class YearlyStatistics:
    def __init__(self):
        self.highest_temprature = None
        self.highest_temprature_day = None
        self.lowest_temprature = None
        self.lowest_temprature_day = None
        self.highest_humidity = None
        self.humid_day = None
class MonthlyStatistics:
    def __init__(self):
        self.avg_highest_temprature = None
        self.avg_lowest_temprature = None
        self.avg_mean_humidity = None