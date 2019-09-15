# SEE README.MD FOR EXPLANATION

# Import Python Libraries
import requests

# Access API key saved outside of git repo
with open("../dev/PlacesAPI.txt") as api_file:
    API_KEY = api_file.read()

with open("list_of_stations.csv") as stations_file:
        STATIONS = stations_file.readlines()

#print(Stations_Dict)


#response = requests.get("https://maps.googleapis.com/maps/api/geocode/json?The+Varsity")
#response = requests.get("https://maps.googleapis.com/maps/api/place/findplacefromtext/json?+%20maryland%20UMD")
#print(response.headers)
