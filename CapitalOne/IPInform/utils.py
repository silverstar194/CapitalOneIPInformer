from math import sin, cos, sqrt, atan2, radians

from shapely.geometry import MultiPoint
from geopy.distance import great_circle


def compute_distance(lat_one, lng_one, lat_two, lng_two):
    if not (lat_one and lng_one and lat_two and lng_two):
        return 0
# approximate radius of earth in km
    R = 6373.0

    lat1 = radians(lat_one)
    lon1 = radians(lng_one)
    lat2 = radians(lat_two)
    lon2 = radians(lng_two)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance


## https://geoffboeing.com/2014/08/clustering-to-reduce-spatial-data-set-size/
def get_centermost_point(cluster):
    centroid = (MultiPoint(cluster).centroid.x, MultiPoint(cluster).centroid.y)
    centermost_point = min(cluster, key=lambda point: great_circle(point, centroid).m)
    return tuple(centermost_point)
