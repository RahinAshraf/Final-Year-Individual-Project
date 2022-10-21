import csv
import datasets
import pandas as pd
import os


class Itinerary:
    rental_id = 0
    duration = 0
    bike_id = 0
    end_date = "No end date"  # this needs to be changed to use objects of type 'datetime'
    end_station_id = 0
    end_station_name = "No end station name"
    start_date = "No start date"  # this needs to be changed to use objects of type 'datetime'
    start_station_id = 0
    start_station_name = "No start station name"

    def __init__(self, rental_id, duration, bike_id, end_date, end_station_id,
                 end_station_name, start_date, start_station_id, start_station_name):
        self.rental_id = rental_id
        self.duration = duration
        self.bike_id = bike_id
        self.end_date = end_date
        self.end_station_id = end_station_id
        self.end_station_name = end_station_name
        self.start_date = start_date
        self.start_station_id = start_station_id
        self.start_station_name = start_station_name


itineraries = []
itinerary_data = []

# for file in os.listdir('datasets'):
#     if file.endswith('.csv'):
#         master_df = pd.concat([pd.read_csv(f'datasets/{file}')])
#
# master_df.to_csv('Master Dataset.CSV')

with open('datasets/195JourneyDataExtract01Jan2020-07Jan2020 (1).csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    next(reader)  # skip over the field names of the csv files
    for row in reader:
        itineraries.append(Itinerary(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))

print(itineraries[0].start_station_name)
