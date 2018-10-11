# coding: utf-8

import json
import os
import yaml
import inspect
import importlib
import glob

TEST_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../../test/')

class Branch:

    def on_get(self, req, resp):
        branch_list = self.getBranchList(TEST_PATH + req.params['p'])

        resp.body = json.dumps(branch_list)

        resp.append_header('Access-Control-Allow-Origin', req.get_header('Origin'))


    def getBranchList(self, project_path):
        branch_list = os.listdir(project_path)
        branch_list = [branch for branch in branch_list if branch != '.DS_Store']
        return branch_list
