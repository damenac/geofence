'''
Created on 18 august 2018
@author: David Mendez-Acuna
'''

from interface.BigGeopixel import BigGeopixel

print('Welcome to GEOFENCE')

longitude = raw_input("Please enter longitude: ")
latitude = raw_input("Please enter latitude: ")
print('You entered: (' + longitude + ', ' + latitude + ')')

france = BigGeopixel("France", 0, 0, 10)


def inside_big_pixel():
    print("I'm checking if your localization is inside the big pixel: " + france.to_string())
    
    

    
inside_big_pixel()
