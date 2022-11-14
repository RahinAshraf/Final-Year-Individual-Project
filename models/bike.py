import csv


class Bike:
    bike_id = 0
    current_bike_station = ""
    distance_travelled = 0

    def __init__(self, bike_id, current_bike_station, distance_travelled):
        self.bike_id = bike_id
        self.current_bike_station = current_bike_station
        self.distance_travelled = distance_travelled


bikes = []

with open('datasets/195JourneyDataExtract01Jan2020-07Jan2020 (1).csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    next(reader)  # skip over the field names of the csv files
    for row in reader:
        bikes.append(Bike(row[2], row[8], row[1]))

print(bikes[0].current_bike_station)
