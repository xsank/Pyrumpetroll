__author__ = 'Xsank'
import json
import tornado.web
import tornado.websocket

from util import object_to_json
from structure import InitData
from structure import CloseData
from structure import SyncPosition


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("Rumpetroll.htm",entry=None)


class WSHandler(tornado.websocket.WebSocketHandler):
    clients=set()

    @staticmethod
    def broadcast(message):
        for client in WSHandler.clients:
            client.write_message(message)

    def open(self):
        WSHandler.clients.add(self)
        self.write_message(object_to_json(InitData(id(self))))

    def on_message(self, message):
        WSHandler.broadcast(message)

    def on_close(self):
        #self.write_message(object_to_json(CloseData(id(self))))
        WSHandler.clients.remove(self)