# coding:utf-8

# BrowserControlメソッド設定クラス


class BrowserControlSetting:

    browser_control_setting = {
        'accessUrl': 'access_url',

        'closeBrowser': 'close_browser',
        'closeCurrentWindow': 'close_current_window',

        'switchToDefault': 'switch_to_default',
        'switchWindowhandle': 'switch_by_window_handle',
        'switchWindowname': 'switch_by_window_name',
        'switchFrame': 'switch_by_frame',

        'openNewTab': 'open_new_tab',

        'fullscreen': 'fullscreen',

        'dialogAnswer': 'dialog_answer',

        'getElementCss': 'get_element_by_css',

        'inputCss': 'input_by_css',
        'inputValueCss': 'input_value_by_css',
        'inputOriginalValueCss': 'input_original_value_by_css',
        'inputInnerHTMLCss': 'input_inner_html_by_css',

        'clickCss': 'click_by_css',

        'mouseHoverCss': 'mouse_hover_by_css',

        'selectIndex': 'select_by_index',
        'selectText': 'select_by_text',

        'scrollCss': 'scroll_by_css',

        'executeJs': 'execute_js',

        'sleepSeconds': 'sleep_by_seconds'
    }

    @staticmethod
    def get_browser_control(browser_control_key):
        return BrowserControlSetting.browser_control_setting[browser_control_key]
