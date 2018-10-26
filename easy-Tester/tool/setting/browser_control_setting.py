# -*- coding: utf-8 -*-

# BrowserControlメソッド設定クラス


class BrowserControlSetting:

    browser_control_setting = {
        'access': 'access',

        'close_browser': 'close_browser',
        'close_current_window': 'close_current_window',

        'switch_to_default': 'switch_to_default',
        'switch_window': 'switch_window',

        'open_new_tab': 'open_new_tab',

        'fullscreen': 'fullscreen',

        'dialog_answer': 'dialog_answer',

        'get_element': 'get_element',

        'input': 'input',
        'input_value': 'input_value',
        'input_original_value': 'input_original_value',
        'input_inner_html': 'input_inner_html',

        'click': 'click',

        'mouse_hover': 'mouse_hover',

        'select': 'select',

        'scroll': 'scroll',

        'execute_js': 'execute_js',

        'sleep': 'sleep'
    }

    @staticmethod
    def get_browser_control(browser_control_key):
        return BrowserControlSetting.browser_control_setting[browser_control_key]
