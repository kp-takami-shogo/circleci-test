# coding: utf-8

import json
import os
import yaml
import inspect
import importlib
import glob

TEST_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../../test/')

class Test:

    def on_get(self, req, resp):
        test_list = self.getTestList(TEST_PATH + req.params['p'] + '/' + req.params['b'] + '/testcase')

        resp.body = json.dumps(test_list)

        resp.append_header('Access-Control-Allow-Origin', req.get_header('Origin'))


    def getTestList(self, branch_path):
        test_list = os.listdir(branch_path)
        test_list = [test for test in test_list if test != '.DS_Store']
        return test_list
