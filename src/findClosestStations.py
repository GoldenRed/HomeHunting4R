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

def returnDistances(gpscoords):
    lat = gpscoords[0]
    lng = gpscoords[1]
    distances = []
    for station in All_Stations:
        distances.append((All_Stations[station].get_distance(lat, lng), station))
        #print(c, All_Stations[station].get_distance(39.042800, -76.981400))
        #c=c+1
    distances.sort()
    return distances

def printing_response(distances, address, maxDistance):
    print("The closest stations to {} (max 6 listed):".format(address))
    k = 0
    for i in range(len(distances)):
        if distances[i][0] < maxDistance:
            print(All_Stations[distances[i][1]].name, "%.2f" % distances[i][0])
            k = k+1
        if i > 6:
            break
    if k == 0:
        print('NO STATIONS WITHIN MAX DISTANCE! Closest:', All_Stations[distances[0][1]].name, "%.2f" % distances[0][0])





if __name__ == '__main__':
    max_distance = 1 #km, as the crow flies km
    print('-----PROGRAM START------')
    with open("../../dev/PlacesAPI.txt") as api_file:
        API_KEY = api_file.read()

    # Read
    All_Stations = read_in_stations("list_of_stations.csv")

    
    with open("list_of_queries.txt") as q:
        addresses = q.read().splitlines()
        print(addresses) 

    for address in addresses:
        print("-----NEW ADRESS-----")
        printing_response(returnDistances(getLATnLNG(address)), address, max_distance)
        


