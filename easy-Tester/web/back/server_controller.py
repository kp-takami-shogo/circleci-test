# coding: utf-8

from wsgiref import simple_server

class ServerController:

    def __init__(self, app):
        self.httpd = simple_server.make_server('localhost', 9001, app)
        self.httpd.serve_forever()
