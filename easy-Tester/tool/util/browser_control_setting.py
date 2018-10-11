#coding:utf-8

# BrowserControlメソッド設定クラス

class BrowserControlSetting:

    browser_control_setting = {
        'accessUrl': 'accessUrl',

        'closeBrowser': 'closeBrowser',
        'closeCurrentWindow': 'closeCurrentWindow',

        'switchToDefault': 'switchToDefault',
        'switchWindowhandle': 'switchByWindowhandle',
        'switchWindowname': 'switchByWindowname',
        'switchIframe': 'switchByIframe',

        'openNewTab': 'openNewTab',

        'fullscreen': 'fullscreen',

        'dialogAnswer': 'dialogAnswer',

        'getElementCss': 'getElementByCss',

        'inputCss': 'inputByCss',
        'inputValueCss': 'inputValueByCss',
        'inputOriginalValueCss': 'inputOriginalValueByCss',
        'inputInnerHTMLCss': 'inputInnerHTMLByCss',

        'clickCss': 'clickByCss',

        'mouseHoverCss': 'mouseHoverByCss',

        'selectIndex': 'selectByIndex',
        'selectText': 'selectByText',

        'scrollCss': 'scrollByCss',

        'sleepSeconds': 'sleepBySeconds',

        'executeJs': 'executeJs'
    }

    def getBrowserControl(browser_control_key):
        return BrowserControlSetting.browser_control_setting[browser_control_key]
