# HouseHunting4Rewina - FLASK API

Please refer to the README.MD for the overarching HouseHunting4Rewina Git Repo for information regarding the project as a whole. Continue reading for info on the FLASK API server.

## Purpose

The purpose of the Flask API server is to extend what was done previously in the findClosestStations.py program, which relied on the user filling up a text file ('list_of_queries.txt') with queries suitable for Google Place API. It re-uses code from that file, repackaging it and presenting it as a RESTful API.

## Usage

Follow the normal instructions for running a Python Flask server, i.e. (for Windows CMD):
```
set FLASK_APP = run.py 
flask run
```

Now, send a GET request to: http://127.0.0.1:5000/json/<QUERY>/<NUM>, making sure to replace the two variables with a query (e.g., maryland+umd) and the number of wanted requests respectively (e.g., 10).

Provided that the Google Place API didn't completley fail due to a bad query, this will return a JSON with the NUM number of closest stations to it place found by the query. It will also provide (under QUERY_INFO) the latitude and longitude of that place, which is good for error checking.


## Code

### Class Station:
Basic class to contain station-specific information. It can handle duplicates, whereby a station might have multiple buss lines associated with it.

### read_in_stations:
Reads in all the stations from "the database", i.e. CSV file "list_of_stations.csv".

### getLATnLNG:
Takes the query, i.e. a string, and returns the latitude and longitude for it using the Google Maps/Places API.

### returnDistances:
Returns a list of all the station-to-query distances and then sorts that list in accordance to shortest distance to longest.

### json_response:
Filters off the ten closest stations and packages them into a nice JSON format that will then be returned to the user.

### route('/'), index:
Just a very simple h2 tag.

### route('/json/<query>/<int:num>'), json_query:
The route for the API request. num has to be an integer or it will return a 404 page.

## Error Handling
At this point there seem to be two ways for the code to fail:
- The user sends in a really bad query that he Google Maps API just doesn't know what to do with, which causes it to send bad stuff to the server which in turn gets propagated as an error.
- The user picks a place that screws with the Haversine great-circles formula, e.g. by picking say "Stockholm" which has "positive" longitude (i.e., it's in the East) as opposed to the Maryland area which has "negative" longitude (it's in the West). This difference in signage causes that built-in Python math library's trigonometry functions to fail, which also propagates itself as an error to the user.

For now these are handled by with try-except blocks and then Flask "abort" functions, which will simply prevent the server from dying completely.

Covered: 
- If a user types in a non-integer number then it will automatically raise a 404 not found error, since that is defined in the json_query route.

Regarding some unexpected behavior:
- It is wholly possible for the GPS coordinates in the "list_of_stations.csv" file to be incorrect for certain stations (e.g., "the Enclave" station - there's another place called "the Enclave" in Silver Spring that my initial script had incorrectly attached itself to). The idea is that this is not a huge issue because each station is in a bus line, and excepting some very particular bus lines, the stations are quite close to each other. Thus, the user might get a "close distance"-hit to a station that is next/previous on the bus line.

- It is also wholly possible for the user to type in an unclear query/address for which the Google Maps/Place API will return the wrong place, e.g. a street in NYC and not in Greenbelt DC. 

The idea to solve both of these is to add a Google Maps/OpenStreetMaps box on the React front-end with pins on the map that will give a visual feedback to the user.