# -*- coding: utf-8 -*-

import os
import re
import yaml

from tester import Tester


class Runner:

    def __init__(self, test_path):
        self.tester = Tester()
        self.test_path = test_path

    def run(self):
        for file_name in os.listdir(self.test_path):
            if re.match('.+\.testsuites.yml$', file_name) is None:
                continue

            file = open(os.path.join(self.test_path, file_name))
            test = yaml.load(file)

            self.tester.set_testsuites(test['testsuites']['name'])

            for testsuite in test['testsuites']['test']:
                testsuite = testsuite['testsuite']

                self.tester.add_testsuite(testsuite['name'])

                for testcase in testsuite['test']:
                    testcase = testcase['testcase']

                    for testcase_index, testcase_path in enumerate(testcase['test']):
                        testcase['test'][testcase_index] = os.path.join(self.test_path, testcase_path)

                    self.tester.add_testcase(testcase['name'], testcase['test'])

            if 'reports_dir' in test['execute']:
                test['execute']['reports_dir'] = os.path.join(self.test_path, test['execute']['reports_dir'])
            else:
                test['execute']['reports_dir'] = os.path.join(self.test_path, 'reports')

            if 'artifacts_dir' in test['execute']:
                test['execute']['artifacts_dir'] = os.path.join(self.test_path, test['execute']['artifacts_dir'])
            else:
                test['execute']['artifacts_dir'] = os.path.join(self.test_path, 'artifacts')

            self.__rm_files_under_dir(test['execute']['reports_dir'])
            self.__rm_files_under_dir(test['execute']['artifacts_dir'])

            self.tester.execute(**test['execute'])

    @staticmethod
    def __rm_files_under_dir(rm_dir):
        for file_name in os.listdir(rm_dir):
            os.remove(os.path.join(rm_dir, file_name))
