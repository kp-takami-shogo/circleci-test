# -*- coding: utf-8 -*-

# ブラウザ操作を行うクラス
#
# @param
# browser 使用ブラウザ名
# driver webdriverインスタンス
# action_chains ActionChainsインスタンス

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

from time import sleep


# from PIL import Image


class BrowserController:

    # 初期化 & ブラウザ起動
    def __init__(self, *, browser='', driver_path='',
                 remote_flg=0, remote_host_url='', artifacts_path='', wait_seconds=5):

        self.browser = browser

        if self.browser.lower() == 'chrome':
            if remote_flg:
                self.driver = webdriver.Remote(
                    command_executor=remote_host_url,
                    desired_capabilities=DesiredCapabilities.CHROME
                )
            else:
                self.driver = webdriver.Chrome()
        elif self.browser.lower() == 'firefox':
            self.driver = webdriver.Firefox(driver_path)
        elif self.browser.lower() == 'safari':
            self.driver = webdriver.Safari(driver_path)
            self.fullscreen()
            self.switch_window({'window_handle': '0'})

        self.action_chains = ActionChains(self.driver)
        self.alert = Alert(self.driver)

        self.artifacts_path = artifacts_path

        self.wait = WebDriverWait(self.driver, wait_seconds)
        self.driver.implicitly_wait(wait_seconds)

        self.temp = {}

    # URLにアクセス
    def access(self, params):
        self.driver.get(params['url'])

    # ブラウザを閉じる
    def close_browser(self):
        self.driver.quit()

    # 現在のウィンドウを閉じる
    def close_current_window(self):
        self.driver.close()

    # 別ウィンドウに切り替える
    def switch_window(self, params):
        if 'window_handle' in params:
            self._switch_by_window_handle(params['window_handle'])
        elif 'window_name' in params:
            self._switch_by_window_name(params['window_name'])
        elif 'frame' in params:
            self._switch_by_frame(params['frame'])

    # handleによって（0から開いた順にhandleが格納される）
    def _switch_by_window_handle(self, window_handle):
        self.driver.switch_to.window(self.driver.window_handles[int(window_handle)])

    # nameによって
    def _switch_by_window_name(self, window_name):
        self.driver.switch_to.window(window_name)

    # 特定frameに切り替える
    def _switch_by_frame(self, frame):
        self.driver.switch_to.frame(self.get_element(frame))

    # 切り替えたwindowやframeを元の方に戻す
    def switch_to_default(self):
        self.driver.switch_to.default_content()

    # 新規タブを開く
    def open_new_tab(self):
        js = "window.open();"
        self.execute_js({'js': js})

    # ブラウザを最大化する
    # Mac
    def fullscreen(self):
        self.driver.maximize_window()

    # スクリーンショット
    def screenshot(self, params):
        self.driver.get_screenshot_as_file(self.artifacts_path + params['file_name'] + '.png')

    # # スクリーンショットを撮る
    # def screenshotByFilename(self, param_list):
    #     sleep(5)
    #     if self.browser == 'Chrome' or self.browser == 'Firefox':
    #         if len(param_list) > 0:
    #             self.fullScreenShot('./screenshot/' + self.browser + '-' + str(datetime.now()) + '-' + str(param_list[0]) + '.png')
    #         else:
    #             self.fullScreenShot('./screenshot/' + self.browser + '-' + str(datetime.now()) + '.png')
    #     else:
    #         if len(param_list) > 0:
    #             self.driver.get_screenshot_as_file("./screenshot/" + self.browser + "-" + str(datetime.now()) + "-" + str(param_list[0]) + ".png")
    #         else:
    #             self.driver.get_screenshot_as_file("./screenshot/" + self.browser + "-" + str(datetime.now()) + ".png")
    #
    # # フルスクリーンショットを撮る
    # #（ブラウザによってSeleniumのget_screenshot_as_file()ではフルスクリーンショットが出来ないため）
    # def fullScreenShot(self, file_path):
    #     self.executeJs(["window.scrollTo(0, 0);"])
    #
    #     total_height = self.executeJs(["return document.body.scrollHeight"])
    #     total_width = self.executeJs(["return document.body.scrollWidth"])
    #
    #     view_height = self.executeJs(["return window.innerHeight"])
    #     view_width = self.executeJs(["return window.innerWidth"])
    #
    #     stitched_image = Image.new("RGB", (total_width, total_height))
    #
    #     scroll_height = 0
    #     scroll_width = 0
    #
    #     row_count = 0
    #
    #     while scroll_height < total_height:
    #         col_count = 0
    #         scroll_width = 0
    #         self.executeJs(["window.scrollTo(%d, %d)" % (scroll_width, scroll_height)])
    #
    #         while scroll_width < total_width:
    #
    #             if col_count > 0:
    #                 self.executeJs(["window.scrollBy("+ str(view_width) +", 0)"])
    #
    #             tmpname = './screenshot/tmp_%d_%d.png' % (row_count, col_count)
    #             self.driver.get_screenshot_as_file(tmpname)
    #             sleep(3)
    #
    #             if scroll_width + view_width >= total_width or scroll_height + view_height >= total_height:
    #                 new_height = view_height
    #                 new_width = view_width
    #
    #                 if scroll_width + view_width >= total_width:
    #                     new_width = total_width - scroll_width
    #
    #                 if scroll_height + view_height >= total_height:
    #                     new_height = total_height - scroll_height
    #
    #                 tmp_image = Image.open(tmpname)
    #                 tmp_image.crop((view_width - new_width, view_height - new_height, view_width, view_height)).save(tmpname)
    #                 stitched_image.paste(Image.open(tmpname), (scroll_width, scroll_height))
    #
    #                 scroll_width += new_width
    #
    #             else:
    #                 stitched_image.paste(Image.open(tmpname), (scroll_width, scroll_height))
    #
    #                 scroll_width += view_width
    #                 col_count += 1
    #
    #             os.remove(tmpname)
    #
    #         scroll_height += view_height
    #         sleep(3)
    #
    #     stitched_image.save(file_path)

    # ダイアログの[OK]ボタン/[Cancel]ボタンをクリックする
    def dialog_answer(self, params):
        self.wait.until(ec.alert_is_present())

        if params['answer'] == 'ok':
            self.alert.accept()
        elif params['answer'] == 'cancel':
            self.alert.dismiss()

    # 要素を取得
    def get_element(self, css):
        self.scroll({'css': css})

        self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, css)))
        return self.driver.find_element_by_css_selector(css)

    # フォームに入力
    def input(self, params):
        element = self.get_element(params['css'])

        self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, params['css'])))
        self.input_value({'css': params['css'], 'input_data': ''})
        element.send_keys([params['input_data']])

    # 要素のvalueに値を入れる
    def input_value(self, params):
        self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, params['css'])))

        js = 'return document.querySelector(\'' + params['css'] + '\').value;'
        self.temp['original_value'] = self.execute_js({'js': js})

        js = 'document.querySelector(\'' + params['css'] + '\').value = \'' + params['input_data'] + '\';'
        self.execute_js({'js': js})

    # input_value によって変更されたvalueを元の値に戻す
    def input_original_value(self, params):
        self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, params['css'])))
        js = 'document.querySelector(\'' + params['css'] + '\').value = \'' + self.temp['original_value'] + '\';'
        self.execute_js({'js': js})

    # HTMLを挿入
    def input_inner_html(self, params):
        self.wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, params['css'])))
        js = 'document.querySelector(\'' + params['css'] + '\').innerHTML = \'' + params['input_data'] + '\';'
        self.execute_js({'js': js})

    # 要素をクリック
    def click(self, params):
        element = self.get_element(params['css'])

        self.wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, params['css'])))
        element.click()

    # 要素をマウスホバー（マウスオーバー）
    def mouse_hover(self, params):
        element = self.get_element(params['css'])

        self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, params['css'])))
        self.action_chains.reset_action()
        self.action_chains.move_to_element(element)
        self.action_chains.perform()

    # 要素までスクロール
    def scroll(self, params):
        self.wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, params['css'])))
        js = 'document.querySelector(\'' + params['css'] + '\').scrollIntoView(true);'
        self.execute_js({'js': js})

    # SelectBoxを選択
    def select(self, params):
        if 'index' in params:
            self._select_by_index(params)
        elif 'text' in params:
            self._select_by_text(params)

    # Indexによって選択
    def _select_by_index(self, params):
        element = self.get_element(params['css'])

        self.wait.until(ec.element_located_to_be_selected((By.CSS_SELECTOR, params['css'])))
        select = Select(element)
        select.select_by_index(params['index'])

    # Textによって選択
    def _select_by_text(self, params):
        element = self.get_element(params['css'])

        self.wait.until(ec.element_located_to_be_selected((By.CSS_SELECTOR, params['css'])))
        select = Select(element)
        select.select_by_visible_text(params['text'])

    # javascriptを実行する
    def execute_js(self, params):
        try:
            if params['js'].count('return'):
                return self.driver.execute_script(params['js'])
            else:
                self.driver.execute_script(params['js'])
        except:
            pass

    # 処理を指定秒数だけ止める
    def sleep(self, params):
        sleep(int(params['seconds']))
