# SEE README.MD FOR EXPLANATION

# Import Python Libraries
import requests, json
from urllib.parse import quote # For cleaning up strings for requests

# Access API key saved outside of git repo
with open("../../dev/PlacesAPI.txt") as api_file:
    API_KEY = api_file.read()

with open("list_of_stations_old_2.txt") as stations_file:
        STATIONS = stations_file.readlines()


def getLATnLNG(name):

    baseURL = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?"
    query = quote(name)
    request = "{}input={}&inputtype=textquery&fields=geometry&key={}".format(baseURL, query, API_KEY)
    print(request)
    response = requests.get(request)
    data = json.loads(response.text)
    print(response.text)
    try:
        lat = data['candidates'][0]['geometry']['location']['lat']
        lng = data['candidates'][0]['geometry']['location']['lng']
        return lat, lng
    except: #If the google query fails, manually perform the query on google maps and manually add the coordinates to the file
        return 0, 0 #one could also replace this with a recursive function that re-performs the query with additional search terms


with open("list_of_stations_wGPS.txt", "w+") as f:
    for line in STATIONS:
        elements = line.split(';')
        print('place', elements[2])
        lat, lng = getLATnLNG(elements[2] + ' maryland UMD') #experiment with this
        f.write('{};{};{};{};{};\n'.format(elements[0], elements[1], elements[2],lat,lng ))