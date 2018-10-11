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

tester.addTestSuite('test')

tester.addTestCase('テスト',[
    [TEST_PATH + 'testcase/test.testcase.yml']
])

tester.execute(
    browser='Chrome',
    url='http://host.docker.internal',
    remote_flg = 1,
    remote_host_url = 'selenium:4444/wd/hub',
    wait_seconds=3
)
