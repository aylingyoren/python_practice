import requests

# url = "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2022-01-01&endtime=2022-10-12&latitude=54.35&longitude=18.65&maxradiuskm=400"
url = "https://earthquake.usgs.gov/fdsnws/event/1/query?"
response = requests.get(url, headers={"Accept": "application/json"}, params={
                "format": "geojson",
                "starttime": "2022-01-01",
                "endtime": "2022-10-12",
                "latitude": "54.35",
                "longitude": "18.65",
                "maxradiuskm": "400"
})

print(f"Request to {url}. Response code is {response.status_code}.")

# print(response.text)    # type str
data = response.json()    # type dict
print(data["features"][0]["properties"]["place"])

print(response.headers["Date"])
print(response.headers["Content-Type"])

# for key in response.headers:
#     print(key)
