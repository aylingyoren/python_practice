from googleplaces import GooglePlaces, types, lang
import requests
import json

# send_url = 'http://freegeoip.net/json'
# r = requests.get(send_url)
# j = json.loads(r.text)
# print(j)
# lat = j['latitude']
# lon = j['longitude']

API_KEY = 'AIzaSyBwUW7kJtIwME81jKRNyzklF2dlzJTqUZg'
latitude = input('Your latitude: ')
longitude = input('Your longitude: ')
radius = input('Your radius: ')

google_places = GooglePlaces(API_KEY)

query_result = google_places.nearby_search(
    lat_lng={'lat': float(latitude), 'lng': float(longitude)},
    radius=int(radius),
    types=[types.TYPE_AIRPORT])

if query_result.has_attributions:
    print(query_result.html_attributions)

for place in query_result.places:
    print(place)
    print(place.name)
    print(f"Latitude: {place.geo_location['lat']}")
    print(f"Longitude: {place.geo_location['lng']}")
    print()
