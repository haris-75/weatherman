
import csv
import os
from models.weather_reading import WeatherReading

class WeatherParser:
    def __init__(self, directory_path: str):
        self.directory_path = directory_path

    def parse_files(self):
        temprature_readings = []
        for filename in os.listdir(self.directory_path):
            file_path = os.path.join(self.directory_path, filename)
            temprature_readings.extend(self._parse_file(file_path))
        return temprature_readings

    def _parse_file(self, file_path):
        try:
            with open(file_path, mode='r') as file:
                return [self._parse_row(row) for row in csv.DictReader(file) if self._parse_row(row)]
        except IOError:
            return [] 

    def _parse_row(self, row):
        try:
            reading_date = row.get('PKT') or row.get('PKST')
            if not reading_date:
                return None 
            max_temp = row['Max TemperatureC']
            min_temp = row['Min TemperatureC']
            humidity = row['Max Humidity']
            mean_humidity = row[' Mean Humidity'].strip()
            return WeatherReading(reading_date, max_temp, min_temp, humidity, mean_humidity)
        except (ValueError, KeyError):
            return None
