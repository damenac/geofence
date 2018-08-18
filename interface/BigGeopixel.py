'''
Created on 18 august 2018
@author: David Mendez-Acuna
'''


class BigGeopixel(object):

    name = None
    latitude = None
    longitude = None
    radious = None

    def __init__(self, name, latitude, longitude, radious):
        '''
        Constructor of the class.
        '''
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.radious = radious

    def to_string(self):
        return self.name + " [Latitude: " + str(self.latitude) + " Longitude: " + str(self.longitude) + "]"
