import csv


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

with open('195JourneyDataExtract01Jan2020-07Jan2020 (1).csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        #print(row)
        itineraries.append({'rental_id': row[0], 'duration': (row[1]), })

    print(itineraries[1]['rental_id'])

