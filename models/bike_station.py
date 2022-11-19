class BikeStation:
    bike_station_id = 0
    name = "No bike station name"
    latitude = 0.0
    longitude = 0.0
    number_of_bikes = 0
    number_of_standard_bikes = 0
    number_of_E_bikes = 0
    number_of_empty_docks = 0
    number_of_docks = 0

    def __init__(self, bike_station_id, name, latitude, longitude, number_of_bikes,
                 number_of_standard_bikes, number_of_E_bikes, number_of_empty_docks,
                 number_of_docks):
        self.bike_station_id = bike_station_id
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.number_of_bikes = number_of_bikes
        self.number_of_Standard_bikes = number_of_standard_bikes
        self.number_of_E_bikes = number_of_E_bikes
        self.number_of_empty_docks = number_of_empty_docks
        self.number_of_docks = number_of_docks


bikes_start_stations = []  # list of all bikesstations
station_name_list = []

# DO NOT DELETE
# with open('datasets/Book1.csv', 'r') as csv_file:
#     reader = csv.reader(csv_file)
#     next(reader)  # skip over the field names of the csv files
#     for row in reader:
#         if not row[8] in station_name_list:  # checks if the station has already been added (exp_total=787)
#             station_name_list.append(row[8])
#             bikes_start_stations.append(BikeStation(1, row[8],None, None))  # append the start_stations
