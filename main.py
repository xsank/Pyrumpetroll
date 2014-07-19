__author__ = 'Xsank'
import os.path
import tornado.ioloop
import tornado.options
import tornado.httpserver
import tornado.web

from urls import handlers
from settings import PORT
from settings import settings


class Application(tornado.web.Application):
    def __init__(self):
        tornado.web.Application.__init__(self,handlers,**settings)


def main():
    tornado.options.parse_command_line()
    http_server=tornado.httpserver.HTTPServer(Application())
    http_server.listen(PORT)
    tornado.ioloop.IOLoop.instance().start()


if __name__=="__main__":
    main()