# coding:utf-8

import sys
import os

from assertioner import Assertioner

sys.path.append(os.path.join(os.path.dirname(__file__), '../util/'))

from assertion_setting import AssertionSetting


class AssertionManager:

    def __init__(self, testsuites_name):
        self.assertioner = Assertioner()

        self.browser_controller = ''

        self.results = {
            'testsuites_name': testsuites_name,
            'testsuites_tests': 0,
            'testsuites_failures': 0,
            'testsuites_errors': 0,
            'testsuite_results': []
        }

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

        self.assertion_count_per_testcase = 0
        self.assertion_failure_count_per_testcase = 0

        self.total_assert_successes = 0
        self.total_assert_failures = 0
        self.total_assert_errors = 0

    def set_browser_controller(self, browser_controller):
        self.browser_controller = browser_controller
        self.assertioner.set_browser_controller(browser_controller)

    def assertion(self, testsuite_name, testcase_name, assertion_key, param_list):
        result = eval('self.assertioner.' + AssertionSetting.get_assertion(assertion_key))(param_list)

        self.assertion_count_per_testcase += 1

        if result[0]:
            self.total_assert_successes += 1
        else:
            self.assertion_failure_count_per_testcase += 1
            self.total_assert_failures += 1
            self.set_testcase_result('failure')
            self.add_testcase_content(result[1])

            self.browser_controller.screenshot(
                [testsuite_name + '-' + testcase_name + '-' + str(self.assertion_failure_count_per_testcase)])

    def get_results(self):
        return self.results

    def set_testsuites_result(self):
        self.results['testsuites_tests'] = self.testsuites_tests
        self.results['testsuites_failures'] = self.testsuites_failures
        self.results['testsuites_errors'] = self.testsuites_errors

    def add_testsuites_error_count(self):
        self.testsuites_errors += 1

    def add_testsuite_result(self, testsuite_name):
        self.results['testsuite_results'].append({
            'testsuite_name': testsuite_name,
            'testsuite_tests': self.testsuite_tests,
            'testsuite_failures': self.testsuite_failures,
            'testsuite_errors': self.testsuite_errors,
            'testcase_results': self.testcase_results
        })

        self.testsuite_tests = 0
        self.testsuite_failures = 0
        self.testsuite_errors = 0
        self.testcase_results = []

    def add_testsuite_error_count(self):
        self.testsuite_errors += 1

    def add_testcase_results(self, testcase_name):
        if not (self.testcase_result or self.assertion_count_per_testcase):
            self.testcase_result = 'skipped'

        self.testcase_results.append({
            'testcase_name': testcase_name,
            'testcase_result': self.testcase_result,
            'testcase_content': self.testcase_content
        })

        if self.testcase_result == 'failure':
            self.testsuites_failures += 1
            self.testsuite_failures += 1

        self.testsuites_tests += 1
        self.testsuite_tests += 1

        self.assertion_count_per_testcase = 0

        self.testcase_result = ''
        self.testcase_content = ''

    def set_testcase_result(self, result):
        self.testcase_result = result

    def add_testcase_content(self, content):
        self.testcase_content += content

    def add_total_error_count(self):
        self.total_assert_errors += 1

    def get_total_assert_successes(self):
        return self.total_assert_successes

    def get_total_assert_failures(self):
        return self.total_assert_failures

    def get_total_assert_errors(self):
        return self.total_assert_errors
