# -*- coding: utf-8 -*-
import sys
import os

TEST_PATH = os.path.dirname(os.path.abspath(__file__)) + '/'
BASE_PATH = TEST_PATH + '../'
TOOL_PATH = BASE_PATH + 'tool/'

sys.path.append(TOOL_PATH + 'core/')
from tester import Tester

tester = Tester()

tester.set_testsuites('CircleCI Test')

tester.add_testsuite('Test')

tester.add_testcase('テスト', [
    TEST_PATH + 'testcase/test.testcase.yml'
])

tester.execute(
    browser='Chrome',
    url='http://localhost',
    ci='circleci',
    report_path=TEST_PATH + 'reports/results.xml',
    artifacts_path=TEST_PATH + 'artifacts/',
    wait_seconds=2
)
