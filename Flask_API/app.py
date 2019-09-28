from flask import Flask, jsonify, request, abort
import json, math, requests
from urllib.parse import quote


app = Flask(__name__)

class Station:
    def __init__(self, NextBusID, LineID, StationName, lat=0, lng=0):
        self.ID = NextBusID
        self.fullLineID = []
        self.busLineNum = [] 
        self.busLineStopNum = []
        self.name = StationName
        self.lat = lat
        self.lng = lng
        self.rad_lat = math.radians(self.lat)
        self.rad_lng = math.radians(self.lng)

        self.set_line_id(LineID)

    def __str__(self):
        return self.name

    def set_line_id(self, LineID):
        self.fullLineID.append(LineID)
        self.busLineNum.append(LineID.split('#')[0])
        self.busLineStopNum.append(LineID.split('#')[1])

    def add_duplicate(self, LineID):
        self.set_line_id(LineID)

    def get_id(self):
        return self.ID

    def get_distance(self, other_lat, other_lng):
        dlat = math.radians(other_lat) - self.rad_lat
        dlon = math.radians(other_lng) - self.rad_lng  
        a = math.sin(dlat/2)**2 + math.cos(other_lat) * math.cos(self.rad_lat) * math.sin(dlon/2)**2
        c = 2 * math.asin(math.sqrt(a)) 
        r = 6371 # Radius of earth in kilometers. Use 3956 for miles 
        return c*r

def read_in_stations(the_csv_path):
    # Reads in "list_of_stations.csv", a semi-colon CSV file. It then parses it, creates Station objects and then returns a dictionary with all.
    with open(the_csv_path) as stations_file:
        STATIONS = stations_file.readlines()
        Stations_Dict = {}
        for line in STATIONS:
            split_line = line.split(';')
            NextBusID = split_line[0]
            LineID = split_line[1]
            StationName = split_line[2]
            StationLat = split_line[3]
            StationLng = split_line[4]
            if not NextBusID in Stations_Dict:
                Stations_Dict[NextBusID] = Station(NextBusID, LineID, StationName, float(StationLat), float(StationLng))
            else: #For duplicate stations, do this
                Stations_Dict[NextBusID].add_duplicate(LineID)
    return Stations_Dict

def getLATnLNG(query):

    baseURL = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?"
    query = quote(query)
    request = "{}input={}&inputtype=textquery&fields=geometry&key={}".format(baseURL, query, API_KEY)
    response = requests.get(request)
    data = json.loads(response.text)
    #print(response.text)
    try:
        lat = data['candidates'][0]['geometry']['location']['lat']
        lng = data['candidates'][0]['geometry']['location']['lng']
    except:
        lat = None
        lng = None
    return lat, lng

def returnDistances(gpscoords):
    lat = gpscoords[0]
    lng = gpscoords[1]
    distances = []
    try:
        for station in All_Stations:
            distances.append((All_Stations[station].get_distance(lat, lng), station))
        distances.sort() #They are sorted in terms of distance
    except:
        distances = None
    return distances


def json_response(distances, geocoords, number):
    information_to_list = {}
    information_to_list['QUERY_INFO'] = [{'query_lat' : geocoords[0], 'query_lng' : geocoords[1]}]
    for i in range(len(distances)):
        curr_station = All_Stations[distances[i][1]]
        information_to_list[curr_station.name] = [{'distance' : distances[i][0], 'buss_fullLineID' : curr_station.fullLineID, 
                                                    'lat' : curr_station.lat, 'lng' : curr_station.lng}]
        if i > number:
            break

    return jsonify(information_to_list)

with open("../../dev/PlacesAPI.txt") as api_file:
    API_KEY = api_file.read()
  
# Read in stations
All_Stations = read_in_stations("list_of_stations.csv")



@app.route('/')
def index():
    return "<h2> Welcome to the HomeHunting4Rewina Flask API </h2>"


@app.route('/json/<query>/<int:num>')
def json_query(query = None, num = 10):
    if query != None:
        lat, lng = getLATnLNG(query)
        if (lat == None) or (lng == None):
            abort(404) #Replace with better error handling
        else:
            distances = returnDistances((lat,lng))
            if (distances == None):
                abort(405) #Replace with better error handling
            else:
                return json_response(distances, (lat, lng), num)
