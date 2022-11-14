import csv


class Weather:
    date = ""
    cloud_coverage = 0
    sunshine = 0
    min_temp = 0
    mean_temp = 0
    max_temp = 0
    precipitation = 0

    def __init__(self, date, cloud_coverage, sunshine, min_temp, mean_temp, max_temp, precipitation):
        self.date = date
        self.cloud_coverage = cloud_coverage
        self.sunshine = sunshine
        self.min_temp = min_temp
        self.mean_temp = mean_temp
        self.max_temp = max_temp
        self.precipitation = precipitation


weather_data_for_each_day_of_the_year = []

with open('datasets/london_weather_2020.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    next(reader)  # skip over the field names of the csv files
    for row in reader:
        weather_data_for_each_day_of_the_year.append(
            Weather(row[0], row[1], row[2], row[6], row[5], row[4], row[7]))

print(weather_data_for_each_day_of_the_year[0].min_temp)
