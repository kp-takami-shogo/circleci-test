# coding: utf-8

from app_controller import AppController
from server_controller import ServerController

class BackendController:

    def __init__(self):
        app_controller = AppController()
        server_controller = ServerController(app_controller.getApp())
