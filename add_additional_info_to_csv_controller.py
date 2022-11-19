import pandas as pd
from geopy.extra.rate_limiter import RateLimiter
from geopy.geocoders import Nominatim
import plotly.express as px

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.float_format', lambda x: f'%.{2}f' % x)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv('datasets/Data-for-15th-Jan-2020.csv')  # csv file you want to get more info for

locator = Nominatim(user_agent="myGeocoder")
# 1 - conveneint function to delay between geocoding calls
geocode = RateLimiter(locator.geocode, min_delay_seconds=0.5)
# 2- - create location column
df['location'] = df['StartStation Name'].apply(geocode)
# 3 - create longitude, laatitude and altitude from location column (returns tuple)
df['point'] = df['location'].apply(lambda loc: tuple(loc.point) if loc else None)
# 4 - split point column into latitude, longitude and altitude columns
df[['latitude', 'longitude', 'altitude']] = pd.DataFrame(df['point'].tolist(), index=df.index)
df = df.dropna()

df = df.join(pd.DataFrame(df.pop('location').values.tolist(), index=df.index))
df.rename(columns={0: 'location'}, inplace=True)
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
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
fig.show()

df.to_csv('datasets/15Jan2020.csv')  # newly made csv file that has additional data
