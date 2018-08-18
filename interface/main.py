'''
Created on 18 august 2018
@author: David Mendez-Acuna
'''

from interface.BigGeopixel import BigGeopixel

print('Welcome to GEOFENCE')

latitude = int(raw_input("Please enter latitude: "))
longitude = int(raw_input("Please enter longitude: "))
print('You entered: (' + str(longitude) + ', ' + str(latitude) + ')')

france = BigGeopixel("France", 0, 0, 10)


def inside_big_pixel(latitude, longitude):
    print("I'm checking if your localization is inside the big pixel: " + france.to_string())
    return abs(france.latitude - latitude) >= france.radious and abs(france.longitude - longitude) >= france.radious

    
inside_big_pixel(latitude, longitude)
