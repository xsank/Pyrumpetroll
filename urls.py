__author__ = 'Xsank'

from handlers import IndexHandler
from handlers import WSHandler

handlers=[
    (r"/",IndexHandler),
    (r"/ws",WSHandler),
    ]