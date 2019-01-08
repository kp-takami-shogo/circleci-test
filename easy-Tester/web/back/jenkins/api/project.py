# coding: utf-8

import json
import os

TEST_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../../../test/')


class Project:

    def on_get(self, req, resp):
        project_list = self.get_project_list(TEST_PATH)

        resp.body = json.dumps(project_list)

        resp.append_header('Access-Control-Allow-Origin', req.get_header('Origin'))

    @staticmethod
    def get_project_list(test_path):
        project_list = os.listdir(test_path)
        project_list = [project for project in project_list if project != '.DS_Store']
        return project_list
