import math

class Station:
    def __init__(self, NextBusID, LineID, StationName, lon=0, lat=0):
        self.ID = NextBusID
        self.fullLineID = []
        self.busLineNum = [] 
        self.busLineStopNum = []
        self.name = StationName
        self.lon = 0
        self.lat = 0

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
            if not NextBusID in Stations_Dict:
                Stations_Dict[NextBusID] = Station(NextBusID, LineID, StationName)
            else: #For duplicate stations, do this
                Stations_Dict[NextBusID].add_duplicate(LineID)
    return Stations_Dict



def distance_func(candidate_lon, candidate_lat, station_object):
    # Calculates distance between two GPS coords on the Earth's surface using the Haversine Great-Circle Formula 
    # Credit: Michael Dunn |-> https://stackoverflow.com/questions/4913349/haversine-formula-in-python-bearing-and-distance-between-two-gps-points 
    lon1 = math.radians(candidate_lon)
    lat1 = math.radians(candidate_lat)
    
    lon2 = math.radians(station_object.lon)
    lat2 = math.radians(station_object.lat)

    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    distance = c*r
    return distance
