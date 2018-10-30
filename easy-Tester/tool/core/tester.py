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

from pprint import  pprint

from test_builder import TestBuilder
from timer import Timer
from browser_controller import BrowserController
from assertion_manager import AssertionManager
from reporter import Reporter

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'setting'))
from browser_control_setting import BrowserControlSetting

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'util'))
from printer import Printer


TEST_PATH = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'eT-test')


class Tester:

    def __init__(self):
        self.test_builder = TestBuilder()
        self.timer = Timer()
        self.assertion_manager = ''
        self.browser_controller = ''

        self.testsuites_name = ''

        self.sleep_time = ''

        self.debug_mode = ''

    # テスト実行
    def execute(self, *, browser='', url='', driver_path='',
                remote_flg=0, remote_host_url='',
                ci='', reports_dir=os.path.join(TEST_PATH, 'reports'), artifacts_dir=os.path.join(TEST_PATH, 'artifacts'),
                wait_seconds=5, sleep_time=0, debug_mode=False):

        self.sleep_time = sleep_time
        self.debug_mode = debug_mode

        self.assertion_manager = AssertionManager(self.testsuites_name)

        self.timer.start_testsuites()

        for testsuite in self.test_builder.get_test():
            self.timer.start_testsuite()

            Printer.printer('testsuite_name', [testsuite['testsuite_name']])
            print('')

            for testcase in testsuite['testcase_list']:
                try:
                    self.timer.start_testcase()

                    self.browser_controller = BrowserController(
                        browser=browser,
                        driver_path=driver_path,
                        remote_flg=remote_flg,
                        remote_host_url=remote_host_url,
                        artifacts_dir=artifacts_dir,
                        wait_seconds=wait_seconds
                    )

                    self.assertion_manager.set_browser_controller(self.browser_controller)

                    self.browser_controller.access({'url': url})

                    Printer.printer('testcase_name', [testcase['testcase_name']])

                    for process in testcase['process_list']:
                        for process_name, params in process.items():
                            if self.sleep_time:
                                self.browser_controller.sleep({'seconds': self.sleep_time})

                            if Tester.get_process_type(process_name) == 'browser_controller':
                                self.execute_browser_controller_method(process_name, params)
                            else:
                                self.execute_assertioner_method(testsuite['testsuite_name'], testcase['testcase_name'], process_name, params)

                except Exception:
                    Printer.printer('exception', [traceback.format_exc()])

                    self.assertion_manager.add_total_error_count()
                    self.assertion_manager.add_testsuites_error_count()
                    self.assertion_manager.add_testsuite_error_count()
                    self.assertion_manager.set_testcase_result('error')
                    self.assertion_manager.add_testcase_content(traceback.format_exc())
                    self.assertion_manager.add_testcase_results(testcase['testcase_name'], self.timer.get_end_testcase_time())

                    self.browser_controller.screenshot({
                        'file_name': self.testsuites_name + '-' + testsuite['testsuite_name'] + '-' + testcase['testcase_name']
                    })

                    self.browser_controller.close_browser()

                    continue

                self.assertion_manager.add_testcase_results(testcase['testcase_name'], self.timer.get_end_testcase_time())

                self.browser_controller.close_browser()

            self.assertion_manager.add_testsuite_result(testsuite['testsuite_name'], self.timer.get_end_testsuite_time())

        print('')
        Printer.printer('assert_result', [
                self.assertion_manager.get_total_assert_successes(),
                self.assertion_manager.get_total_assert_failures(),
                self.assertion_manager.get_total_assert_errors()
            ]
        )
        print('')

        self.assertion_manager.set_testsuites_result(self.timer.get_end_testsuites_time())

        reporter = Reporter()

        reporter.create_report(self.assertion_manager.get_results(), reports_dir=reports_dir)

        if ci.lower() == 'circleci' and self.assertion_manager.get_total_assert_failures() is not 0:
            sys.exit(1)

    # testsuitesをセット
    def set_testsuites(self, testsuites_name):
        self.testsuites_name = testsuites_name

    # testsuiteを追加
    def add_testsuite(self, testsuite_name):
        self.test_builder.add_testsuite(testsuite_name)

    # testcaseを追加
    def add_testcase(self, testcase_name, testcase):
        self.test_builder.add_testcase(testcase_name, testcase)

    def add_config(self, config_file_path):
        self.test_builder.add_config(config_file_path)

    # processタイプをゲット
    @staticmethod
    def get_process_type(process_name):
        if 'assert' in process_name:
            return 'assert'
        else:
            return 'browser_controller'

    # BrowserControllerのメソッドを実行
    def execute_browser_controller_method(self, process_name, params):
        config = self.test_builder.get_config()

        if 'css' in params:
            if params['css'] in config:
                params['css'] = config[params['css']]

        if self.debug_mode:
            Printer.printer('process', [process_name, params])

        if not params:
            eval('self.browser_controller.' + BrowserControlSetting.get_browser_control(process_name))()
        else:
            eval('self.browser_controller.' + BrowserControlSetting.get_browser_control(process_name))(params)

    # Assertionerのメソッドを実行
    def execute_assertioner_method(self, testsuite_name, testcase_name, process_name, assertion):
        config = self.test_builder.get_config()

        assertion_key = list(assertion.keys())[0]

        params = assertion[assertion_key]

        if 'css' in params:
            if params['css'] in config:
                params['css'] = config[params['css']]

        if self.debug_mode:
            Printer.printer('process', [process_name + ' ' + assertion_key, params])

        self.assertion_manager.assertion(testsuite_name, testcase_name, assertion_key, params)
