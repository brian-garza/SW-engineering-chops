# Script to find the distance a crow takes

import pgeocode

country = pgeocode.GeoDistance('us')

start_zip = input("What zip code does the crow start?\n")
end_zip = input ("Where does the crow end?\n")

segment_length = country.query_postal_code(start_zip, end_zip)
miles_seg_length = segment_length * float(0.621371)

print(f'The crow has traveled {miles_seg_length:2,.2f} miles so far')

####&&&&########&&&&########&&&&########&&&&########&&&&########&&&&####
####&&&&########&&&&########&&&&########&&&&########&&&&########&&&&####
####&&&&########&&&&########&&&&########&&&&########&&&&########&&&&####

class Coordinates():
    def __init__(self, start_coords, end_coords):

        self.start_coords = start_coords
        self.end_coords = end_coords

    def get_start_coords(self):
        start_coords = {}
        start_coords['lat']  = input("What is the starting latitude?\n")
        start_coords['long'] = input("What is the starting longitude?\n")
        return start_coords

    def get_end_coords(self):
        end_coords = {}
        end_coords['lat']  = input("What is the ending latitude?\n")
        end_coords['long'] = input("What is the ending longitude?\n")
        return end_coords

class Segment(Coordinates):
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def get_distance_of_segment(self, latitude, longitude):
        pass

class Trip(Segment):
    def __init__(self, latitude, longitude):
        pass

    def get_distance_of_trip(self):
        pass

