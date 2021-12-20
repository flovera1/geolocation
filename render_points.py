# import plotly.express as px
# import pandas as pd
#
# # instantiate a feature group for the incidents in the dataframe
# from folium import plugins
# import folium
# incidents = folium.map.FeatureGroup()
# # San Francisco latitude and longitude values
# latitude = 37.77
# longitude = -122.42
# # create map and display it
# sanfran_map = folium.Map(location=[latitude, longitude], zoom_start=12)
# # display the map of San Francisco
# sanfran_map
#
# df = pd.read_csv("data/sandyT6.csv")
# df = df[["lon", "lat"]]
#
#
# for lat, lng, in zip(df.lon, df.lat):
#  incidents.add_child(
#  folium.features.CircleMarker(
#  [lat, lng],
#  radius=5, # define how big you want the circle markers to be
#  color='yellow',
#  fill=True,
#  fill_color='red',
#  fill_opacity=0.6
#    )
#  )
#  # add pop-up text to each marker on the map
#  latitudes = list(df.lon)
#  longitudes = list(df.lat)
# for lat, lng in zip(latitudes, longitudes):
#     folium.Marker([lat, lng]).add_to(sanfran_map)
# # display map
# #
# sanfran_map.render()
import pandas as pd
import requests
from xml.etree import ElementTree
import numpy as np
import folium
from IPython.display import display


df = pd.read_csv("data/albertaT6.csv")
latitude = []
longitude = []
for i, row in df.iterrows():
 latitude.append(row["lat"])
 longitude.append(row["lon"])

locations = df[['lat', 'lon']]
locationlist = locations.values.tolist()

map = folium.Map(location=[38.9, -77.05], zoom_start=12)
for point in range(0, len(locationlist)):
    folium.Marker(locationlist[point], popup=df['user_screen_name'][point]).add_to(map)
display(map)