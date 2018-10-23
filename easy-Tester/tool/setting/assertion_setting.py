# coding:utf-8

# Assertionメソッド設定クラス


class AssertionSetting:

    assert_setting = {
        'urlEqual': 'assert_url_equals',
        'urlContain': 'assert_url_contains',

        'titleEqual': 'assert_title_equals',
        'titleContain': 'assert_title_contains',

        'innerHTMLContain': 'assert_inner_html_contains',
        'innerHTMLNotContain': 'assert_inner_html_not_contains',

        'attributeEqual': 'assert_attribute_equals',
        'attributeContain': 'assert_attribute_contains',

        'textContain': 'assert_text_contains',
        'textNotContain': 'assert_text_not_contains',

        'classExist': 'assert_class_exist',
        'classNotExist': 'assert_class_not_exist',

        'cssPropertyEqual': 'assert_css_property_equals',

        'elementExist': 'assert_element_exist',
        'elementNotExist': 'assert_element_not_exist',

        'valueEqual': 'assert_value_equals',
        'valueContain': 'assert_value_contains',
        'valueNotContain': 'assert_value_not_contains'
    }

    @staticmethod
    def get_assertion(assertion_key):
        return AssertionSetting.assert_setting[assertion_key]
