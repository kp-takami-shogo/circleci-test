# -*- coding: utf-8 -*-

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "../"))
from print_decoration import PrintDecoration


class Printer:
    print_message = {
        'testsuite_name': PrintDecoration.BOLD + '{0[0]}' + PrintDecoration.END,

        'testcase_name': '   ' + PrintDecoration.YELLOW + 'Run: {0[0]}' + PrintDecoration.END,

        'exception': PrintDecoration.RED + '{0[0]}' + PrintDecoration.END,

        'process': '      {0[0]}({0[1]})',

        'verify_assert_result': PrintDecoration.GREEN + 'Success: {0[0]}' + PrintDecoration.END + ', ' + PrintDecoration.RED + 'Failure: {0[1]}' + PrintDecoration.END + ', ' + PrintDecoration.RED + 'Error: {0[2]}' + PrintDecoration.END,

        'verify_assert_comment': '      ' + PrintDecoration.UNDERLINE + '{0[0]}' + PrintDecoration.END,

        'verify_url_equals_success': '      Verify ' + PrintDecoration.GREEN + 'Success' + PrintDecoration.END + ' url: ( {0[0]} ) equals ( {0[1]} )',
        'verify_url_equals_failure': '      Verify ' + PrintDecoration.RED + 'Failure' + PrintDecoration.END + ' url: ( {0[0]} ) equals ( {0[1]} )',

        'verify_url_contains_success': '      Verify ' + PrintDecoration.GREEN + 'Success' + PrintDecoration.END + ' url: ( {0[0]} ) contains ( {0[1]} )',
        'verify_url_contains_failure': '      Verify ' + PrintDecoration.RED + 'Failure' + PrintDecoration.END + ' url: ( {0[0]} ) contains ( {0[1]} )',

        'verify_title_equals_success': '      Verify ' + PrintDecoration.GREEN + 'Success' + PrintDecoration.END + ' title: ( {0[0]} ) equals ( {0[1]} )',
        'verify_title_equals_failure': '      Verify ' + PrintDecoration.RED + 'Failure' + PrintDecoration.END + ' title: ( {0[0]} ) equals ( {0[1]} )',

        'verify_title_contains_success': '      Verify ' + PrintDecoration.GREEN + 'Success' + PrintDecoration.END + ' title: ( {0[0]} ) contains ( {0[1]} )',
        'verify_title_contains_failure': '      Verify ' + PrintDecoration.RED + 'Failure' + PrintDecoration.END + ' title: ( {0[0]} ) contains ( {0[1]} )',

        'verify_inner_html_contains_success': '      Verify ' + PrintDecoration.GREEN + 'Success' + PrintDecoration.END + ' innerHTML: ( {0[0]} ) contains ( {0[1]} )',
        'verify_inner_html_contains_failure': '      Verify ' + PrintDecoration.RED + 'Failure' + PrintDecoration.END + ' innerHTML: ( {0[0]} ) contains ( {0[1]} )',

        'verify_inner_html_not_contains_success': '      Verify ' + PrintDecoration.GREEN + 'Success' + PrintDecoration.END + ' innerHTML: ( {0[0]} ) not contains ( {0[1]} )',
        'verify_inner_html_not_contains_failure': '      Verify ' + PrintDecoration.RED + 'Failure' + PrintDecoration.END + ' innerHTML: ( {0[0]} ) not contains ( {0[1]} )',

        'verify_attribute_equals_success': '      Verify ' + PrintDecoration.GREEN + 'Success' + PrintDecoration.END + ' attribute: ( {0[0]} ) equals ( {0[1]} )',
        'verify_attribute_equals_failure': '      Verify ' + PrintDecoration.RED + 'Failure' + PrintDecoration.END + ' attribute: ( {0[0]} ) equals ( {0[1]} )',

        'verify_attribute_contains_success': '      Verify ' + PrintDecoration.GREEN + 'Success' + PrintDecoration.END + ' attribute: ( {0[0]} ) contains ( {0[1]} )',
        'verify_attribute_contains_failure': '      Verify ' + PrintDecoration.RED + 'Failure' + PrintDecoration.END + ' attribute: ( {0[0]} ) contains ( {0[1]} )',

        'verify_text_contains_success': '      Verify ' + PrintDecoration.GREEN + 'Success' + PrintDecoration.END + ' text: ( {0[0]} ) contains ( {0[1]} )',
        'verify_text_contains_failure': '      Verify ' + PrintDecoration.RED + 'Failure' + PrintDecoration.END + ' text: ( {0[0]} ) contains ( {0[1]} )',

        'verify_text_not_contains_success': '      Verify ' + PrintDecoration.GREEN + 'Success' + PrintDecoration.END + ' text: ( {0[0]} ) not contains ( {0[1]} )',
        'verify_text_not_contains_failure': '      Verify ' + PrintDecoration.RED + 'Failure' + PrintDecoration.END + ' text: ( {0[0]} ) not contains ( {0[1]} )',

        'verify_class_exist_success': '      Verify ' + PrintDecoration.GREEN + 'Success' + PrintDecoration.END + ' class: ( {0[0]} ) exist',
        'verify_class_exist_failure': '      Verify ' + PrintDecoration.RED + 'Failure' + PrintDecoration.END + ' class: ( {0[0]} ) exist',

        'verify_class_not_exist_success': '      Verify ' + PrintDecoration.GREEN + 'Success' + PrintDecoration.END + ' class: ( {0[0]} ) not exist',
        'verify_class_not_exist_failure': '      Verify ' + PrintDecoration.RED + 'Failure' + PrintDecoration.END + ' class: ( {0[0]} ) not exist',

        'verify_css_property_equals_success': '      Verify ' + PrintDecoration.GREEN + 'Success' + PrintDecoration.END + ' css property: ( {0[0]} ) equals ( {0[1]} )',
        'verify_css_property_equals_failure': '      Verify ' + PrintDecoration.RED + 'Failure' + PrintDecoration.END + ' css property: ( {0[0]} ) equals ( {0[1]} )',

        'verify_element_exist_success': '      Verify ' + PrintDecoration.GREEN + 'Success' + PrintDecoration.END + ' element: ( {0[0]} ) exist',
        'verify_element_exist_failure': '      Verify ' + PrintDecoration.RED + 'Failure' + PrintDecoration.END + ' element: ( {0[0]} ) exist',

        'verify_element_not_exist_success': '      Verify ' + PrintDecoration.GREEN + 'Success' + PrintDecoration.END + ' element: ( {0[0]} ) not exist',
        'verify_element_not_exist_failure': '      Verify ' + PrintDecoration.RED + 'Failure' + PrintDecoration.END + ' element: ( {0[0]} ) not exist',

        'verify_value_equals_success': '      Verify ' + PrintDecoration.GREEN + 'Success' + PrintDecoration.END + ' value: ( {0[0]} ) equals ( {0[1]} )',
        'verify_value_equals_failure': '      Verify ' + PrintDecoration.RED + 'Failure' + PrintDecoration.END + ' value: ( {0[0]} ) equals ( {0[1]} )',

        'verify_value_contains_success': '      Verify ' + PrintDecoration.GREEN + 'Success' + PrintDecoration.END + ' value: ( {0[0]} ) contains ( {0[1]} )',
        'verify_value_contains_failure': '      Verify ' + PrintDecoration.RED + 'Failure' + PrintDecoration.END + ' value: ( {0[0]} ) contains ( {0[1]} )',

        'verify_value_not_contains_success': '      Verify ' + PrintDecoration.GREEN + 'Success' + PrintDecoration.END + ' value: ( {0[0]} ) not contains ( {0[1]} )',
        'verify_value_not_contains_failure': '      Verify ' + PrintDecoration.RED + 'Failure' + PrintDecoration.END + ' value: ( {0[0]} ) not contains ( {0[1]} )',

        'assert_url_equals_success': '      Assert ' + PrintDecoration.GREEN + 'Success' + PrintDecoration.END + ' url: ( {0[0]} ) equals ( {0[1]} )',
        'assert_url_equals_failure': '      Assert ' + PrintDecoration.RED + 'Failure' + PrintDecoration.END + ' url: ( {0[0]} ) equals ( {0[1]} )',

        'assert_url_contains_success': '      Assert ' + PrintDecoration.GREEN + 'Success' + PrintDecoration.END + ' url: ( {0[0]} ) contains ( {0[1]} )',
        'assert_url_contains_failure': '      Assert ' + PrintDecoration.RED + 'Failure' + PrintDecoration.END + ' url: ( {0[0]} ) contains ( {0[1]} )',

        'assert_title_equals_success': '      Assert ' + PrintDecoration.GREEN + 'Success' + PrintDecoration.END + ' title: ( {0[0]} ) equals ( {0[1]} )',
        'assert_title_equals_failure': '      Assert ' + PrintDecoration.RED + 'Failure' + PrintDecoration.END + ' title: ( {0[0]} ) equals ( {0[1]} )',

        'assert_title_contains_success': '      Assert ' + PrintDecoration.GREEN + 'Success' + PrintDecoration.END + ' title: ( {0[0]} ) contains ( {0[1]} )',
        'assert_title_contains_failure': '      Assert ' + PrintDecoration.RED + 'Failure' + PrintDecoration.END + ' title: ( {0[0]} ) contains ( {0[1]} )',

        'assert_inner_html_contains_success': '      Assert ' + PrintDecoration.GREEN + 'Success' + PrintDecoration.END + ' innerHTML: ( {0[0]} ) contains ( {0[1]} )',
        'assert_inner_html_contains_failure': '      Assert ' + PrintDecoration.RED + 'Failure' + PrintDecoration.END + ' innerHTML: ( {0[0]} ) contains ( {0[1]} )',

        'assert_inner_html_not_contains_success': '      Assert ' + PrintDecoration.GREEN + 'Success' + PrintDecoration.END + ' innerHTML: ( {0[0]} ) not contains ( {0[1]} )',
        'assert_inner_html_not_contains_failure': '      Assert ' + PrintDecoration.RED + 'Failure' + PrintDecoration.END + ' innerHTML: ( {0[0]} ) not contains ( {0[1]} )',

        'assert_attribute_equals_success': '      Assert ' + PrintDecoration.GREEN + 'Success' + PrintDecoration.END + ' attribute: ( {0[0]} ) equals ( {0[1]} )',
        'assert_attribute_equals_failure': '      Assert ' + PrintDecoration.RED + 'Failure' + PrintDecoration.END + ' attribute: ( {0[0]} ) equals ( {0[1]} )',

        'assert_attribute_contains_success': '      Assert ' + PrintDecoration.GREEN + 'Success' + PrintDecoration.END + ' attribute: ( {0[0]} ) contains ( {0[1]} )',
        'assert_attribute_contains_failure': '      Assert ' + PrintDecoration.RED + 'Failure' + PrintDecoration.END + ' attribute: ( {0[0]} ) contains ( {0[1]} )',

        'assert_text_contains_success': '      Assert ' + PrintDecoration.GREEN + 'Success' + PrintDecoration.END + ' text: ( {0[0]} ) contains ( {0[1]} )',
        'assert_text_contains_failure': '      Assert ' + PrintDecoration.RED + 'Failure' + PrintDecoration.END + ' text: ( {0[0]} ) contains ( {0[1]} )',

        'assert_text_not_contains_success': '      Assert ' + PrintDecoration.GREEN + 'Success' + PrintDecoration.END + ' text: ( {0[0]} ) not contains ( {0[1]} )',
        'assert_text_not_contains_failure': '      Assert ' + PrintDecoration.RED + 'Failure' + PrintDecoration.END + ' text: ( {0[0]} ) not contains ( {0[1]} )',

        'assert_class_exist_success': '      Assert ' + PrintDecoration.GREEN + 'Success' + PrintDecoration.END + ' class: ( {0[0]} ) exist',
        'assert_class_exist_failure': '      Assert ' + PrintDecoration.RED + 'Failure' + PrintDecoration.END + ' class: ( {0[0]} ) exist',

        'assert_class_not_exist_success': '      Assert ' + PrintDecoration.GREEN + 'Success' + PrintDecoration.END + ' class: ( {0[0]} ) not exist',
        'assert_class_not_exist_failure': '      Assert ' + PrintDecoration.RED + 'Failure' + PrintDecoration.END + ' class: ( {0[0]} ) not exist',

        'assert_css_property_equals_success': '      Assert ' + PrintDecoration.GREEN + 'Success' + PrintDecoration.END + ' css property: ( {0[0]} ) equals ( {0[1]} )',
        'assert_css_property_equals_failure': '      Assert ' + PrintDecoration.RED + 'Failure' + PrintDecoration.END + ' css property: ( {0[0]} ) equals ( {0[1]} )',

        'assert_element_exist_success': '      Assert ' + PrintDecoration.GREEN + 'Success' + PrintDecoration.END + ' element: ( {0[0]} ) exist',
        'assert_element_exist_failure': '      Assert ' + PrintDecoration.RED + 'Failure' + PrintDecoration.END + ' element: ( {0[0]} ) exist',

        'assert_element_not_exist_success': '      Assert ' + PrintDecoration.GREEN + 'Success' + PrintDecoration.END + ' element: ( {0[0]} ) not exist',
        'assert_element_not_exist_failure': '      Assert ' + PrintDecoration.RED + 'Failure' + PrintDecoration.END + ' element: ( {0[0]} ) not exist',

        'assert_value_equals_success': '      Assert ' + PrintDecoration.GREEN + 'Success' + PrintDecoration.END + ' value: ( {0[0]} ) equals ( {0[1]} )',
        'assert_value_equals_failure': '      Assert ' + PrintDecoration.RED + 'Failure' + PrintDecoration.END + ' value: ( {0[0]} ) equals ( {0[1]} )',

        'assert_value_contains_success': '      Assert ' + PrintDecoration.GREEN + 'Success' + PrintDecoration.END + ' value: ( {0[0]} ) contains ( {0[1]} )',
        'assert_value_contains_failure': '      Assert ' + PrintDecoration.RED + 'Failure' + PrintDecoration.END + ' value: ( {0[0]} ) contains ( {0[1]} )',

        'assert_value_not_contains_success': '      Assert ' + PrintDecoration.GREEN + 'Success' + PrintDecoration.END + ' value: ( {0[0]} ) not contains ( {0[1]} )',
        'assert_value_not_contains_failure': '      Assert ' + PrintDecoration.RED + 'Failure' + PrintDecoration.END + ' value: ( {0[0]} ) not contains ( {0[1]} )',
    }

    return_message = {
        'testsuite_name': '{0[0]}',

        'testcase_name': 'Run: {0[0]}',

        'exception': '{0[0]}',

        'process': '{0[0]}({0[1]})',

        'verify_assert_result': 'Success: {0[0]}, Failure: {0[1]}, Error: {0[2]}',

        'verify_assert_comment': '{0[0]}',

        'verify_url_equals_success': 'Verify Success url: ( {0[0]} ) equals ( {0[1]} )',
        'verify_url_equals_failure': 'Verify Failure url: ( {0[0]} ) equals ( {0[1]} )',

        'verify_url_contains_success': 'Verify Success url: ( {0[0]} ) contains ( {0[1]} )',
        'verify_url_contains_failure': 'Verify Failure url: ( {0[0]} ) contains ( {0[1]} )',

        'verify_title_equals_success': 'Verify Success title: ( {0[0]} ) equals ( {0[1]} )',
        'verify_title_equals_failure': 'Verify Failure title: ( {0[0]} ) equals ( {0[1]} )',

        'verify_title_contains_success': 'Verify Success title: ( {0[0]} ) contains ( {0[1]} )',
        'verify_title_contains_failure': 'Verify Failure title: ( {0[0]} ) contains ( {0[1]} )',

        'verify_inner_html_contains_success': 'Verify Success innerHTML: ( {0[0]} ) contains ( {0[1]} )',
        'verify_inner_html_contains_failure': 'Verify Failure innerHTML: ( {0[0]} ) contains ( {0[1]} )',

        'verify_inner_html_not_contains_success': 'Verify Success innerHTML: ( {0[0]} ) not contains ( {0[1]} )',
        'verify_inner_html_not_contains_failure': 'Verify Failure innerHTML: ( {0[0]} ) not contains ( {0[1]} )',

        'verify_attribute_equals_success': 'Verify Success attribute: ( {0[0]} ) equals ( {0[1]} )',
        'verify_attribute_equals_failure': 'Verify Failure attribute: ( {0[0]} ) equals ( {0[1]} )',

        'verify_attribute_contains_success': 'Verify Success attribute: ( {0[0]} ) contains ( {0[1]} )',
        'verify_attribute_contains_failure': 'Verify Failure attribute: ( {0[0]} ) contains ( {0[1]} )',

        'verify_text_contains_success': 'Verify Success text: ( {0[0]} ) contains ( {0[1]} )',
        'verify_text_contains_failure': 'Verify Failure text: ( {0[0]} ) contains ( {0[1]} )',

        'verify_text_not_contains_success': 'Verify Success text: ( {0[0]} ) not contains ( {0[1]} )',
        'verify_text_not_contains_failure': 'Verify Failure text: ( {0[0]} ) not contains ( {0[1]} )',

        'verify_class_exist_success': 'Verify Success class: ( {0[0]} ) exist',
        'verify_class_exist_failure': 'Verify Failure class: ( {0[0]} ) exist',

        'verify_class_not_exist_success': 'Verify Success class: ( {0[0]} ) not exist',
        'verify_class_not_exist_failure': 'Verify Failure class: ( {0[0]} ) not exist',

        'verify_css_property_equals_success': 'Verify Success css property: ( {0[0]} ) equals ( {0[1]} )',
        'verify_css_property_equals_failure': 'Verify Failure css property: ( {0[0]} ) equals ( {0[1]} )',

        'verify_element_exist_success': 'Verify Success element: ( {0[0]} ) exist',
        'verify_element_exist_failure': 'Verify Failure element: ( {0[0]} ) exist',

        'verify_element_not_exist_success': 'Verify Success element: ( {0[0]} ) not exist',
        'verify_element_not_exist_failure': 'Verify Failure element: ( {0[0]} ) not exist',

        'verify_value_equals_success': 'Verify Success value: ( {0[0]} ) equals ( {0[1]} )',
        'verify_value_equals_failure': 'Verify Failure value: ( {0[0]} ) equals ( {0[1]} )',

        'verify_value_contains_success': 'Verify Success value: ( {0[0]} ) contains ( {0[1]} )',
        'verify_value_contains_failure': 'Verify Failure value: ( {0[0]} ) contains ( {0[1]} )',

        'verify_value_not_contains_success': 'Verify Success value: ( {0[0]} ) not contains ( {0[1]} )',
        'verify_value_not_contains_failure': 'Verify Failure value: ( {0[0]} ) not contains ( {0[1]} )',

        'assert_url_equals_success': 'Assert Success url: ( {0[0]} ) equals ( {0[1]} )',
        'assert_url_equals_failure': 'Assert Failure url: ( {0[0]} ) equals ( {0[1]} )',

        'assert_url_contains_success': 'Assert Success url: ( {0[0]} ) contains ( {0[1]} )',
        'assert_url_contains_failure': 'Assert Failure url: ( {0[0]} ) contains ( {0[1]} )',

        'assert_title_equals_success': 'Assert Success title: ( {0[0]} ) equals ( {0[1]} )',
        'assert_title_equals_failure': 'Assert Failure title: ( {0[0]} ) equals ( {0[1]} )',

        'assert_title_contains_success': 'Assert Success title: ( {0[0]} ) contains ( {0[1]} )',
        'assert_title_contains_failure': 'Assert Failure title: ( {0[0]} ) contains ( {0[1]} )',

        'assert_inner_html_contains_success': 'Assert Success innerHTML: ( {0[0]} ) contains ( {0[1]} )',
        'assert_inner_html_contains_failure': 'Assert Failure innerHTML: ( {0[0]} ) contains ( {0[1]} )',

        'assert_inner_html_not_contains_success': 'Assert Success innerHTML: ( {0[0]} ) not contains ( {0[1]} )',
        'assert_inner_html_not_contains_failure': 'Assert Failure innerHTML: ( {0[0]} ) not contains ( {0[1]} )',

        'assert_attribute_equals_success': 'Assert Success attribute: ( {0[0]} ) equals ( {0[1]} )',
        'assert_attribute_equals_failure': 'Assert Failure attribute: ( {0[0]} ) equals ( {0[1]} )',

        'assert_attribute_contains_success': 'Assert Success attribute: ( {0[0]} ) contains ( {0[1]} )',
        'assert_attribute_contains_failure': 'Assert Failure attribute: ( {0[0]} ) contains ( {0[1]} )',

        'assert_text_contains_success': 'Assert Success text: ( {0[0]} ) contains ( {0[1]} )',
        'assert_text_contains_failure': 'Assert Failure text: ( {0[0]} ) contains ( {0[1]} )',

        'assert_text_not_contains_success': 'Assert Success text: ( {0[0]} ) not contains ( {0[1]} )',
        'assert_text_not_contains_failure': 'Assert Failure text: ( {0[0]} ) not contains ( {0[1]} )',

        'assert_class_exist_success': 'Assert Success class: ( {0[0]} ) exist',
        'assert_class_exist_failure': 'Assert Failure class: ( {0[0]} ) exist',

        'assert_class_not_exist_success': 'Assert Success class: ( {0[0]} ) not exist',
        'assert_class_not_exist_failure': 'Assert Failure class: ( {0[0]} ) not exist',

        'assert_css_property_equals_success': 'Assert Success css property: ( {0[0]} ) equals ( {0[1]} )',
        'assert_css_property_equals_failure': 'Assert Failure css property: ( {0[0]} ) equals ( {0[1]} )',

        'assert_element_exist_success': 'Assert Success element: ( {0[0]} ) exist',
        'assert_element_exist_failure': 'Assert Failure element: ( {0[0]} ) exist',

        'assert_element_not_exist_success': 'Assert Success element: ( {0[0]} ) not exist',
        'assert_element_not_exist_failure': 'Assert Failure element: ( {0[0]} ) not exist',

        'assert_value_equals_success': 'Assert Success value: ( {0[0]} ) equals ( {0[1]} )',
        'assert_value_equals_failure': 'Assert Failure value: ( {0[0]} ) equals ( {0[1]} )',

        'assert_value_contains_success': 'Assert Success value: ( {0[0]} ) contains ( {0[1]} )',
        'assert_value_contains_failure': 'Assert Failure value: ( {0[0]} ) contains ( {0[1]} )',

        'assert_value_not_contains_success': 'Assert Success value: ( {0[0]} ) not contains ( {0[1]} )',
        'assert_value_not_contains_failure': 'Assert Failure value: ( {0[0]} ) not contains ( {0[1]} )',
    }

    @staticmethod
    def printer(print_type, print_contents):
        print(Printer.print_message[print_type].format(print_contents))
        return Printer.return_message[print_type].format(print_contents)
