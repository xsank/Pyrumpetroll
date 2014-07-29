Pyrumpetroll
====================


Pyrumpetroll is a multiplayer-chat-room. It learns from the Rumpetroll. That one is written in ruby,
but this one is written in python and it supports Chinese.

License: MIT (see LICENSE)

Information
-----------

1.git clone https://github.com/xsank/Pyrumpetroll.git

2.pip install tornado

3.then change the Settings.js's socketserver url to your local ip or your domain

4.python main.py


Now it works and seems like the http://rumpetroll.com/


Preview
-------

![image](https://raw.githubusercontent.com/xsank/Pyrumpetroll/master/preview/preview.png "Preview image")


Others
-------

I have tried to deploy the Pyrumpetroll on the SAE,but it seems that the cloud-service don't support the
websocket. For example,i have to use SAE's channel to support long-connection,but it means the Pyrumpetroll
have to change a lot of code. So deploy the Pyrumpetroll on the vps our your personal server is the best and
easiest way.
