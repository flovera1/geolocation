from geopy.geocoders import Nominatim

# create a Nominatim object
geolocator = Nominatim(user_agent="your_app_name")
location = geolocator.geocode("121 N LaSalle St, Chicago")
print(location.raw)
print(location.address)
print((location.latitude, location.longitude))