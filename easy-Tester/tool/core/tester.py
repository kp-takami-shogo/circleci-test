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

from printer import Printer

class Tester:

    def __init__(self):
        self.test_builder = TestBuilder()

        self.testsuite_name = ''


    # BrowserControllerインスタンスゲット
    def getBrowserController(self):
        return self.browser_controller

    # TestBuilderインスタンスゲット
    def getTestBuilder(self):
        return self.test_builder


    # テスト実行
    def execute(self, *, browser = '', url = '', driver_path = '',
                remote_flg = 0, remote_host_url = '',
                report_path = '', wait_seconds = 5, sleep_time = 0.5, debug_mode = False):

        self.sleep_time = sleep_time
        self.debug_mode = debug_mode

        self.assertion_manager = AssertionManager()

        for testcase_name, process_list in self.test_builder.getTestCase().items():

            try:

                self.browser_controller = BrowserController(
                    browser = browser,
                    driver_path = driver_path,
                    remote_flg = remote_flg,
                    remote_host_url = remote_host_url,
                    wait_seconds = wait_seconds
                )

                self.assertion_manager.setBrowserController(self.browser_controller)

                self.browser_controller.accessByUrl([url])

                Printer.printer('testcase_name', [testcase_name])

                for process in process_list:

                    for process_name, params in process.items():

                        if self.sleep_time:
                            self.browser_controller.sleepBySeconds([self.sleep_time])

                        if self.getProcessType(process_name) == 'browser_controller':
                            self.executeBrowserControllerMethod(process_name, params)
                        else:
                            self.executeAssertionerMethod(testcase_name, process_name, params)

            except Exception as e:
                Printer.printer('exception', [traceback.format_exc()])

                self.assertion_manager.addTotalErrorCount()
                self.assertion_manager.addTestSuiteErrorCount()
                self.assertion_manager.setTestCaseResult('error')
                self.assertion_manager.addTestCaseContent(traceback.format_exc())
                self.assertion_manager.addTestCaseResults(testcase_name)

                self.browser_controller.closeWindow()

                continue

            print('')

            self.assertion_manager.addTestCaseResults(testcase_name)

            self.browser_controller.closeWindow()

        Printer.printer('assert_result', [self.assertion_manager.getTotalSuccessCount(), self.assertion_manager.getTotalFailureCount(), self.assertion_manager.getTotalErrorCount()])
        print('')

        self.assertion_manager.setResult(self.testsuite_name)

        reporter = Reporter()

        if report_path:
            reporter.createReport(self.assertion_manager.getResult(), report_path = report_path)
        else:
            reporter.createReport(self.assertion_manager.getResult())


    # テスト名をセット
    def setTestSuiteName(self, testsuite_name):
        self.testsuite_name = testsuite_name


    # テストシナリオを追加する
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
            method = process_name
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

            method = process_name + 'By' + by_item

        if self.debug_mode:
            Printer.printer('process', [method, param_list])

        method = 'self.browser_controller.'+ method

        eval(method)(param_list)

    # Assertionerのメソッドを実行
    def executeAssertionerMethod(self, testcase_name, process_name, params):
        config = self.test_builder.getConfig()

        param_list = []
        for param in params.values():
            if param in config:
                param_list.append(config[param])
            else:
                param_list.append(param)

        method = process_name

        if self.debug_mode:
            Printer.printer('process', [method, param_list])

        method = 'self.assertioner.'+ method

        self.assertion_manager.assertion(testcase_name, method, param_list)
