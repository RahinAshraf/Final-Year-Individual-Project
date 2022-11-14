import csv
import geopandas as gpd
import pandas as pd
import geopy as gy
from geopy.geocoders import Nominatim
import pandas as pd
from geopy.extra.rate_limiter import RateLimiter
from geopy.geocoders import Nominatim

import plotly.express as px

pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
pd.set_option('display.float_format', lambda x: f'%.{2}f' % x)
pd.set_option('display.max_colwidth', None)


class BikeStation:
    bike_station_id = 0
    name = ""
    parked_bikes = []
    geometric_cord = None

    def __init__(self, bike_station_id, name, parked_bikes, geometric_cord):
        self.bike_station_id = bike_station_id
        self.name = name
        self.parked_bikes = parked_bikes
        self.geometric_cord = geometric_cord


bikes_start_stations = []  # list of all bikesstations
station_name_list = []

# DO NOT DELETE
# with open('datasets/Book1.csv', 'r') as csv_file:
#     reader = csv.reader(csv_file)
#     next(reader)  # skip over the field names of the csv files
#     for row in reader:
#         if not row[8] in station_name_list:  # checks if the station has already been added (exp_total=787)
#             #station_name_list.append(row[8])
#             # geolocator = Nominatim(user_agent="me")
#             # location = geolocator.geocode(row[8])
#             print(row[8])
#             station_name_list.append(row[8])
#             bikes_start_stations.append(BikeStation(1, row[8],None, None))  # append the start_stations


df = pd.read_csv('datasets/Book1.csv')

locator = Nominatim(user_agent="myGeocoder")
# 1 - conveneint function to delay between geocoding calls
geocode = RateLimiter(locator.geocode, min_delay_seconds=0.5)
# 2- - create location column
df['location'] = df['StartStation Name'].apply(geocode)
# 3 - create longitude, laatitude and altitude from location column (returns tuple)
df['point'] = df['location'].apply(lambda loc: tuple(loc.point) if loc else None)
# 4 - split point column into latitude, longitude and altitude columns
df[['latitude', 'longitude', 'altitude']] = pd.DataFrame(df['point'].tolist(), index=df.index)


df = df.join(pd.DataFrame(df.pop('location').values.tolist(), index=df.index))
df.rename(columns = {0:'location'}, inplace = True)
df['Postal Code'] = df['location'].str.split(',').str[-2]
df['Street'] = df['location'].str.split(',').str[0]

df.drop([1], axis=1, inplace=True)
# df.drop(['point','location'], axis=1, inplace=True)
df.set_index(['Rental Id'], inplace=True)
df.head()

fig = px.scatter_mapbox(df, lat="latitude", lon="longitude", hover_name="Street", hover_data=["Duration", "Bike Id"],
                        color_discrete_sequence=["fuchsia"], zoom=3, height=300)
fig.update_layout(mapbox_style="open-street-map")
# fig.update_layout(mapbox_style="satellite")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()

df.to_csv('datasets/1test.csv')



#print(len(bikes_start_stations))


# address = "Spanish Road, Clapham Junction"
# geolocator = Nominatim(user_agent="me")
# location = geolocator.geocode(address)
# print(location.latitude, location.longitude)

# print(bikes_start_stations[0].geometric_cord.latitude, bikes_start_stations[0].geometric_cord.longitude)

# with open('datasets/Book1.csv','r+') as csv_file:
# #         r = csv.reader(csv_file)
# #         next(r)
# #         for row in r:
# #             address = row[8]
# #             geolocator = Nominatim(user_agent="me")
# #             location = geolocator.geocode(address)
# #             print(location.latitude, location.longitude)
# #             row.append(location.latitude)


