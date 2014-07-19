__author__ = 'Xsank'
import os.path

PORT=8888

settings=dict(
        template_path=os.path.join(os.path.dirname(__file__),"templates"),
        static_path=os.path.join(os.path.dirname(__file__),"static"),
        xsrf_cookies=True,
        cookie_secret="bb904fe1b095cab9499a85f864e6c612",
        port=8888,
    )