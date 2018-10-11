#coding:utf-8

import sys
import os
from pprint import pprint

from assertioner import Assertioner

sys.path.append(os.path.join(os.path.dirname(__file__), '../util/'))

from assertion_setting import AssertionSetting

class AssertionManager:

    def __init__(self, testsuites_name):
        self.assertioner = Assertioner()

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

        self.assertion_count_per_testcase = 0

        self.testcase_results = []
        self.testcase_result = ''
        self.testcase_content = ''

        self.total_assert_successes = 0
        self.total_assert_failures = 0
        self.total_assert_errors = 0


    def setBrowserController(self, browser_controller):
        self.assertioner.setBrowserController(browser_controller)


    def assertion(self, testcase_name, assertion_key, param_list):
        result = eval('self.assertioner.' + AssertionSetting.getAssertion(assertion_key))(param_list)

        self.assertion_count_per_testcase += 1

        if result[0]:
            self.total_assert_successes += 1
        else:
            self.total_assert_failures += 1
            self.setTestCaseResult('failure')
            self.addTestCaseContent(result[1])


    def getResults(self):
        return self.results


    def setTestSuitesResult(self):
        self.results['testsuites_tests'] = self.testsuites_tests
        self.results['testsuites_failures'] = self.testsuites_failures
        self.results['testsuites_errors'] = self.testsuites_errors


    def addTestSuitesErrorCount (self):
        self.testsuites_errors += 1


    def addTestSuiteResult(self, testsuite_name):
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


    def addTestSuiteErrorCount (self):
        self.testsuite_errors += 1


    def addTestCaseResults(self, testcase_name):
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


    def setTestCaseResult(self, result):
        self.testcase_result = result


    def addTestCaseContent(self, content):
        self.testcase_content += content


    def addTotalErrorCount(self):
        self.total_assert_errors += 1


    def getTotalAssertSuccesses(self):
        return self.total_assert_successes

    def getTotalAssertFailures(self):
        return self.total_assert_failures

    def getTotalAssertErrors(self):
        return self.total_assert_errors
