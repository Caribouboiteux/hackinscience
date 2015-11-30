import json
from distance import *
import sys


def locate(l, p):
    a = open('velib.json')
    data = json.load(a)
    a = 1000000000000000
    position = [l, p]
    for i in data:
        liste = []
        liste.append(i["latitude"])
        liste.append(i["longitude"])
        moi_station = euclidean(liste, position)
        if moi_station < a:
            a = moi_station
            station = i
    return station

