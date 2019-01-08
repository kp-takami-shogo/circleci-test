# coding: utf-8

import os
import re
import yaml

TEST_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..', '..', 'eT-test')


class TestCase:

    @staticmethod
    def get_testcase_list():
        testcase_list = os.listdir(os.path.join(TEST_PATH, 'testcase'))
        testcase_list = [test for test in testcase_list if test != '.DS_Store']
        testcase_list = [re.split('\.testcase\.yml', test)[0] for test in testcase_list]
        return testcase_list

    @staticmethod
    def get_testcase(testcase_name):
        file = open(os.path.join(TEST_PATH, 'testcase', testcase_name + '.testcase.yml'))
        return yaml.load(file)
