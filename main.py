import requests
import time
from geopy.geocoders import Nominatim
from geopy.distance import geodesic


def find_location(lat, long):
    geolocator = Nominatim(user_agent="wohiwa2202@o3live.com")
    formatted_str = lat + ',' + long
    loc = geolocator.reverse(formatted_str)
    return loc

def find_distance(lat1, lat2, long1, long2):
    formatted1 = lat1 + ',' + long1
    formatted2 = lat2 + ',' + long2
    distance_in_miles = geodesic(formatted1, formatted2).miles
    return distance_in_miles


astro_response = requests.get('http://api.open-notify.org/astros.json').json()

no_astros = astro_response['number']
print('Current no. astronauts in space:', no_astros)

list_astros = astro_response['people']
for astro in list_astros:
    print('Astronaut ' + astro['name'] + ' is on the craft "' + astro['craft'] + '"')

cycles = 0
while cycles < 100:
    cycles += 1
    print("Refreshing...")

    iss_response = requests.get('http://api.open-notify.org/iss-now.json').json()
    iss_position = iss_response['iss_position']
    print("X: " + iss_position['latitude'] + " Y: " + iss_position['longitude'])

    location = find_location(iss_position['latitude'], iss_position['longitude'])
    if location is not None:
        print("It's on land @ " + str(location) + "!")
    else:
        print("ISS is over unrecognized land/ocean.")
    time.sleep(60)