from math import *


def Haversine(c1, c2):
    """calculate distance between too coordinates accounting for the
    curvature of the earth"""
    lat1 = float(c1.split(",")[0])
    lon1 = float(c1.split(",")[1])
    lat2 = float(c2.split(",")[0])
    lon2 = float(c2.split(",")[1])


    #convert degrees into radians
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 3959.87433               # Radius of earth in miles
    return c * r