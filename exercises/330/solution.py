from pprint import pprint
import json


def load_json(chemin):
    json_data=open(chemin)
    data = json.load(json_data)
    return data
    json_data.close()
