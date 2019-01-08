# coding: utf-8

import os
import inspect
import importlib
import glob
import falcon


class AppController:

    def __init__(self):
        self.app = falcon.API()

        api_list = self.load_api()

        for api in api_list:
            self.app.add_route('/' + api[0], api[1]())

    @staticmethod
    def load_api():
        api_list = []

        for fpath in glob.glob(os.path.dirname(os.path.abspath(__file__)) + '/api/*.py'):
            cpath = os.path.splitext(fpath)[0]
            cpath = cpath.split(os.path.sep)
            cpath = cpath[-2] + '.' + cpath[-1]

            mod = importlib.import_module(cpath)

            for cls_name, cls in inspect.getmembers(mod, inspect.isclass):
                api_list.append([cpath.split('.')[1], cls])

        return api_list

    def get_app(self):
        return self.app
