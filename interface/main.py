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


def inside_big_pixel(bigPixel, latitude, longitude):
    print("I'm checking if your localization is inside the big pixel: " + bigPixel.to_string())
    return ((latitude - bigPixel.latitude) ^ 2 + (longitude - bigPixel.longitude) ^ 2) < bigPixel.radious


def check_known_big_pixels():
    inside_france = inside_big_pixel(france, latitude, longitude)
    print("France: " + str(inside_france))


check_known_big_pixels()
