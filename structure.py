__author__ = 'Xsank'
import json


class SyncPosition(object):
    def __init__(self,gson=""):
        self.__dict__=json.loads(gson)


class SyncData(object):
    def __init__(self):
        self.type="message"
        self.message=""


class InitData(object):
    def __init__(self,id):
        self.type="welcome"
        self.id=id


class CloseData(object):
    def __init__(self,id):
        self.type="closed"
        self.id=id