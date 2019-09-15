
# HouseHunting4Rewina

## To Dos:

- [x] Gather the initial bus stations.
- [x] Create a Git repo and connect it.
- [ ] Write a script that uses the Google Maps Places API to extract longitude and latitude for each bus station in the CSV file, and then append the information to each line in the CSV. 
- [ ] Add the Great-Circle Distance function that will allow distance calculations between two coordinates on the face of the Earth.
- [ ] Write a script that accepts a place location info as input (from terminal or a text file) using the Google Maps Places API and returns a list of the closest stations within a given distance metric. 
- [ ] Setup a simple REST API using Flask that can accept a potential location as input (address? query?) and return the closest bus station(s) within a given distance.
- [ ] Create a front end interface to interact with the Flask API.
- [ ] Add a Google Maps window for graphics.


## Background:
Rewina has been looking for a place to stay. She has visited multiple places, but one of the issues is that she hasn't been able to know beforehand if the place is close to a University of Maryland College Park Shuttle Bus Station or not. This project was started to help with that.

## Comma-Separated-Value (CSV) Formatting:

The list_of_stations.csv file makes use of semi-colons to separate the information in the following way:

- The bus station identification number in the NextBus System
- The bus station number in its respective bus line 
- The name of the bus station
- ~~Add the longitutude and latitude values of each station as two semi-colon separated value.~~

## The APIs
This project makes use of Google's Places API. The API key is private and is saved outside of this git repo.


## Regarding the Bus Lines:
As of today (2019-09-15), the following bus lines are available and have been saved in the CSV file. Note that some of these bus lines are subject to change in the SPRING semester, and this projcet is only applicable to the FALL semester. The hope is that Rewina will have found a room by before then.

- 104 College Park Metro
- 105 Campus Connector
- 108 Adelphi
- 109 River Road
- 111 Silver Spring
- 113 Hyattsville (ID)
- 114 University View 
- 115 Orange
- 116 Purple (PM)
- 117 Blue
- 118 Gold
- 122 Green
- 123 Discovery District
- 126 New Carrollton
- 127 Mazza Grandmarc
- 128 The Enclave
- 131 MGM/Enclave
- 132 The Varsity
- 133 Grocery Shopping Shuttle
- 140 Carey School of Law
- 141 Gaithersburg Park&Ride
- 142 Columbia Park&Ride
- 143 Greenbelt


#### Notes:
- ID: "ID is required to ride these shuttles"
- PM: "Evening Service Route"
- Bus line 110 was at the moment of writing undergoing service change.