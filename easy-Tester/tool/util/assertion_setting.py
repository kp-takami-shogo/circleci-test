#coding:utf-8

# Assertionメソッド設定クラス

class AssertionSetting:

    assert_setting = {
        'urlEqual': 'assertUrlEquals',
        'urlContain': 'assertUrlContains',

        'titleEqual': 'assertTitleEquals',
        'titleContain': 'assertTitleContains',

        'innerHTMLContain': 'assertInnerHTMLContains',
        'innerHTMLNotContain': 'assertInnerHTMLNotContains',

        'attributeEqual': 'assertAttributeEquals',
        'attributeContain': 'assertAttributeContains',

        'textContain': 'assertTextContains',
        'textNotContain': 'assertTextNotContains',

        'classExist': 'assertClassExist',
        'classNotExist': 'assertClassNotExist',

        'cssPropertyEqual': 'assertCssPropertyEquals',

        'elementExist': 'assertElementExist',
        'elementNotExist': 'assertElementNotExist',

        'valueEqual': 'assertValueEquals',
        'valueContain': 'assertValueContains',
        'valueNotContain': 'assertValueNotContains'
    }

    def getAssertion(assertion_key):
        return AssertionSetting.assert_setting[assertion_key]
