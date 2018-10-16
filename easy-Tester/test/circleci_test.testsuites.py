#coding:utf-8
import sys
import os

TEST_PATH = os.path.dirname(os.path.abspath(__file__)) + '/'
BASE_PATH = TEST_PATH + '../'
TOOL_PATH = BASE_PATH + 'tool/'

sys.path.append(TOOL_PATH + 'core/')
from tester import Tester

tester = Tester()

tester.setTestSuites('CircleCI Test')

tester.addTestSuite('Test')

tester.addTestCase('テスト',[
    [TEST_PATH + 'testcase/test.testcase.yml']
])

tester.execute(
    browser='Chrome',
    url='http://localhost',
    wait_seconds=3
)
