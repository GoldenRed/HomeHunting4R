# SEE README.MD FOR EXPLANATION

# Import Python Libraries
import requests, json
from urllib.parse import quote

# Import Functions and Classes
from helper_code import *

def getLATnLNG(name):

    baseURL = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?"
    query = quote(name)
    request = "{}input={}&inputtype=textquery&fields=geometry&key={}".format(baseURL, query, API_KEY)
    response = requests.get(request)
    data = json.loads(response.text)
    #print(response.text)
    lat = data['candidates'][0]['geometry']['location']['lat']
    lng = data['candidates'][0]['geometry']['location']['lng']
    return lat, lng

def returnDistances(lat, lng):
    distances = []
    for station in All_Stations:
        distances.append((All_Stations[station].get_distance(lat, lng), station))
        #print(c, All_Stations[station].get_distance(39.042800, -76.981400))
        #c=c+1
    distances.sort()
    return distances

def printing_response(distances, address):
    print("The 10 closest stations to {}:".format(address))
    for i in range(10):
        print(All_Stations[distances[i][1]].name, distances[i][0])


# Access API key saved outside of git repo
with open("../dev/PlacesAPI.txt") as api_file:
    API_KEY = api_file.read()

# Read
All_Stations = read_in_stations("list_of_stations.csv")
#Rewy = (39.042800, -76.981400) #11407 July Drive, Silver Spring, MD
def main():
    with open("list_of_queries.txt") as q:
        addresses = q.read().splitlines()
        print(addresses) 

    for address in addresses:
        lat, lng = getLATnLNG(address)
        d = returnDistances(lat, lng)
        printing_response(d,address)
        print("________")

main()



