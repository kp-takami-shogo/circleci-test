#coding:utf-8

import sys

from assertioner import Assertioner

class AssertionManager:

    def __init__(self):
        self.assertioner = Assertioner()

        self.results = []

        self.testsuite_tests = 0
        self.assertion_count_per_testcase = 0

        self.testsuite_errors = 0
        self.testsuite_failures = 0

        self.testcase_results = []
        self.testcase_result = ''
        self.testcase_content = ''

        self.total_success_count = 0
        self.total_failure_count = 0
        self.total_error_count = 0


    def setBrowserController(self, browser_controller):
        self.assertioner.setBrowserController(browser_controller)


    def assertion(self, testcase_name, assertion_method, param_list):
        result = eval(assertion_method)(param_list)

        self.assertion_count_per_testcase += 1

        if result[0]:
            self.total_success_count += 1
        else:
            self.setTestCaseResult('failure')
            self.addTestCaseContent(result[1])
            self.total_failure_count += 1


    def setResult(self, testsuite_name):
        self.results.append({
            'testsuite_name': testsuite_name,
            'testsuite_tests': self.testsuite_tests,
            'testsuite_errors': self.testsuite_errors,
            'testsuite_failures': self.testsuite_failures,
            'testcase_results': self.testcase_results
        })

        self.testsuite_errors = 0
        self.testsuite_failures = 0

    def getResult(self):
        return self.results


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
            self.testsuite_failures += 1

        self.testsuite_tests += 1

        self.assertion_count_per_testcase = 0

        self.testcase_result = ''
        self.testcase_content = ''


    def setTestCaseResult(self, result):
        self.testcase_result = result


    def addTestCaseContent(self, content):
        self.testcase_content += content


    def getTotalSuccessCount(self):
        return self.total_success_count

    def getTotalFailureCount(self):
        return self.total_failure_count

    def addTotalErrorCount(self):
        self.total_error_count += 1

    def getTotalErrorCount(self):
        return self.total_error_count
