from datetime import date

class YearlyStatistics:
    def __init__(self):
        self.highest_temp = None
        self.highest_temp_day = None
        self.lowest_temp = None
        self.lowest_temp_day = None
        self.highest_humidity = None
        self.humid_day = None
class MonthlyStatistics:
    def __init__(self):
        self.avg_highest_temp = None
        self.avg_lowest_temp = None
        self.avg_mean_humidity = None