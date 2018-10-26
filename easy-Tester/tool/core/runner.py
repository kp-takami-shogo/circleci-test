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

            file = open(self.test_path + file_name)
            test = yaml.load(file)

            self.tester.set_testsuites(test['testsuites']['name'])

            for testsuite in test['testsuites']['test']:
                testsuite = testsuite['testsuite']

                self.tester.add_testsuite(testsuite['name'])

                for testcase in testsuite['test']:
                    testcase = testcase['testcase']

                    for testcase_index, testcase_path in enumerate(testcase['test']):
                        testcase['test'][testcase_index] = self.test_path + testcase_path

                    self.tester.add_testcase(testcase['name'], testcase['test'])

            if 'report_path' in test['execute']:
                test['execute']['report_path'] = self.test_path + test['execute']['report_path']

            if 'artifacts_path' in test['execute']:
                test['execute']['artifacts_path'] = self.test_path + test['execute']['artifacts_path']

            self.tester.execute(**test['execute'])
