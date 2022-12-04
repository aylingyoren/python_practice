import requests
import sqlite3

start_time = input("Enter start time: ")
end_time = input("Enter end time: ")
latitude = input("Enter latitude: ")
longitude = input("Enter longitude: ")
max_radius_km = input("Enter max radius in km: ")
min_magnitude = input("Enter min magnitude: ")

url = "https://earthquake.usgs.gov/fdsnws/event/1/query?"
response = requests.get(url, headers={"Accept": "application/json"}, params={
    "format": "geojson",
    "starttime": start_time,
    "endtime": end_time,
    "latitude": latitude,
    "longitude": longitude,
    "maxradiuskm": max_radius_km,
    "minmagnitude": min_magnitude
})

print(response.url)
data = response.json()

earthquake_list = data["features"]
i = 1
for earthquake in earthquake_list:
    place, magnitude = earthquake["properties"]["place"], earthquake["properties"]["mag"]
    print(f"{i}. Place: {place}. Magnitude: {magnitude}")
    i += 1


# def save_earthquakes():
#     conn = sqlite3.connect('earthquakes_db.db')
#     cursor = conn.cursor()
#     cursor.execute('CREATE TABLE earthquakes (place TEXT, magnitude REAL)')
#     insert_query = "INSERT INTO earthquakes (place, magnitude) VALUES (?, ?)"
#
#     for eq in earthquake_list:
#         cursor.execute(insert_query, (eq["properties"]["place"], eq["properties"]["mag"]))
#
#     conn.commit()
#     conn.close()
#
#
# save_earthquakes()


# def show_earthquakes():
#     conn = sqlite3.connect('earthquakes_db.db')
#     cursor = conn.cursor()
#     cursor.execute('SELECT * FROM earthquakes')
#     [print(eq) for eq in cursor.fetchall()]
#
#     conn.commit()
#     conn.close()
#
#
# show_earthquakes()
