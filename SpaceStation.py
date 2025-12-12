# Name: Aquielle Campbell   
# Date: 12/11/25
# Period: 4
# Lab: SpaceStation.py
# Description: Students use web services to gather and process live data from the internet.
#
#     Style - Code format, whitespace and PEP-8 style is followed making code easy to read.
#     Comments - Blocks of code are well commented, every function has a descriptive comment.
#     Tests -   The program runs as described in the specifications without errors(passes all tests).
#

import json  # to interpret JSON data from a web service
import urllib.request  # to load data from a specific web service api
import turtle  # for images
import time # for time.sleep

# TODO: Step 1 Who is in space?
url = 'http://api.open-notify.org/astros.json'

response = urllib.request.urlopen(url)
result = json.loads(response.read())

# print(result)
print('there are ',result['number'],' people in space.')

print('They are:')
for astro in result['people']:
    print('\t', astro['name'])

# TODO: Step 2 Where is the ISS?
time.sleep(1) # pause 1 sec before load map

url = 'http://api.open-notify.org/iss-now.json'

response = urllib.request.urlopen(url)
result = json.loads(response.read())

# print(result)
location = result['iss_position']
lat = location['latitude']
lon = location['longitude']

print('Latitude:', lat)
print('Longitude:', lon)

screen = turtle.Screen()
screen.setup(1280, 640)
screen.bgpic('map.gif')
screen.setworldcoordinates(-180, -90, 180 ,90)

screen.register_shape('iss.gif')
iss = turtle.Turtle()
iss.shape('iss.gif')
iss.setheading(90)

iss.penup()
iss.goto(float(lon), float(lat))

count = 0
while True:
    count += 1
    if count % 1000 == 0:
        try:
            # make a new request 
            response = urllib.request.urlopen(url)
            result = json.loads(response.read())

            location = result['iss_position']
            lat = location['latitude']
            lon = location['longitude']
            print(lon, lat)

            # move ISS
            iss.goto(float(lon), float(lat))
            iss.pendown()
        except:
            print('something bad happened')




screen.mainloop()