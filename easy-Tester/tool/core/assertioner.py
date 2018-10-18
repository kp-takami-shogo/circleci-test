#coding:utf-8

# アサーションを行うクラス
#
# @param
# browser_controller BrowserControllerインスタンス

import sys
import os
import re
from pprint import pprint

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium.common.exceptions import TimeoutException

sys.path.append(os.path.join(os.path.dirname(__file__), "../util/"))
from printer import Printer

class Assertioner:

    def __init__(self):
        self.browser_controller = ''


    def setBrowserController(self, browser_controller):
        self.browser_controller = browser_controller


    # 期待値とURLが等しいか
    def assertUrlEquals(self, param_list):
        WebDriverWait(self.browser_controller.driver, self.browser_controller.wait_seconds).until(EC.url_to_be(param_list[0]))
        result = self.browser_controller.driver.current_url

        try:
            assert param_list[0] == result

            if (len(param_list) > 1):
                Printer.printer('assert_comment', [param_list[1]])

            Printer.printer('assert_url_equals_success', [param_list[0], result])
            print('')

            return [True]

        except AssertionError as e:
            result_content = ''

            if (len(param_list) > 1):
                result_content += Printer.printer('assert_comment', [param_list[1]]) + '\n'

            result_content += Printer.printer('assert_url_equals_failure', [param_list[0], result]) + '\n\n'
            print('')

            return [False, result_content]

    # 期待値がURLに含まれるか
    def assertUrlContains(self, param_list):
        WebDriverWait(self.browser_controller.driver, self.browser_controller.wait_seconds).until(EC.url_contains(param_list[0]))
        result = self.browser_controller.driver.current_url

        try:
            assert param_list[0] in result

            if (len(param_list) > 1):
                Printer.printer('assert_comment', [param_list[1]])

            Printer.printer('assert_url_contains_success', [param_list[0], result])
            print('')

            return [True]

        except AssertionError as e:
            result_content = ''

            if (len(param_list) > 1):
                result_content += Printer.printer('assert_comment', [param_list[1]]) + '\n'

            result_content += Printer.printer('assert_url_contains_failure', [param_list[0], result]) + '\n\n'
            print('')

            return [False, result_content]


    # 期待値とTitleが等しいか
    def assertTitleEquals(self, param_list):
        WebDriverWait(self.browser_controller.driver, self.browser_controller.wait_seconds).until(EC.title_is(param_list[0]))
        result = self.browser_controller.driver.title

        try:
            assert param_list[0] == result

            if (len(param_list) > 1):
                Printer.printer('assert_comment', [param_list[1]])

            Printer.printer('assert_title_equals_success', [param_list[0], result])
            print('')

            return [True]

        except AssertionError as e:
            result_content = ''

            if (len(param_list) > 1):
                result_content += Printer.printer('assert_comment', [param_list[1]]) + '\n'

            result_content += Printer.printer('assert_title_equals_failure', [param_list[0], result]) + '\n\n'
            print('')

            return [False, result_content]

    # 期待値がTitleに含まれるか
    def assertTitleContains(self, param_list):
        WebDriverWait(self.browser_controller.driver, self.browser_controller.wait_seconds).until(EC.title_contains(param_list[0]))
        result = self.browser_controller.driver.title

        try:
            assert param_list[0] in result

            if (len(param_list) > 1):
                Printer.printer('assert_comment', [param_list[1]])

            Printer.printer('assert_title_contains_success', [param_list[0], result])
            print('')

            return [True]

        except AssertionError as e:
            result_content = ''

            if (len(param_list) > 1):
                result_content += Printer.printer('assert_comment', [param_list[1]]) + '\n'

            result_content += Printer.printer('assert_title_contains_failure', [param_list[0], result]) + '\n\n'
            print('')

            return [False, result_content]

    # 期待値がInnerHTMLに含まれるか
    def assertInnerHTMLContains(self, param_list):
        WebDriverWait(self.browser_controller.driver, self.browser_controller.wait_seconds).until(EC.presence_of_element_located((By.CSS_SELECTOR, param_list[0])))
        js = 'return document.querySelector(\'' + param_list[0] + '\').innerHTML'
        result = self.browser_controller.executeJs([js])

        try:
            assert param_list[1] in result

            if (len(param_list) > 2):
                Printer.printer('assert_comment', [param_list[2]])

            Printer.printer('assert_innerhtml_contains_success', [param_list[1], result])
            print('')

            return [True]

        except AssertionError as e:
            result_content = ''

            if (len(param_list) > 2):
                result_content += Printer.printer('assert_comment', [param_list[2]]) + '\n'

            result_content += Printer.printer('assert_innerhtml_contains_failure', [param_list[1], result]) + '\n\n'
            print('')

            return [False, result_content]

    # 期待値がInnerHTMLに含まれないか
    def assertInnerHTMLNotContains(self, param_list):
        WebDriverWait(self.browser_controller.driver, self.browser_controller.wait_seconds).until(EC.presence_of_element_located((By.CSS_SELECTOR, param_list[0])))
        js = 'return document.querySelector(\'' + param_list[0] + '\').innerHTML'
        result = self.browser_controller.executeJs([js])

        try:
            assert param_list[1] not in result

            if (len(param_list) > 2):
                Printer.printer('assert_comment', [param_list[2]])

            Printer.printer('assert_innerhtml_not_contains_success', [param_list[1], result])
            print('')

            return [True]

        except AssertionError as e:
            result_content = ''

            if (len(param_list) > 2):
                result_content += Printer.printer('assert_comment', [param_list[2]]) + '\n'

            result_content += Printer.printer('assert_innerhtml_not_contains_failure', [param_list[1], result]) + '\n\n'
            print('')

            return [False, result_content]



    # 期待値とAttributeが等しいか
    def assertAttributeEquals(self, param_list):
        WebDriverWait(self.browser_controller.driver, self.browser_controller.wait_seconds).until(EC.presence_of_element_located((By.CSS_SELECTOR, param_list[0])))
        js = 'return document.querySelector(\'' + param_list[0] + '\').getAttribute(\'' + param_list[1] + '\');'
        result = self.browser_controller.executeJs([js])

        try:
            assert param_list[2] == result

            if (len(param_list) > 3):
                Printer.printer('assert_comment', [param_list[3]])

            Printer.printer('assert_attribute_equals_success', [param_list[2], result])
            print('')

            return [True]

        except AssertionError as e:
            result_content = ''

            if (len(param_list) > 3):
                result_content += Printer.printer('assert_comment', [param_list[3]]) + '\n'

            result_content += Printer.printer('assert_attribute_equals_failure', [param_list[2], result]) + '\n\n'
            print('')

            return [False, result_content]

    # 期待値がAttributeに含まれるか
    def assertAttributeContains(self, param_list):
        WebDriverWait(self.browser_controller.driver, self.browser_controller.wait_seconds).until(EC.presence_of_element_located((By.CSS_SELECTOR, param_list[0])))
        js = 'return document.querySelector(\'' + param_list[0] + '\').getAttribute(\'' + param_list[1] + '\');'
        result = self.browser_controller.executeJs([js])

        try:
            assert param_list[2] in result

            if (len(param_list) > 3):
                Printer.printer('assert_comment', [param_list[3]])

            Printer.printer('assert_attribute_contains_success', [param_list[2], result])
            print('')

            return [True]

        except AssertionError as e:
            result_content = ''

            if (len(param_list) > 3):
                result_content += Printer.printer('assert_comment', [param_list[3]]) + '\n'

            result_content += Printer.printer('assert_attribute_contains_failure', [param_list[2], result]) + '\n\n'
            print('')

            return [False, result_content]


    # 期待値がTextに含まれるか
    def assertTextContains(self, param_list):
        try:
            WebDriverWait(self.browser_controller.driver, self.browser_controller.wait_seconds).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, param_list[0]), param_list[1]))
            js = 'return document.querySelector(\'' + param_list[0] + '\').textContent;'
            result = self.browser_controller.executeJs([js])

            assert param_list[1] in result

            if (len(param_list) > 2):
                Printer.printer('assert_comment', [param_list[2]])

            Printer.printer('assert_text_contains_success', [param_list[1], result])
            print('')

            return [True]

        except TimeoutException as e:
            js = 'return document.querySelector(\'' + param_list[0] + '\').textContent;'
            result = self.browser_controller.executeJs([js])

            result_content = ''

            if (len(param_list) > 2):
                result_content += Printer.printer('assert_comment', [param_list[2]]) + '\n'

            result_content += Printer.printer('assert_text_contains_failure', [param_list[1], result]) + '\n\n'
            print('')

            return [False, result_content]

        except AssertionError as e:
            result_content = ''

            if (len(param_list) > 2):
                result_content += Printer.printer('assert_comment', [param_list[2]]) + '\n'

            result_content += Printer.printer('assert_text_contains_failure', [param_list[1], result]) + '\n\n'
            print('')

            return [False, result_content]

    # 期待値がTextに含まれないか
    def assertTextNotContains(self, param_list):
        try:
            WebDriverWait(self.browser_controller.driver, self.browser_controller.wait_seconds).until(EC.presence_of_element_located((By.CSS_SELECTOR, param_list[0])))
            js = 'return document.querySelector(\'' + param_list[0] + '\').textContent;'
            result = self.browser_controller.executeJs([js])

            assert param_list[1] not in result

            if (len(param_list) > 2):
                Printer.printer('assert_comment', [param_list[2]])

            Printer.printer('assert_text_not_contains_success', [param_list[1], result])
            print('')

            return [True]

        except TimeoutException as e:
            js = 'return document.querySelector(\'' + param_list[0] + '\').textContent;'
            result = self.browser_controller.executeJs([js])

            if (len(param_list) > 2):
                Printer.printer('assert_comment', [param_list[2]])

            Printer.printer('assert_text_not_contains_success', [param_list[1], result])
            print('')

            return [True]

        except AssertionError as e:
            result_content = ''

            if (len(param_list) > 2):
                result_content += Printer.printer('assert_comment', [param_list[2]]) + '\n'

            result_content += Printer.printer('assert_text_not_contains_failure', [param_list[1], result]) + '\n\n'
            print('')

            return [False, result_content]


    # ClassNameに期待値が存在するか
    def assertClassExist(self, param_list):
        WebDriverWait(self.browser_controller.driver, self.browser_controller.wait_seconds).until(EC.presence_of_element_located((By.CSS_SELECTOR, param_list[0])))
        js = 'return document.querySelector(\'' + param_list[0] + '\').className;'
        class_names = self.browser_controller.executeJs([js])

        try:
            match_result = False
            for class_name in class_names.split():
                if re.match('^' + param_list[1] + '$', class_name):
                    match_result = True

            assert match_result

            if (len(param_list) > 2):
                Printer.printer('assert_comment', [param_list[2]])

            Printer.printer('assert_class_exist_success', [param_list[1]])
            print('')

            return [True]

        except AssertionError as e:
            result_content = ''

            if (len(param_list) > 2):
                result_content += Printer.printer('assert_comment', [param_list[2]]) + '\n'

            result_content += Printer.printer('assert_class_exist_failure', [param_list[1]]) + '\n\n'
            print('')

            return [False, result_content]

    # ClassNameに期待値が存在しないか
    def assertClassNotExist(self, param_list):
        WebDriverWait(self.browser_controller.driver, self.browser_controller.wait_seconds).until(EC.presence_of_element_located((By.CSS_SELECTOR, param_list[0])))
        js = 'return document.querySelector(\'' + param_list[0] + '\').className;'
        class_names = self.browser_controller.executeJs([js])

        try:
            match_result = True
            for class_name in class_names.split():
                if re.match('^' + param_list[1] + '$', class_name):
                    match_result = False

            assert match_result

            if (len(param_list) > 2):
                Printer.printer('assert_comment', [param_list[2]])

            Printer.printer('assert_class_not_exist_success', [param_list[1]])
            print('')

            return [True]

        except AssertionError as e:
            result_content = ''

            if (len(param_list) > 2):
                result_content += Printer.printer('assert_comment', [param_list[2]]) + '\n'

            result_content += Printer.printer('assert_class_not_exist_failure', [param_list[1]]) + '\n\n'
            print('')

            return [False, result_content]


    # 期待値とCssPropertyが等しいか
    def assertCssPropertyEquals(self, param_list):
        WebDriverWait(self.browser_controller.driver, self.browser_controller.wait_seconds).until(EC.presence_of_element_located((By.CSS_SELECTOR, param_list[0])))
        js = 'return document.querySelector(\'' + param_list[0] + '\').style.' + param_list[1] + ';'
        result = self.browser_controller.executeJs([js])

        try:
            assert param_list[2] == result

            if (len(param_list) > 3):
                Printer.printer('assert_comment', [param_list[3]])

            Printer.printer('assert_css_property_equals_success', [param_list[2], result])
            print('')

            return [True]

        except AssertionError as e:
            result_content = ''

            if (len(param_list) > 3):
                result_content += Printer.printer('assert_comment', [param_list[3]]) + '\n'

            result_content += Printer.printer('assert_css_property_equals_failure', [param_list[2], result]) + '\n\n'
            print('')

            return [False, result_content]


    # 特定のElementが存在するか
    def assertElementExist(self, param_list):
        try:
            WebDriverWait(self.browser_controller.driver, self.browser_controller.wait_seconds).until(EC.presence_of_element_located((By.CSS_SELECTOR, param_list[0])))
            js = 'return document.querySelector(\'' + param_list[0] + '\');'
            result = self.browser_controller.executeJs([js])

            assert result != None

            if (len(param_list) > 1):
                Printer.printer('assert_comment', [param_list[1]])

            Printer.printer('assert_element_exist_success', [param_list[0]])
            print('')

            return [True]

        except TimeoutException as e:
            js = 'return document.querySelector(\'' + param_list[0] + '\');'
            result = self.browser_controller.executeJs([js])

            result_content = ''

            if (len(param_list) > 1):
                result_content += Printer.printer('assert_comment', [param_list[1]]) + '\n'

            result_content += Printer.printer('assert_element_exist_failure', [param_list[0]]) + '\n\n'
            print('')

            return [False, result_content]

        except AssertionError as e:
            result_content = ''

            if (len(param_list) > 1):
                result_content += Printer.printer('assert_comment', [param_list[1]]) + '\n'

            result_content += Printer.printer('assert_element_exist_failure', [param_list[0]]) + '\n\n'
            print('')

            return [False, result_content]

    # 特定のElementが存在しないか
    def assertElementNotExist(self, param_list):
        try:
            WebDriverWait(self.browser_controller.driver, self.browser_controller.wait_seconds).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, param_list[0])))
            js = 'return document.querySelector(\'' + param_list[0] + '\');'
            result = self.browser_controller.executeJs([js])

            assert result == None

            if (len(param_list) > 1):
                Printer.printer('assert_comment', [param_list[1]])

            Printer.printer('assert_element_not_exist_success', [param_list[0]])
            print('')

            return [True]

        except TimeoutException as e:
            js = 'return document.querySelector(\'' + param_list[0] + '\');'
            result = self.browser_controller.executeJs([js])

            result_content = ''

            if (len(param_list) > 1):
                result_content += Printer.printer('assert_comment', [param_list[1]]) + '\n'

            result_content += Printer.printer('assert_element_not_exist_failure', [param_list[0]]) + '\n\n'
            print('')

            return [False, result_content]

        except AssertionError as e:
            result_content = ''

            if (len(param_list) > 1):
                result_content += Printer.printer('assert_comment', [param_list[1]]) + '\n'

            result_content += Printer.printer('assert_element_not_exist_failure', [param_list[0]]) + '\n\n'
            print('')

            return [False, result_content]


    # 期待値とValueが等しいか
    def assertValueEquals(self, param_list):
        WebDriverWait(self.browser_controller.driver, self.browser_controller.wait_seconds).until(EC.presence_of_element_located((By.CSS_SELECTOR, param_list[0])))
        js = 'return document.querySelector(\'' + param_list[0] + '\').value;'
        result = self.browser_controller.executeJs([js])

        try:
            assert param_list[1] == result

            if (len(param_list) > 2):
                Printer.printer('assert_comment', [param_list[2]])

            Printer.printer('assert_value_equals_success', [param_list[1], result])
            print('')

            return [True]

        except AssertionError as e:
            result_content = ''

            if (len(param_list) > 2):
                result_content += Printer.printer('assert_comment', [param_list[2]]) + '\n'

            result_content += Printer.printer('assert_value_equals_failure', [param_list[1], result]) + '\n\n'
            print('')

            return [False, result_content]

    # 期待値がValueに含まれるか
    def assertValueContains(self, param_list):
        WebDriverWait(self.browser_controller.driver, self.browser_controller.wait_seconds).until(EC.presence_of_element_located((By.CSS_SELECTOR, param_list[0])))
        js = 'return document.querySelector(\'' + param_list[0] + '\').value;'
        result = self.browser_controller.executeJs([js])

        try:
            assert param_list[1] in result

            if (len(param_list) > 2):
                Printer.printer('assert_comment', [param_list[2]])

            Printer.printer('assert_value_contains_success', [param_list[1], result])
            print('')

            return [True]

        except AssertionError as e:
            result_content = ''

            if (len(param_list) > 2):
                result_content += Printer.printer('assert_comment', [param_list[2]]) + '\n'

            result_content += Printer.printer('assert_value_contains_failure', [param_list[1], result]) + '\n\n'
            print('')

            return [False, result_content]

    # 期待値がValueに含まれないか
    def assertValueNotContains(self, param_list):
        WebDriverWait(self.browser_controller.driver, self.browser_controller.wait_seconds).until(EC.presence_of_element_located((By.CSS_SELECTOR, param_list[0])))
        js = 'return document.querySelector(\'' + param_list[0] + '\').value;'
        result = self.browser_controller.executeJs([js])

        try:
            assert param_list[1] not in result

            if (len(param_list) > 2):
                Printer.printer('assert_comment', [param_list[2]])

            Printer.printer('assert_value_not_contains_success', [param_list[1], result])
            print('')

            return [True]

        except AssertionError as e:
            result_content = ''

            if (len(param_list) > 2):
                result_content += Printer.printer('assert_comment', [param_list[2]]) + '\n'

            result_content += Printer.printer('assert_value_not_contains_failure', [param_list[1], result]) + '\n\n'
            print('')

            return [False, result_content]
