# SEE README.MD FOR EXPLANATION

# Import Python Libraries
import requests, json
from urllib.parse import quote # For cleaning up strings for requests

# Access API key saved outside of git repo
with open("../dev/PlacesAPI.txt") as api_file:
    API_KEY = api_file.read()

with open("list_of_stations.csv") as stations_file:
        STATIONS = stations_file.readlines()


def getLATnLNG(name):

    baseURL = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?"
    query = quote(name)
    request = "{}input={}&inputtype=textquery&fields=geometry&key={}".format(baseURL, query, API_KEY)
    response = requests.get(request)
    data = json.loads(response.text)
    lat = data['candidates'][0]['geometry']['location']['lat']
    lng = data['candidates'][0]['geometry']['location']['lng']
    return lat, lng

print(getLATnLNG("Courtyards #500 Maryland"))