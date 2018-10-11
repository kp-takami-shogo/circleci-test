# coding: utf-8

import json
import os
import yaml
import inspect
import importlib
import glob

TEST_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../../test/')

class Project:

    def on_get(self, req, resp):
        project_list = self.getProjectList(TEST_PATH)

        resp.body = json.dumps(project_list)

        resp.append_header('Access-Control-Allow-Origin', req.get_header('Origin'))


    def getProjectList(self, test_path):
        project_list = os.listdir(test_path)
        project_list = [project for project in project_list if project != '.DS_Store']
        return project_list
