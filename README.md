
# HouseHunting4Rewina

## To Dos:

- [x] Gather the initial bus stations.
- [x] Create a Git repo and connect it.
- [x] Write a script that uses the Google Maps Places API to extract longitude and latitude for each bus station in the CSV file, and then append the information to each line in the CSV. 
- [x] Add the Great-Circle Distance function that will allow distance calculations between two coordinates on the face of the Earth.
- [x] Write a script that accepts a place location info as input (from terminal or a text file) using the Google Maps Places API and returns a list of the closest stations within a given distance metric. 
- [x] Setup a simple REST API using Flask that can accept a potential location as input (address? query?) and return the closest bus station(s) within a given distance.
- [x] Deploy the API to AWS.
- [x] Create a front end interface to interact with the Flask API.
- [x] [Deploy the Front-End to AWS](http://rewina.yared.se).
- [ ] Add a Google Maps window for graphics.

## Updates:

2019-09-15:
- Came up with the idea.

- Cleaned the copy+pasted files.
 
- Set up the Git repo.
 
- Set up the Google APIs.
 
- Did some initial python stuff.
 
- Created this README.MD.
 
- Not necessarily in that order.

2019-09-16:

- Finished the add_GPSCoords_script and supplemented the CSV file with GPS coordinates. Note that one error was found, specifically for the station "The Enclave". One such station exists on campus, but there is also one coincidentally very close to where Rewina lives currently ("The Enclave Apartments Silver Spring"). The Google Places API incorrectly grabbed the latter and as such said that there existed a shuttle station very close to her current address.

- It is now possible to fill a text file ("list_of_queries.txt") with rows of adresses and the program will then return whether or not those adresses are close enough within a given metric (e.g., 1 km) to a UMD shuttle bus. The program is called "findClosesStations.py",

2019-09-17:

- Made a Flask_API dir. Created the REST API using Flask. It is now possible to send a get request to address:5000/json/'query'/'num', replacing 'query' with the address/place query and 'num' with the number of stations to respond with. If you want the 10 closest you get the 10 closets, and so on. Though due to the way Jsonify is used on a dictionary to preserve the nice Json format, the responses are not in order so the front end 

- Reorganized the Git Repo, making the Files tab slightly obsolete and outdated.

2019-09-19

- Deployed the Flask API to AWS Beanstalk! It required that we change Note that the necessary zipfile used fr deployement has been created in a separate directory, so as to avoid my API-key gettng leaked through Github. 

- Initialized the React frontend.
    
2019-09-21:

- Followed a [React tutorial by Dev Ed](https://www.youtube.com/watch?v=U9T6YkEDkMo) on Youtube for creating a React app that communicates with a public API. It relies solely on functional components and React Hooks, making it very cool. By following that I was able to quickly set up the React frptnend to my specifications. 

- While the Flask API was deployed to Elastic Beanstalk since it is a "server", the React Frontend was instead compiled into its build form using ``` npm run build ``` and then uploaded and set up on AWS S3 Bucket as a static website.

- I bought the domain for [yared.se](yared.se) at GoDaddy. I have redirected Yared.se to go to my Github Pages site, but the subdomain [Rewina](rewina.yared.se) has been set up to redirect to the AwS 

## Background:
Rewina has been looking for a place to stay. She has visited multiple places, but one of the issues is that she hasn't been able to know beforehand if the place is close to a [University of Maryland College Park Shuttle](https://transportation.umd.edu/) Bus Station or not. This project was started to help with that.

## Files:

### README.MD:
This file.

### list_of_stations.csv
The CSV file that serves as a database for the project.

### list_of_stations_old_*.txt
Various versions of the list_of_stations.csv file. The file has been/will be updated and cleaned and thus older versions of the text file are saved.

### main.py
Where the main program development is happening right now.

### helper_code.py
Contains various supplementary functions and classes that can be used by other Python programs.

### add_GPSCoords_script.py
A script that was used to supplement the list_of_stations file with GPS coordinates of all the 400-500+ stations in the UMD Shuttle Bus system. For some few entries the script's query failed (a try/except block made sure to save those failed files as having 0,0 gps coordinates) but the success rate was close to 99%. Note that there is no actual guarantee that all of the queries were actually successful in returning the CORRECT place and not the coordinates of a different place (i.e., a False True).

### findClosestStations.py
Reads from the "list_of_queries.txt" file and gets out a range of addresses. It recovers the GPS coordinates of each of the addresses, calculates the distance to all the bus stations and then returns a list of the closest (6 or so) stations to that address (provided that they are within a given maximum distance range).

## REGARDING THE FLASK STUFF
Check out the README.MD for the Flask directory.

## Comma-Separated-Value (CSV) Formatting:

The list_of_stations.csv file makes use of semi-colons to separate the information in the following way:

- The bus station identification number in the NextBus System
- The bus station number in its respective bus line 
- The name of the bus station
- ~~The longitutude and latitude values of each station as two semi-colon separated value.~~

## The Public APIs
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
- "The Courtyards" has 3 stations: "The Courtyards \#300", "The Courtyards \#400" and "The Courtyards\#500. A Google Maps query is likely to only return the main "The Courtyards" GPS coordinate for them, and not their individual ones.