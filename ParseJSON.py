import json

class ToObject(object):
    def __init__(self, data):
        self.__dict__ = json.loads(data)