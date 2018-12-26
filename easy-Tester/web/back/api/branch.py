# coding: utf-8

import json
import os

TEST_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../../test/')


class Branch:

    def on_get(self, req, resp):
        branch_list = self.get_branch_list(TEST_PATH + req.params['p'])

        resp.body = json.dumps(branch_list)

        resp.append_header('Access-Control-Allow-Origin', req.get_header('Origin'))

    @staticmethod
    def get_branch_list(project_path):
        branch_list = os.listdir(project_path)
        branch_list = [branch for branch in branch_list if branch != '.DS_Store']
        return branch_list
