import folium
from pprint import pprint
import json
json_data = open("velib.json")
data = json.load(json_data)
map_osm = folium.Map(location=[48.8535, 2.3454], zoom_start=12)
for i in data:
    a = i["address"] + " " + i["name"]
    map_osm.simple_marker([i["latitude"], i["longitude"]], popup=a)
map_osm.create_map(path='velib.html')
json_data.close()
