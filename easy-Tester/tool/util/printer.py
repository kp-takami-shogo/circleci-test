#coding:utf-8

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "../"))
from print_decoration import PrintDecoration

class Printer:

    print_message = {
        'testcase_name': PrintDecoration.YELLOW + 'Run: {0[0]}' + PrintDecoration.END,

        'exception': PrintDecoration.RED + '{0[0]}' + PrintDecoration.END,

        'process': '   {0[0]}({0[1]})',

        'assert_result': PrintDecoration.GREEN + 'Success: {0[0]}' + PrintDecoration.END + ', ' + PrintDecoration.RED + 'Failure: {0[1]}' + PrintDecoration.END + ', ' + PrintDecoration.RED + 'Error: {0[2]}' + PrintDecoration.END,

        'assert_comment': '   ' + PrintDecoration.UNDERLINE + '{0[0]}' + PrintDecoration.END,

        'assert_url_equals_success': '   ' + PrintDecoration.GREEN + 'Success' + PrintDecoration.END + ' url: ( {0[0]} ) equals ( {0[1]} )',
        'assert_url_equals_failure': '   ' + PrintDecoration.RED + 'Failure' + PrintDecoration.END + ' url: ( {0[0]} ) equals ( {0[1]} )',

        'assert_url_contains_success': '   ' + PrintDecoration.GREEN + 'Success' + PrintDecoration.END + ' url: ( {0[0]} ) contains ( {0[1]} )',
        'assert_url_contains_failure': '   ' + PrintDecoration.RED + 'Failure' + PrintDecoration.END + ' url: ( {0[0]} ) contains ( {0[1]} )',

        'assert_title_equals_success': '   ' + PrintDecoration.GREEN + 'Success' + PrintDecoration.END + ' title: ( {0[0]} ) equals ( {0[1]} )',
        'assert_title_equals_failure': '   ' + PrintDecoration.RED + 'Failure' + PrintDecoration.END + ' title: ( {0[0]} ) equals ( {0[1]} )',

        'assert_title_contains_success': '   ' + PrintDecoration.GREEN + 'Success' + PrintDecoration.END + ' title: ( {0[0]} ) contains ( {0[1]} )',
        'assert_title_contains_failure': '   ' + PrintDecoration.RED + 'Failure' + PrintDecoration.END + ' title: ( {0[0]} ) contains ( {0[1]} )',

        'assert_innerhtml_contains_success': '   ' + PrintDecoration.GREEN + 'Success' + PrintDecoration.END + ' innerHTML: ( {0[0]} ) contains ( {0[1]} )',
        'assert_innerhtml_contains_failure': '   ' + PrintDecoration.RED + 'Failure' + PrintDecoration.END + ' innerHTML: ( {0[0]} ) contains ( {0[1]} )',

        'assert_innerhtml_not_contains_success': '   ' + PrintDecoration.GREEN + 'Success' + PrintDecoration.END + ' innerHTML: ( {0[0]} ) not contains ( {0[1]} )',
        'assert_innerhtml_not_contains_failure': '   ' + PrintDecoration.RED + 'Failure' + PrintDecoration.END + ' innerHTML: ( {0[0]} ) not contains ( {0[1]} )',

        'assert_attribute_equals_success': '   ' + PrintDecoration.GREEN + 'Success' + PrintDecoration.END + ' attribute: ( {0[0]} ) equals ( {0[1]} )',
        'assert_attribute_equals_failure': '   ' + PrintDecoration.RED + 'Failure' + PrintDecoration.END + ' attribute: ( {0[0]} ) equals ( {0[1]} )',

        'assert_attribute_contains_success': '   ' + PrintDecoration.GREEN + 'Success' + PrintDecoration.END + ' attribute: ( {0[0]} ) contains ( {0[1]} )',
        'assert_attribute_contains_failure': '   ' + PrintDecoration.RED + 'Failure' + PrintDecoration.END + ' attribute: ( {0[0]} ) contains ( {0[1]} )',

        'assert_text_contains_success': '   ' + PrintDecoration.GREEN + 'Success' + PrintDecoration.END + ' text: ( {0[0]} ) contains ( {0[1]} )',
        'assert_text_contains_failure': '   ' + PrintDecoration.RED + 'Failure' + PrintDecoration.END + ' text: ( {0[0]} ) contains ( {0[1]} )',

        'assert_text_not_contains_success': '   ' + PrintDecoration.GREEN + 'Success' + PrintDecoration.END + ' text: ( {0[0]} ) not contains ( {0[1]} )',
        'assert_text_not_contains_failure': '   ' + PrintDecoration.RED + 'Failure' + PrintDecoration.END + ' text: ( {0[0]} ) not contains ( {0[1]} )',

        'assert_class_exist_success': '   ' + PrintDecoration.GREEN + 'Success' + PrintDecoration.END + ' class: ( {0[0]} ) exist',
        'assert_class_exist_failure': '   ' + PrintDecoration.RED + 'Failure' + PrintDecoration.END + ' class: ( {0[0]} ) exist',

        'assert_class_not_exist_success': '   ' + PrintDecoration.GREEN + 'Success' + PrintDecoration.END + ' class: ( {0[0]} ) not exist',
        'assert_class_not_exist_failure': '   ' + PrintDecoration.RED + 'Failure' + PrintDecoration.END + ' class: ( {0[0]} ) not exist',

        'assert_css_property_equals_success': '   ' + PrintDecoration.GREEN + 'Success' + PrintDecoration.END + ' css property: ( {0[0]} ) equals ( {0[1]} )',
        'assert_css_property_equals_failure': '   ' + PrintDecoration.RED + 'Failure' + PrintDecoration.END + ' css property: ( {0[0]} ) equals ( {0[1]} )',

        'assert_element_exist_success': '   ' + PrintDecoration.GREEN + 'Success' + PrintDecoration.END + ' element: ( {0[0]} ) exist',
        'assert_element_exist_failure': '   ' + PrintDecoration.RED + 'Failure' + PrintDecoration.END + ' element: ( {0[0]} ) exist',

        'assert_element_not_exist_success': '   ' + PrintDecoration.GREEN + 'Success' + PrintDecoration.END + ' element: ( {0[0]} ) not exist',
        'assert_element_not_exist_failure': '   ' + PrintDecoration.RED + 'Failure' + PrintDecoration.END + ' element: ( {0[0]} ) not exist',

        'assert_value_equals_success': '   ' + PrintDecoration.GREEN + 'Success' + PrintDecoration.END + ' value: ( {0[0]} ) equals ( {0[1]} )',
        'assert_value_equals_failure': '   ' + PrintDecoration.RED + 'Failure' + PrintDecoration.END + ' value: ( {0[0]} ) equals ( {0[1]} )',

        'assert_value_contains_success': '   ' + PrintDecoration.GREEN + 'Success' + PrintDecoration.END + ' value: ( {0[0]} ) contains ( {0[1]} )',
        'assert_value_contains_failure': '   ' + PrintDecoration.RED + 'Failure' + PrintDecoration.END + ' value: ( {0[0]} ) contains ( {0[1]} )',

        'assert_value_not_contains_success': '   ' + PrintDecoration.GREEN + 'Success' + PrintDecoration.END + ' value: ( {0[0]} ) not contains ( {0[1]} )',
        'assert_value_not_contains_failure': '   ' + PrintDecoration.RED + 'Failure' + PrintDecoration.END + ' value: ( {0[0]} ) not contains ( {0[1]} )',
    }

    return_message = {
        'testcase_name': 'Run: {0[0]}',

        'exception': '{0[0]}',

        'process': '{0[0]}({0[1]})',

        'assert_result': 'Success: {0[0]}, Failure: {0[1]}, Error: {0[2]}'  ,

        'assert_comment': '{0[0]}',

        'assert_url_equals_success': 'Success url: ( {0[0]} ) equals ( {0[1]} )',
        'assert_url_equals_failure': 'Failure url: ( {0[0]} ) equals ( {0[1]} )',

        'assert_url_contains_success': 'Success url: ( {0[0]} ) contains ( {0[1]} )',
        'assert_url_contains_failure': 'Failure url: ( {0[0]} ) contains ( {0[1]} )',

        'assert_title_equals_success': 'Success title: ( {0[0]} ) equals ( {0[1]} )',
        'assert_title_equals_failure': 'Failure title: ( {0[0]} ) equals ( {0[1]} )',

        'assert_title_contains_success': 'Success title: ( {0[0]} ) contains ( {0[1]} )',
        'assert_title_contains_failure': 'Failure title: ( {0[0]} ) contains ( {0[1]} )',

        'assert_innerhtml_contains_success': 'Success innerHTML: ( {0[0]} ) contains ( {0[1]} )',
        'assert_innerhtml_contains_failure': 'Failure innerHTML: ( {0[0]} ) contains ( {0[1]} )',

        'assert_innerhtml_not_contains_success': 'Success innerHTML: ( {0[0]} ) not contains ( {0[1]} )',
        'assert_innerhtml_not_contains_failure': 'Failure innerHTML: ( {0[0]} ) not contains ( {0[1]} )',

        'assert_attribute_equals_success': 'Success attribute: ( {0[0]} ) equals ( {0[1]} )',
        'assert_attribute_equals_failure': 'Failure attribute: ( {0[0]} ) equals ( {0[1]} )',

        'assert_attribute_contains_success': 'Success attribute: ( {0[0]} ) contains ( {0[1]} )',
        'assert_attribute_contains_failure': 'Failure attribute: ( {0[0]} ) contains ( {0[1]} )',

        'assert_text_contains_success': 'Success text: ( {0[0]} ) contains ( {0[1]} )',
        'assert_text_contains_failure': 'Failure text: ( {0[0]} ) contains ( {0[1]} )',

        'assert_text_not_contains_success': 'Success text: ( {0[0]} ) not contains ( {0[1]} )',
        'assert_text_not_contains_failure': 'Failure text: ( {0[0]} ) not contains ( {0[1]} )',

        'assert_class_exist_success': 'Success class: ( {0[0]} ) exist',
        'assert_class_exist_failure': 'Failure class: ( {0[0]} ) exist',

        'assert_class_not_exist_success': 'Success class: ( {0[0]} ) not exist',
        'assert_class_not_exist_failure': 'Failure class: ( {0[0]} ) not exist',

        'assert_css_property_equals_success': 'Success css property: ( {0[0]} ) equals ( {0[1]} )',
        'assert_css_property_equals_failure': 'Failure css property: ( {0[0]} ) equals ( {0[1]} )',

        'assert_element_exist_success': 'Success element: ( {0[0]} ) exist',
        'assert_element_exist_failure': 'Failure element: ( {0[0]} ) exist',

        'assert_element_not_exist_success': 'Success element: ( {0[0]} ) not exist',
        'assert_element_not_exist_failure': 'Failure element: ( {0[0]} ) not exist',

        'assert_value_equals_success': 'Success value: ( {0[0]} ) equals ( {0[1]} )',
        'assert_value_equals_failure': 'Failure value: ( {0[0]} ) equals ( {0[1]} )',

        'assert_value_contains_success': 'Success value: ( {0[0]} ) contains ( {0[1]} )',
        'assert_value_contains_failure': 'Failure value: ( {0[0]} ) contains ( {0[1]} )',

        'assert_value_not_contains_success': 'Success value: ( {0[0]} ) not contains ( {0[1]} )',
        'assert_value_not_contains_failure': 'Failure value: ( {0[0]} ) not contains ( {0[1]} )',
    }

    @staticmethod
    def printer(print_type, print_contents):
        print(Printer.print_message[print_type].format(print_contents))
        return Printer.return_message[print_type].format(print_contents)
