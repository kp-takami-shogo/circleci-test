# -*- coding: utf-8 -*-

# Assertionメソッド設定クラス


class AssertionSetting:

    assert_setting = {
        'url_equal': 'assert_url_equals',
        'url_contain': 'assert_url_contains',

        'title_equal': 'assert_title_equals',
        'title_contain': 'assert_title_contains',

        'inner_html_contain': 'assert_inner_html_contains',
        'inner_html_not_contain': 'assert_inner_html_not_contains',

        'attribute_equal': 'assert_attribute_equals',
        'attribute_contain': 'assert_attribute_contains',

        'text_contain': 'assert_text_contains',
        'text_not_contain': 'assert_text_not_contains',

        'class_exist': 'assert_class_exist',
        'class_not_exist': 'assert_class_not_exist',

        'css_property_equal': 'assert_css_property_equals',

        'element_exist': 'assert_element_exist',
        'element_not_exist': 'assert_element_not_exist',

        'value_equal': 'assert_value_equals',
        'value_contain': 'assert_value_contains',
        'value_not_contain': 'assert_value_not_contains'
    }

    @staticmethod
    def get_assertion(assertion_key):
        return AssertionSetting.assert_setting[assertion_key]
