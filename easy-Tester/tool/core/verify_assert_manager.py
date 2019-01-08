# -*- coding: utf-8 -*-

import sys
import os

from verifier import Verifier
from asserter import Asserter

sys.path.append(os.path.join(os.path.dirname(__file__), '../setting/'))
from verify_setting import VerifySetting
from assert_setting import AssertSetting


class VerifyAssertManager:

    def __init__(self, testsuites_name):
        self.verifier = Verifier()
        self.asserter = Asserter()

        self.testsuites_name = testsuites_name
        self.testsuites_tests = 0
        self.testsuites_failures = 0
        self.testsuites_errors = 0

        self.testsuite_tests = 0
        self.testsuite_failures = 0
        self.testsuite_errors = 0

        self.testcase_results = []
        self.testcase_result = ''
        self.testcase_content = ''

        self.all_count_per_testcase = 0
        self.failure_count_per_testcase = 0

        self.total_successes = 0
        self.total_failures = 0
        self.total_errors = 0

        self.results = {
            'testsuites_name': self.testsuites_name,
            'testsuites_tests': 0,
            'testsuites_failures': 0,
            'testsuites_errors': 0,
            'testsuite_results': [],
            'time': 0
        }

    def set_browser_controller(self, browser_controller):
        self.verifier.set_browser_controller(browser_controller)
        self.asserter.set_browser_controller(browser_controller)

    def verify(self, verify_key, params):
        result = eval('self.verifier.' + VerifySetting.get_verify(verify_key))(params)

        self.all_count_per_testcase += 1

        if result[0]:
            self.total_successes += 1
        else:
            self.failure_count_per_testcase += 1
            self.total_failures += 1
            self.set_testcase_result('failure')
            self.add_testcase_content(result[1])

        return result[0]

    def assertion(self, assert_key, params):
        result = eval('self.asserter.' + AssertSetting.get_assert(assert_key))(params)

        self.all_count_per_testcase += 1

        if result[0]:
            self.total_successes += 1
        else:
            self.failure_count_per_testcase += 1
            self.total_failures += 1
            self.set_testcase_result('failure')
            self.add_testcase_content(result[1])

        return result[0]

    def get_results(self):
        return self.results

    def set_testsuites_result(self, time):
        self.results['testsuites_tests'] = self.testsuites_tests
        self.results['testsuites_failures'] = self.testsuites_failures
        self.results['testsuites_errors'] = self.testsuites_errors
        self.results['time'] = time

    def add_testsuites_errors(self):
        self.testsuites_errors += 1

    def add_testsuite_result(self, testsuite_name, time):
        self.results['testsuite_results'].append({
            'testsuite_name': testsuite_name,
            'testsuite_tests': self.testsuite_tests,
            'testsuite_failures': self.testsuite_failures,
            'testsuite_errors': self.testsuite_errors,
            'testcase_results': self.testcase_results,
            'time': time
        })

        self.testsuite_tests = 0
        self.testsuite_failures = 0
        self.testsuite_errors = 0
        self.testcase_results = []

    def add_testsuite_errors(self):
        self.testsuite_errors += 1

    def add_testcase_results(self, testcase_name, time):
        if not (self.testcase_result or self.all_count_per_testcase):
            self.testcase_result = 'skipped'

        self.testcase_results.append({
            'testcase_name': testcase_name,
            'testcase_result': self.testcase_result,
            'testcase_content': self.testcase_content,
            'time': time
        })

        if self.testcase_result == 'failure':
            self.testsuites_failures += 1
            self.testsuite_failures += 1

        self.testsuites_tests += 1
        self.testsuite_tests += 1

        self.all_count_per_testcase = 0

        self.testcase_result = ''
        self.testcase_content = ''

    def set_testcase_result(self, result):
        self.testcase_result = result

    def add_testcase_content(self, content):
        self.testcase_content += content

    def get_failure_count_per_testcase(self):
        return self.failure_count_per_testcase

    def get_total_successes(self):
        return self.total_successes

    def get_total_failures(self):
        return self.total_failures

    def get_total_errors(self):
        return self.total_errors

    def add_total_errors(self):
        self.total_errors += 1
