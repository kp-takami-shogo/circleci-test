# coding: utf-8

# テストコントローラ
#
# @param
# test_builder TestBuilderインスタンス
# browser_controller BrowserControllerインスタンス
# sleep_time 処理を遅延させる秒数

import sys
import os
import traceback
from pprint import pprint

from selenium.common.exceptions import WebDriverException

from test_builder import TestBuilder
from browser_controller import BrowserController
from assertion_manager import AssertionManager
from reporter import Reporter

sys.path.append(os.path.join(os.path.dirname(__file__), '../util/'))

from browser_control_setting import BrowserControlSetting
from printer import Printer

class Tester:

    def __init__(self):
        self.test_builder = TestBuilder()
        self.testsuites_name = ''

    # テスト実行
    def execute(self, *, browser = '', url = '', driver_path = '',
                remote_flg = 0, remote_host_url = '',
                report_path = './result.xml', artifacts_path = './',
                wait_seconds = 5, sleep_time = 0, debug_mode = False):

        self.sleep_time = sleep_time
        self.debug_mode = debug_mode

        self.assertion_manager = AssertionManager(self.testsuites_name)

        for testsuite_name, testcase_list in self.test_builder.getTest().items():
            Printer.printer('testsuite_name', [testsuite_name])
            print('')

            for testcase_name, process_list in testcase_list.items():
                try:
                    self.browser_controller = BrowserController(
                        browser = browser,
                        driver_path = driver_path,
                        remote_flg = remote_flg,
                        remote_host_url = remote_host_url,
                        artifacts_path = artifacts_path,
                        wait_seconds = wait_seconds
                    )

                    self.assertion_manager.setBrowserController(self.browser_controller)

                    self.browser_controller.accessUrl([url])

                    Printer.printer('testcase_name', [testcase_name])

                    for process in process_list:

                        for process_name, params in process.items():

                            if self.sleep_time:
                                self.browser_controller.sleepBySeconds([self.sleep_time])

                            if self.getProcessType(process_name) == 'browser_controller':
                                self.executeBrowserControllerMethod(process_name, params)
                            else:
                                self.executeAssertionerMethod(testsuite_name, testcase_name, process_name, params)

                except Exception as e:
                    Printer.printer('exception', [traceback.format_exc()])

                    self.assertion_manager.addTotalErrorCount()
                    self.assertion_manager.addTestSuitesErrorCount()
                    self.assertion_manager.addTestSuiteErrorCount()
                    self.assertion_manager.setTestCaseResult('error')
                    self.assertion_manager.addTestCaseContent(traceback.format_exc())
                    self.assertion_manager.addTestCaseResults(testcase_name)

                    self.browser_controller.screenshot([testsuite_name + '-' + testcase_name])

                    self.browser_controller.closeBrowser()

                    continue

                self.assertion_manager.addTestCaseResults(testcase_name)

                self.browser_controller.closeBrowser()

            self.assertion_manager.addTestSuiteResult(testsuite_name)

        print('')
        Printer.printer('assert_result', [self.assertion_manager.getTotalAssertSuccesses(), self.assertion_manager.getTotalAssertFailures(), self.assertion_manager.getTotalAssertErrors()])
        print('')

        self.assertion_manager.setTestSuitesResult()

        reporter = Reporter()

        reporter.createReport(self.assertion_manager.getResults(), report_path = report_path)


    # testsuitesをセット
    def setTestSuites(self, testsuites_name):
        self.testsuites_name = testsuites_name


    # testsuiteを追加
    def addTestSuite(self, testsuite_name):
        self.test_builder.addTestSuite(testsuite_name)


    # testcaseを追加
    def addTestCase(self, testcase_name, testcase):
        self.test_builder.addTestCase(testcase_name, testcase)


    def addConfig(self, config_file_path):
        self.test_builder.addConfig(config_file_path)


    # processタイプをゲット
    def getProcessType(self, process_name):
        if 'assert' in process_name:
            return 'assert'
        else:
            return 'browser_controller'


    # BrowserControllerのメソッドを実行
    def executeBrowserControllerMethod(self, process_name, params):
        config = self.test_builder.getConfig()

        if params is None or not params:
            browser_control_key = process_name
            param_list = []
        else:
            i = 0
            operate = ''
            by_item = ''
            param_list = []
            for param_name, param in params.items():
                if i == 0:
                    by_item = param_name.capitalize()

                if param in config:
                    param_list.append(config[param])
                else:
                    param_list.append(param)

                i += 1

            browser_control_key = process_name + by_item

        if self.debug_mode:
            Printer.printer('process', [browser_control_key, param_list])

        eval('self.browser_controller.' + BrowserControlSetting.getBrowserControl(browser_control_key))(param_list)

    # Assertionerのメソッドを実行
    def executeAssertionerMethod(self, testsuite_name, testcase_name, process_name, assertion):
        config = self.test_builder.getConfig()

        param_list = []
        for assertion_key, params in assertion.items():
            for param in params.values():
                if param in config:
                    param_list.append(config[param])
                else:
                    param_list.append(param)

            if self.debug_mode:
                Printer.printer('process', [process_name + ' ' + assertion_key, param_list])

        self.assertion_manager.assertion(testsuite_name, testcase_name, assertion_key, param_list)
