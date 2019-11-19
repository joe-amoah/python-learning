# Python program that allows the user to enter the latitude and longitude of two points on the Earth in degrees
from math import radians, cos, sin, asin, sqrt
def distance (lat1, lat2, lon1, lon2):

    lon1 = radians(lon1)
    lon2 = radians(lon2)
    lat1 = radians(lat1)
    lat2 = radians(lat2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2

    c = 2 * asin(sqrt(a))

    r = 6371

    return(c * r)


lat1 = 53.32055555555556
lat2 = 53.31861111111111
lon1 = -1.7297222222222221
lon2 = -1.69972222222222223
print(distance(lat1, lat2, lon1, lon2), 'K.M')

