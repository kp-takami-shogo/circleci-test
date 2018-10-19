# coding:utf-8

# アサーションを行うクラス
#
# @param
# browser_controller BrowserControllerインスタンス

import sys
import os
import re

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

from selenium.common.exceptions import TimeoutException

sys.path.append(os.path.join(os.path.dirname(__file__), "../util/"))
from printer import Printer


class Assertioner:

    def __init__(self):
        self.browser_controller = ''

    def set_browser_controller(self, browser_controller):
        self.browser_controller = browser_controller

    # 期待値とURLが等しいか
    def assert_url_equals(self, param_list):
        WebDriverWait(self.browser_controller.driver, self.browser_controller.wait_seconds).until(
            ec.url_to_be(param_list[0]))
        result = self.browser_controller.driver.current_url

        try:
            assert param_list[0] == result

            if len(param_list) > 1:
                Printer.printer('assert_comment', [param_list[1]])

            Printer.printer('assert_url_equals_success', [param_list[0], result])
            print('')

            return [True]

        except AssertionError:
            result_content = ''

            if len(param_list) > 1:
                result_content += Printer.printer('assert_comment', [param_list[1]]) + '\n'

            result_content += Printer.printer('assert_url_equals_failure', [param_list[0], result]) + '\n\n'
            print('')

            return [False, result_content]

    # 期待値がURLに含まれるか
    def assert_url_contains(self, param_list):
        WebDriverWait(self.browser_controller.driver, self.browser_controller.wait_seconds).until(
            ec.url_contains(param_list[0]))
        result = self.browser_controller.driver.current_url

        try:
            assert param_list[0] in result

            if len(param_list) > 1:
                Printer.printer('assert_comment', [param_list[1]])

            Printer.printer('assert_url_contains_success', [param_list[0], result])
            print('')

            return [True]

        except AssertionError:
            result_content = ''

            if len(param_list) > 1:
                result_content += Printer.printer('assert_comment', [param_list[1]]) + '\n'

            result_content += Printer.printer('assert_url_contains_failure', [param_list[0], result]) + '\n\n'
            print('')

            return [False, result_content]

    # 期待値とTitleが等しいか
    def assert_title_equals(self, param_list):
        WebDriverWait(self.browser_controller.driver, self.browser_controller.wait_seconds).until(
            ec.title_is(param_list[0]))
        result = self.browser_controller.driver.title

        try:
            assert param_list[0] == result

            if len(param_list) > 1:
                Printer.printer('assert_comment', [param_list[1]])

            Printer.printer('assert_title_equals_success', [param_list[0], result])
            print('')

            return [True]

        except AssertionError:
            result_content = ''

            if len(param_list) > 1:
                result_content += Printer.printer('assert_comment', [param_list[1]]) + '\n'

            result_content += Printer.printer('assert_title_equals_failure', [param_list[0], result]) + '\n\n'
            print('')

            return [False, result_content]

    # 期待値がTitleに含まれるか
    def assert_title_contains(self, param_list):
        WebDriverWait(self.browser_controller.driver, self.browser_controller.wait_seconds).until(
            ec.title_contains(param_list[0]))
        result = self.browser_controller.driver.title

        try:
            assert param_list[0] in result

            if len(param_list) > 1:
                Printer.printer('assert_comment', [param_list[1]])

            Printer.printer('assert_title_contains_success', [param_list[0], result])
            print('')

            return [True]

        except AssertionError:
            result_content = ''

            if len(param_list) > 1:
                result_content += Printer.printer('assert_comment', [param_list[1]]) + '\n'

            result_content += Printer.printer('assert_title_contains_failure', [param_list[0], result]) + '\n\n'
            print('')

            return [False, result_content]

    # 期待値がInnerHTMLに含まれるか
    def assert_inner_html_contains(self, param_list):
        WebDriverWait(self.browser_controller.driver, self.browser_controller.wait_seconds).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, param_list[0])))
        js = 'return document.querySelector(\'' + param_list[0] + '\').innerHTML'
        result = self.browser_controller.execute_js([js])

        try:
            assert param_list[1] in result

            if len(param_list) > 2:
                Printer.printer('assert_comment', [param_list[2]])

            Printer.printer('assert_innerhtml_contains_success', [param_list[1], result])
            print('')

            return [True]

        except AssertionError:
            result_content = ''

            if len(param_list) > 2:
                result_content += Printer.printer('assert_comment', [param_list[2]]) + '\n'

            result_content += Printer.printer('assert_innerhtml_contains_failure', [param_list[1], result]) + '\n\n'
            print('')

            return [False, result_content]

    # 期待値がInnerHTMLに含まれないか
    def assert_inner_html_not_contains(self, param_list):
        WebDriverWait(self.browser_controller.driver, self.browser_controller.wait_seconds).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, param_list[0])))
        js = 'return document.querySelector(\'' + param_list[0] + '\').innerHTML'
        result = self.browser_controller.execute_js([js])

        try:
            assert param_list[1] not in result

            if len(param_list) > 2:
                Printer.printer('assert_comment', [param_list[2]])

            Printer.printer('assert_innerhtml_not_contains_success', [param_list[1], result])
            print('')

            return [True]

        except AssertionError:
            result_content = ''

            if len(param_list) > 2:
                result_content += Printer.printer('assert_comment', [param_list[2]]) + '\n'

            result_content += Printer.printer('assert_innerhtml_not_contains_failure', [param_list[1], result]) + '\n\n'
            print('')

            return [False, result_content]

    # 期待値とAttributeが等しいか
    def assert_attribute_equals(self, param_list):
        WebDriverWait(self.browser_controller.driver, self.browser_controller.wait_seconds).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, param_list[0])))
        js = 'return document.querySelector(\'' + param_list[0] + '\').getAttribute(\'' + param_list[1] + '\');'
        result = self.browser_controller.execute_js([js])

        try:
            assert param_list[2] == result

            if len(param_list) > 3:
                Printer.printer('assert_comment', [param_list[3]])

            Printer.printer('assert_attribute_equals_success', [param_list[2], result])
            print('')

            return [True]

        except AssertionError:
            result_content = ''

            if len(param_list) > 3:
                result_content += Printer.printer('assert_comment', [param_list[3]]) + '\n'

            result_content += Printer.printer('assert_attribute_equals_failure', [param_list[2], result]) + '\n\n'
            print('')

            return [False, result_content]

    # 期待値がAttributeに含まれるか
    def assert_attribute_contains(self, param_list):
        WebDriverWait(self.browser_controller.driver, self.browser_controller.wait_seconds).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, param_list[0])))
        js = 'return document.querySelector(\'' + param_list[0] + '\').getAttribute(\'' + param_list[1] + '\');'
        result = self.browser_controller.execute_js([js])

        try:
            assert param_list[2] in result

            if len(param_list) > 3:
                Printer.printer('assert_comment', [param_list[3]])

            Printer.printer('assert_attribute_contains_success', [param_list[2], result])
            print('')

            return [True]

        except AssertionError:
            result_content = ''

            if len(param_list) > 3:
                result_content += Printer.printer('assert_comment', [param_list[3]]) + '\n'

            result_content += Printer.printer('assert_attribute_contains_failure', [param_list[2], result]) + '\n\n'
            print('')

            return [False, result_content]

    # 期待値がTextに含まれるか
    def assert_text_contains(self, param_list):
        try:
            WebDriverWait(self.browser_controller.driver, self.browser_controller.wait_seconds).until(
                ec.text_to_be_present_in_element((By.CSS_SELECTOR, param_list[0]), param_list[1]))
            js = 'return document.querySelector(\'' + param_list[0] + '\').textContent;'
            result = self.browser_controller.execute_js([js])

            assert param_list[1] in result

            if len(param_list) > 2:
                Printer.printer('assert_comment', [param_list[2]])

            Printer.printer('assert_text_contains_success', [param_list[1], result])
            print('')

            return [True]

        except TimeoutException:
            js = 'return document.querySelector(\'' + param_list[0] + '\').textContent;'
            result = self.browser_controller.execute_js([js])

            result_content = ''

            if len(param_list) > 2:
                result_content += Printer.printer('assert_comment', [param_list[2]]) + '\n'

            result_content += Printer.printer('assert_text_contains_failure', [param_list[1], result]) + '\n\n'
            print('')

            return [False, result_content]

        except AssertionError:
            result_content = ''

            if len(param_list) > 2:
                result_content += Printer.printer('assert_comment', [param_list[2]]) + '\n'

            result_content += Printer.printer('assert_text_contains_failure', [param_list[1], result]) + '\n\n'
            print('')

            return [False, result_content]

    # 期待値がTextに含まれないか
    def assert_text_not_contains(self, param_list):
        try:
            WebDriverWait(self.browser_controller.driver, self.browser_controller.wait_seconds).until(
                ec.presence_of_element_located((By.CSS_SELECTOR, param_list[0])))
            js = 'return document.querySelector(\'' + param_list[0] + '\').textContent;'
            result = self.browser_controller.execute_js([js])

            assert param_list[1] not in result

            if len(param_list) > 2:
                Printer.printer('assert_comment', [param_list[2]])

            Printer.printer('assert_text_not_contains_success', [param_list[1], result])
            print('')

            return [True]

        except TimeoutException:
            js = 'return document.querySelector(\'' + param_list[0] + '\').textContent;'
            result = self.browser_controller.execute_js([js])

            if len(param_list) > 2:
                Printer.printer('assert_comment', [param_list[2]])

            Printer.printer('assert_text_not_contains_success', [param_list[1], result])
            print('')

            return [True]

        except AssertionError:
            result_content = ''

            if len(param_list) > 2:
                result_content += Printer.printer('assert_comment', [param_list[2]]) + '\n'

            result_content += Printer.printer('assert_text_not_contains_failure', [param_list[1], result]) + '\n\n'
            print('')

            return [False, result_content]

    # ClassNameに期待値が存在するか
    def assert_class_exist(self, param_list):
        WebDriverWait(self.browser_controller.driver, self.browser_controller.wait_seconds).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, param_list[0])))
        js = 'return document.querySelector(\'' + param_list[0] + '\').className;'
        class_names = self.browser_controller.execute_js([js])

        try:
            match_result = False
            for class_name in class_names.split():
                if re.match('^' + param_list[1] + '$', class_name):
                    match_result = True

            assert match_result

            if len(param_list) > 2:
                Printer.printer('assert_comment', [param_list[2]])

            Printer.printer('assert_class_exist_success', [param_list[1]])
            print('')

            return [True]

        except AssertionError:
            result_content = ''

            if len(param_list) > 2:
                result_content += Printer.printer('assert_comment', [param_list[2]]) + '\n'

            result_content += Printer.printer('assert_class_exist_failure', [param_list[1]]) + '\n\n'
            print('')

            return [False, result_content]

    # ClassNameに期待値が存在しないか
    def assert_class_not_exist(self, param_list):
        WebDriverWait(self.browser_controller.driver, self.browser_controller.wait_seconds).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, param_list[0])))
        js = 'return document.querySelector(\'' + param_list[0] + '\').className;'
        class_names = self.browser_controller.execute_js([js])

        try:
            match_result = True
            for class_name in class_names.split():
                if re.match('^' + param_list[1] + '$', class_name):
                    match_result = False

            assert match_result

            if len(param_list) > 2:
                Printer.printer('assert_comment', [param_list[2]])

            Printer.printer('assert_class_not_exist_success', [param_list[1]])
            print('')

            return [True]

        except AssertionError:
            result_content = ''

            if len(param_list) > 2:
                result_content += Printer.printer('assert_comment', [param_list[2]]) + '\n'

            result_content += Printer.printer('assert_class_not_exist_failure', [param_list[1]]) + '\n\n'
            print('')

            return [False, result_content]

    # 期待値とCssPropertyが等しいか
    def assert_css_property_equals(self, param_list):
        WebDriverWait(self.browser_controller.driver, self.browser_controller.wait_seconds).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, param_list[0])))
        js = 'return document.querySelector(\'' + param_list[0] + '\').style.' + param_list[1] + ';'
        result = self.browser_controller.execute_js([js])

        try:
            assert param_list[2] == result

            if len(param_list) > 3:
                Printer.printer('assert_comment', [param_list[3]])

            Printer.printer('assert_css_property_equals_success', [param_list[2], result])
            print('')

            return [True]

        except AssertionError:
            result_content = ''

            if len(param_list) > 3:
                result_content += Printer.printer('assert_comment', [param_list[3]]) + '\n'

            result_content += Printer.printer('assert_css_property_equals_failure', [param_list[2], result]) + '\n\n'
            print('')

            return [False, result_content]

    # 特定のElementが存在するか
    def assert_element_exist(self, param_list):
        try:
            WebDriverWait(self.browser_controller.driver, self.browser_controller.wait_seconds).until(
                ec.presence_of_element_located((By.CSS_SELECTOR, param_list[0])))
            js = 'return document.querySelector(\'' + param_list[0] + '\');'
            result = self.browser_controller.execute_js([js])

            assert result is not None

            if len(param_list) > 1:
                Printer.printer('assert_comment', [param_list[1]])

            Printer.printer('assert_element_exist_success', [param_list[0]])
            print('')

            return [True]

        except TimeoutException:
            result_content = ''

            if len(param_list) > 1:
                result_content += Printer.printer('assert_comment', [param_list[1]]) + '\n'

            result_content += Printer.printer('assert_element_exist_failure', [param_list[0]]) + '\n\n'
            print('')

            return [False, result_content]

        except AssertionError:
            result_content = ''

            if len(param_list) > 1:
                result_content += Printer.printer('assert_comment', [param_list[1]]) + '\n'

            result_content += Printer.printer('assert_element_exist_failure', [param_list[0]]) + '\n\n'
            print('')

            return [False, result_content]

    # 特定のElementが存在しないか
    def assert_element_not_exist(self, param_list):
        try:
            WebDriverWait(self.browser_controller.driver, self.browser_controller.wait_seconds).until(
                ec.invisibility_of_element_located((By.CSS_SELECTOR, param_list[0])))
            js = 'return document.querySelector(\'' + param_list[0] + '\');'
            result = self.browser_controller.execute_js([js])

            assert result is None

            if len(param_list) > 1:
                Printer.printer('assert_comment', [param_list[1]])

            Printer.printer('assert_element_not_exist_success', [param_list[0]])
            print('')

            return [True]

        except TimeoutException:
            result_content = ''

            if len(param_list) > 1:
                result_content += Printer.printer('assert_comment', [param_list[1]]) + '\n'

            result_content += Printer.printer('assert_element_not_exist_failure', [param_list[0]]) + '\n\n'
            print('')

            return [False, result_content]

        except AssertionError:
            result_content = ''

            if len(param_list) > 1:
                result_content += Printer.printer('assert_comment', [param_list[1]]) + '\n'

            result_content += Printer.printer('assert_element_not_exist_failure', [param_list[0]]) + '\n\n'
            print('')

            return [False, result_content]

    # 期待値とValueが等しいか
    def assert_value_equals(self, param_list):
        WebDriverWait(self.browser_controller.driver, self.browser_controller.wait_seconds).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, param_list[0])))
        js = 'return document.querySelector(\'' + param_list[0] + '\').value;'
        result = self.browser_controller.execute_js([js])

        try:
            assert param_list[1] == result

            if len(param_list) > 2:
                Printer.printer('assert_comment', [param_list[2]])

            Printer.printer('assert_value_equals_success', [param_list[1], result])
            print('')

            return [True]

        except AssertionError:
            result_content = ''

            if len(param_list) > 2:
                result_content += Printer.printer('assert_comment', [param_list[2]]) + '\n'

            result_content += Printer.printer('assert_value_equals_failure', [param_list[1], result]) + '\n\n'
            print('')

            return [False, result_content]

    # 期待値がValueに含まれるか
    def assert_value_contains(self, param_list):
        WebDriverWait(self.browser_controller.driver, self.browser_controller.wait_seconds).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, param_list[0])))
        js = 'return document.querySelector(\'' + param_list[0] + '\').value;'
        result = self.browser_controller.execute_js([js])

        try:
            assert param_list[1] in result

            if len(param_list) > 2:
                Printer.printer('assert_comment', [param_list[2]])

            Printer.printer('assert_value_contains_success', [param_list[1], result])
            print('')

            return [True]

        except AssertionError:
            result_content = ''

            if len(param_list) > 2:
                result_content += Printer.printer('assert_comment', [param_list[2]]) + '\n'

            result_content += Printer.printer('assert_value_contains_failure', [param_list[1], result]) + '\n\n'
            print('')

            return [False, result_content]

    # 期待値がValueに含まれないか
    def assert_value_not_contains(self, param_list):
        WebDriverWait(self.browser_controller.driver, self.browser_controller.wait_seconds).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, param_list[0])))
        js = 'return document.querySelector(\'' + param_list[0] + '\').value;'
        result = self.browser_controller.execute_js([js])

        try:
            assert param_list[1] not in result

            if len(param_list) > 2:
                Printer.printer('assert_comment', [param_list[2]])

            Printer.printer('assert_value_not_contains_success', [param_list[1], result])
            print('')

            return [True]

        except AssertionError:
            result_content = ''

            if len(param_list) > 2:
                result_content += Printer.printer('assert_comment', [param_list[2]]) + '\n'

            result_content += Printer.printer('assert_value_not_contains_failure', [param_list[1], result]) + '\n\n'
            print('')

            return [False, result_content]
