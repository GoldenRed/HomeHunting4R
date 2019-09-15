import requests

API_KEY = "../dev/PlacesAPI.txt" #API key saved outside of git repo.
file_path = "list_of_stations.txt"

#response = requests.get("https://maps.googleapis.com/maps/api/geocode/json?The+Varsity")
response = requests.get("https://maps.googleapis.com/maps/api/place/findplacefromtext/json?+%20maryland%20UMD")
print(response.headers)
