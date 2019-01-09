# -*- coding: utf-8 -*-

# verifyを行うクラス
#
# @param
# browser_controller BrowserControllerインスタンス

import sys
import os
import re

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

from selenium.common.exceptions import TimeoutException

sys.path.append(os.path.join(os.path.dirname(__file__), "../util/"))
from printer import Printer


class Verifier:

    def __init__(self):
        self.browser_controller = ''

    def set_browser_controller(self, browser_controller):
        self.browser_controller = browser_controller

    # 期待値とURLが等しいか
    def verify_url_equals(self, params):
        result_content = ''

        if 'comment' in params:
            result_content += Printer.printer('verify_assert_comment', [params['comment']]) + '\n'

        try:
            self.browser_controller.wait.until(ec.url_to_be(params['expect']))

            Printer.printer('verify_url_equals_success', [params['expect'], self.browser_controller.driver.current_url])
            print('')

            return [True]

        except TimeoutException:
            result_content += Printer.printer('verify_url_equals_failure', [params['expect'], self.browser_controller.driver.current_url]) + '\n\n'
            print('')

            return [False, result_content]

    # 期待値がURLに含まれるか
    def verify_url_contains(self, params):
        result_content = ''

        if 'comment' in params:
            result_content += Printer.printer('verify_assert_comment', [params['comment']]) + '\n'

        try:
            self.browser_controller.wait.until(ec.url_contains(params['expect']))

            Printer.printer('verify_url_contains_success', [params['expect'], self.browser_controller.driver.current_url])
            print('')

            return [True]

        except TimeoutException:
            result_content += Printer.printer('verify_url_contains_failure', [params['expect'], self.browser_controller.driver.current_url]) + '\n\n'
            print('')

            return [False, result_content]

    # 期待値とTitleが等しいか
    def verify_title_equals(self, params):
        result_content = ''

        if 'comment' in params:
            result_content += Printer.printer('verify_assert_comment', [params['comment']]) + '\n'

        try:
            self.browser_controller.wait.until(ec.title_is(params['expect']))

            Printer.printer('verify_title_equals_success', [params['expect'], self.browser_controller.driver.title])
            print('')

            return [True]

        except TimeoutException:
            result_content += Printer.printer('verify_title_equals_failure', [params['expect'], self.browser_controller.driver.title]) + '\n\n'
            print('')

            return [False, result_content]

    # 期待値がTitleに含まれるか
    def verify_title_contains(self, params):
        result_content = ''

        if 'comment' in params:
            result_content += Printer.printer('verify_assert_comment', [params['comment']]) + '\n'

        try:
            self.browser_controller.wait.until(ec.title_contains(params['expect']))

            Printer.printer('verify_title_contains_success', [params['expect'], self.browser_controller.driver.title])
            print('')

            return [True]

        except TimeoutException:
            result_content += Printer.printer('verify_title_contains_failure', [params['expect'], self.browser_controller.driver.title]) + '\n\n'
            print('')

            return [False, result_content]

    # 期待値がInnerHTMLに含まれるか
    def verify_inner_html_contains(self, params):
        result_content = ''

        if 'comment' in params:
            result_content += Printer.printer('verify_assert_comment', [params['comment']]) + '\n'

        self.browser_controller.wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, params['css'])))

        js = 'return document.querySelector(\'' + params['css'] + '\').innerHTML'
        result = self.browser_controller.execute_js({'js': js})

        if params['expect'] in result:
            Printer.printer('verify_inner_html_contains_success', [params['expect'], result])
            print('')

            return [True]

        else:
            result_content += Printer.printer('verify_inner_html_contains_failure', [params['expect'], result]) + '\n\n'
            print('')

            return [False, result_content]

    # 期待値がInnerHTMLに含まれないか
    def verify_inner_html_not_contains(self, params):
        result_content = ''

        if 'comment' in params:
            result_content += Printer.printer('verify_assert_comment', [params['comment']]) + '\n'

        self.browser_controller.wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, params['css'])))

        js = 'return document.querySelector(\'' + params['css'] + '\').innerHTML'
        result = self.browser_controller.execute_js({'js': js})

        if params['expect'] not in result:
            Printer.printer('verify_inner_html_not_contains_success', [params['expect'], result])
            print('')

            return [True]

        else:
            result_content += Printer.printer('verify_inner_html_not_contains_failure', [params['expect'], result]) + '\n\n'
            print('')

            return [False, result_content]

    # 期待値とAttributeが等しいか
    def verify_attribute_equals(self, params):
        result_content = ''

        if 'comment' in params:
            result_content += Printer.printer('verify_assert_comment', [params['comment']]) + '\n'

        self.browser_controller.wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, params['css'])))

        js = 'return document.querySelector(\'' + params['css'] + '\').getAttribute(\'' + params['attr'] + '\');'
        result = self.browser_controller.execute_js({'js': js})

        if params['expect'] == result:
            Printer.printer('verify_attribute_equals_success', [params['expect'], result])
            print('')

            return [True]

        else:
            result_content += Printer.printer('verify_attribute_equals_failure', [params['expect'], result]) + '\n\n'
            print('')

            return [False, result_content]

    # 期待値がAttributeに含まれるか
    def verify_attribute_contains(self, params):
        result_content = ''

        if 'comment' in params:
            result_content += Printer.printer('verify_assert_comment', [params['comment']]) + '\n'

        self.browser_controller.wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, params['css'])))

        js = 'return document.querySelector(\'' + params['css'] + '\').getAttribute(\'' + params['attr'] + '\');'
        result = self.browser_controller.execute_js({'js': js})

        if params['expect'] in result:
            Printer.printer('verify_attribute_contains_success', [params['expect'], result])
            print('')

            return [True]

        else:
            result_content += Printer.printer('verify_attribute_contains_failure', [params['expect'], result]) + '\n\n'
            print('')

            return [False, result_content]

    # 期待値がTextに含まれるか
    def verify_text_contains(self, params):
        result_content = ''

        if 'comment' in params:
            result_content += Printer.printer('verify_assert_comment', [params['comment']]) + '\n'

        try:
            self.browser_controller.wait.until(ec.text_to_be_present_in_element((By.CSS_SELECTOR, params['css']), params['expect']))

            Printer.printer('verify_text_contains_success', [params['expect'], self.browser_controller.get_element(params['css']).text])
            print('')

            return [True]

        except TimeoutException:
            result_content += Printer.printer('verify_text_contains_failure', [params['expect'], self.browser_controller.get_element(params['css']).text]) + '\n\n'
            print('')

            return [False, result_content]

    # 期待値がTextに含まれないか
    def verify_text_not_contains(self, params):
        result_content = ''

        if 'comment' in params:
            result_content += Printer.printer('verify_assert_comment', [params['comment']]) + '\n'

        try:
            self.browser_controller.wait.until(ec.text_to_be_present_in_element((By.CSS_SELECTOR, params['css']), params['expect']))

            result_content += Printer.printer('verify_text_not_contains_failure', [params['expect'], self.browser_controller.get_element(params['css']).text]) + '\n\n'
            print('')

            return [False, result_content]

        except TimeoutException:
            Printer.printer('verify_text_not_contains_success', [params['expect'], self.browser_controller.get_element(params['css']).text])
            print('')

            return [True]

    # ClassNameに期待値が存在するか
    def verify_class_exist(self, params):
        result_content = ''

        if 'comment' in params:
            result_content += Printer.printer('verify_assert_comment', [params['comment']]) + '\n'

        self.browser_controller.wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, params['css'])))

        js = 'return document.querySelector(\'' + params['css'] + '\').className;'
        class_names = self.browser_controller.execute_js({'js': js})

        match_result = False
        for class_name in class_names.split():
            if re.match('^' + params['expect'] + '$', class_name):
                match_result = True

        if match_result:
            Printer.printer('verify_class_exist_success', [params['expect']])
            print('')

            return [True]

        else:
            result_content += Printer.printer('verify_class_exist_failure', [params['expect']]) + '\n\n'
            print('')

            return [False, result_content]

    # ClassNameに期待値が存在しないか
    def verify_class_not_exist(self, params):
        result_content = ''

        if 'comment' in params:
            result_content += Printer.printer('verify_assert_comment', [params['comment']]) + '\n'

        self.browser_controller.wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, params['css'])))

        js = 'return document.querySelector(\'' + params['css'] + '\').className;'
        class_names = self.browser_controller.execute_js({'js': js})

        match_result = True
        for class_name in class_names.split():
            if re.match('^' + params['expect'] + '$', class_name):
                match_result = False

        if match_result:
            Printer.printer('verify_class_not_exist_success', [params['expect']])
            print('')

            return [True]

        else:
            result_content += Printer.printer('verify_class_not_exist_failure', [params['expect']]) + '\n\n'
            print('')

            return [False, result_content]

    # 期待値とCssPropertyが等しいか
    def verify_css_property_equals(self, params):
        result_content = ''

        if 'comment' in params:
            result_content += Printer.printer('verify_assert_comment', [params['comment']]) + '\n'

        self.browser_controller.wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, params['css'])))

        js = 'return document.querySelector(\'' + params['css'] + '\').style.' + params['property'] + ';'
        result = self.browser_controller.execute_js({'js': js})

        if params['expect'] == result:
            Printer.printer('verify_css_property_equals_success', [params['expect'], result])
            print('')

            return [True]

        else:
            result_content += Printer.printer('verify_css_property_equals_failure', [params['expect'], result]) + '\n\n'
            print('')

            return [False, result_content]

    # 特定のElementが存在するか
    def verify_element_exist(self, params):
        result_content = ''

        if 'comment' in params:
            result_content += Printer.printer('verify_assert_comment', [params['comment']]) + '\n'

        try:
            self.browser_controller.wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, params['css'])))

            Printer.printer('verify_element_exist_success', [params['expect']])
            print('')

            return [True]

        except TimeoutException:
            result_content += Printer.printer('verify_element_exist_failure', [params['expect']]) + '\n\n'
            print('')

            return [False, result_content]

    # 特定のElementが存在しないか
    def verify_element_not_exist(self, params):
        result_content = ''

        if 'comment' in params:
            result_content += Printer.printer('verify_assert_comment', [params['comment']]) + '\n'

        try:
            self.browser_controller.wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, params['css'])))

            result_content += Printer.printer('verify_element_not_exist_failure', [params['css']]) + '\n\n'
            print('')

            return [False, result_content]

        except TimeoutException:
            Printer.printer('verify_element_not_exist_success', [params['css']])
            print('')

            return [True]

    # 期待値とValueが等しいか
    def verify_value_equals(self, params):
        result_content = ''

        if 'comment' in params:
            result_content += Printer.printer('verify_assert_comment', [params['comment']]) + '\n'

        try:
            self.browser_controller.wait.until(ec.text_to_be_present_in_element_value((By.CSS_SELECTOR, params['css']), params['expect']))

            result = self.browser_controller.get_element(params['css']).get_attribute('value')

            if params['expect'] == result:
                Printer.printer('verify_value_equals_success', [params['expect'], result])
                print('')

                return [True]

            else:
                raise TimeoutException()

        except TimeoutException:
            result_content += Printer.printer('verify_value_equals_failure', [params['expect'], self.browser_controller.get_element(params['css']).get_attribute('value')]) + '\n\n'
            print('')

            return [False, result_content]

    # 期待値がValueに含まれるか
    def verify_value_contains(self, params):
        result_content = ''

        if 'comment' in params:
            result_content += Printer.printer('verify_assert_comment', [params['comment']]) + '\n'

        try:
            self.browser_controller.wait.until(ec.text_to_be_present_in_element_value((By.CSS_SELECTOR, params['css']), params['expect']))

            Printer.printer('verify_value_contains_success', [params['expect'], self.browser_controller.get_element(params['css']).get_attribute('value')])
            print('')

            return [True]

        except TimeoutException:
            result_content += Printer.printer('verify_value_contains_failure', [params['expect'], self.browser_controller.get_element(params['css']).get_attribute('value')]) + '\n\n'
            print('')

            return [False, result_content]

    # 期待値がValueに含まれないか
    def verify_value_not_contains(self, params):
        result_content = ''

        if 'comment' in params:
            result_content += Printer.printer('verify_assert_comment', [params['comment']]) + '\n'

        try:
            self.browser_controller.wait.until(ec.text_to_be_present_in_element_value((By.CSS_SELECTOR, params['css']), params['expect']))

            result_content += Printer.printer('verify_value_not_contains_failure', [params['expect'], self.browser_controller.get_element(params['css']).get_attribute('value')]) + '\n\n'
            print('')

            return [False, result_content]

        except TimeoutException:
            Printer.printer('verify_value_not_contains_success', [params['expect'], self.browser_controller.get_element(params['css']).get_attribute('value')])
            print('')

            return [True]

    def verify_checked(self, params):
        result_content = ''

        if 'comment' in params:
            result_content += Printer.printer('verify_assert_comment', [params['comment']]) + '\n'

        self.browser_controller.wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, params['css'])))

        js = 'return document.querySelector(\'' + params['css'] + '\').checked;'
        result = self.browser_controller.execute_js({'js': js})

        if result:
            Printer.printer('verify_checked_success', ['True', result])
            print('')

            return [True]

        else:
            result_content += Printer.printer('verify_checked_failure', ['True', result]) + '\n\n'
            print('')

            return [False, result_content]

    def verify_not_checked(self, params):
        result_content = ''

        if 'comment' in params:
            result_content += Printer.printer('verify_assert_comment', [params['comment']]) + '\n'

        self.browser_controller.wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, params['css'])))

        js = 'return document.querySelector(\'' + params['css'] + '\').checked;'
        result = self.browser_controller.execute_js({'js': js})

        if not result:
            Printer.printer('verify_not_checked_success', ['False', result])
            print('')

            return [True]

        else:
            result_content += Printer.printer('verify_not_checked_failure', ['False', result]) + '\n\n'
            print('')

            return [False, result_content]
