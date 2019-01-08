# -*- coding: utf-8 -*-

# Verifierメソッド設定クラス


class VerifySetting:

    verify_setting = {
        'url_equal': 'verify_url_equals',
        'url_contain': 'verify_url_contains',

        'title_equal': 'verify_title_equals',
        'title_contain': 'verify_title_contains',

        'inner_html_contain': 'verify_inner_html_contains',
        'inner_html_not_contain': 'verify_inner_html_not_contains',

        'attribute_equal': 'verify_attribute_equals',
        'attribute_contain': 'verify_attribute_contains',

        'text_contain': 'verify_text_contains',
        'text_not_contain': 'verify_text_not_contains',

        'class_exist': 'verify_class_exist',
        'class_not_exist': 'verify_class_not_exist',

        'css_property_equal': 'verify_css_property_equals',

        'element_exist': 'verify_element_exist',
        'element_not_exist': 'verify_element_not_exist',

        'value_equal': 'verify_value_equals',
        'value_contain': 'verify_value_contains',
        'value_not_contain': 'verify_value_not_contains'
    }

    @staticmethod
    def get_verify(verify_key):
        return VerifySetting.verify_setting[verify_key]
