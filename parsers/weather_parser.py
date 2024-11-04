import os
import csv
from datetime import datetime
from models.weather_reading import WeatherReading

class WeatherParser:
    def __init__(self, directory_path: str):
        self.directory_path = directory_path

    def parse_files(self):
        readings = []
        for filename in os.listdir(self.directory_path):
            file_path = os.path.join(self.directory_path, filename)
            with open(file_path, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        reading_date = datetime.strptime(row['PKT'], '%Y-%m-%d').date()
                        max_temp = int(row['Max TemperatureC'])
                        min_temp = int(row['Min TemperatureC'])
                        humidity = int(row['Max Humidity'])
                        mean_humidity = int(row[' Mean Humidity'].strip())
                        readings.append(WeatherReading(reading_date, max_temp, min_temp, humidity, mean_humidity))
                    except (ValueError, KeyError):
                        continue
        return readings