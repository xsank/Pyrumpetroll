__author__ = 'Xsank'
import json


def object_to_json(obj):
    return json.dumps(obj.__dict__)
