#coding:utf-8
import sys
import os

TEST_PATH = os.path.dirname(os.path.abspath(__file__)) + '/'
BASE_PATH = TEST_PATH + '../'
TOOL_PATH = BASE_PATH + 'tool/'

sys.path.append(TOOL_PATH + 'core/')
from tester import Tester

tester = Tester()
tester.addConfig(TEST_PATH + 'element.yml')

tester.setTestSuiteName('CircleCIテスト')

tester.addTestCase('タイトル一致 成功', [
    [TEST_PATH + 'testcase/test/success.testcase.yml']
])

tester.execute(
    browser = 'Chrome',
    url = 'http://localhost'
)
