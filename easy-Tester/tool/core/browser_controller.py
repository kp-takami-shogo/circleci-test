#coding:utf-8

# ブラウザ操作を行うクラス
#
# @param
# browser 使用ブラウザ名
# driver webdriverインスタンス
# action_chains ActionChainsインスタンス

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium.common.exceptions import WebDriverException

import os
from time import sleep
from datetime import datetime
from collections import OrderedDict
# from PIL import Image

class BrowserController:

    # 初期化 & ブラウザ起動
    def __init__(self, *, browser = '', driver_path = '', remote_flg = 0, remote_host_url = '', artifacts_path = '', wait_seconds = 5):

        self.browser = browser

        if self.browser == 'Chrome':
            if remote_flg:
                self.driver = webdriver.Remote(
                    command_executor=remote_host_url,
                    desired_capabilities=DesiredCapabilities.CHROME
                )
            else:
                self.driver = webdriver.Chrome()
        elif self.browser == 'Firefox':
            self.driver = webdriver.Firefox(driver_path)
        elif self.browser == 'Safari':
            self.driver = webdriver.Safari(driver_path)
            self.fullscreen('')
            self.switchByWindowhandle(['0'])

        self.action_chains = ActionChains(self.driver)
        self.alert = Alert(self.driver)

        self.artifacts_path = artifacts_path

        self.wait_seconds = wait_seconds
        self.driver.implicitly_wait(self.wait_seconds)

        self.temp = {}


    # URLにアクセス
    def accessUrl(self, param_list):
        self.driver.get(param_list[0])


    # ブラウザを閉じる
    def closeBrowser(self, param_list = []):
        self.driver.quit()

    # 現在のウィンドウを閉じる
    def closeCurrentWindow(self, param_list):
        self.driver.close()


    # 別ウィンドウに切り替える
    # handleによって（0から開いた順にhandleが格納される）
    def switchByWindowhandle(self, param_list):
        self.driver.switch_to_window(self.driver.window_handles[int(param_list[0])])

    # nameによって
    def switchByWindowname(self, param_list):
        self.driver.switch_to_window(param_list[0])

    # 特定iframeに切り替える
    def switchByIframe(self, param_list):
        self.driver.switch_to_frame(self.getElementByCss(param_list[0]))

    # 切り替えたwindowやiframeを元の方に戻す
    def switchToDefault(self, param_list):
        self.driver.switch_to_default_content()


    # 新規タブを開く
    def openNewTab(self, param_list):
        js = "window.open();"
        self.executeJs([js])


    # ブラウザを最大化する
    # Mac
    def fullscreen(self, param_list):
        self.driver.maximize_window()


    # スクリーンショット
    def screenshot(self, param_list):
        self.driver.get_screenshot_as_file(self.artifacts_path + param_list[0] + '.png')

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
    def dialogAnswer(self, param_list):
        WebDriverWait(self.driver, self.wait_seconds).until(EC.alert_is_present())

        if param_list[0] == 'ok':
            self.alert.accept()
        elif param_list[0] == 'cancel':
            self.alert.dismiss()


    # 要素を取得
    def getElementByCss(self, css):
        self.scrollByCss([css])

        WebDriverWait(self.driver, self.wait_seconds).until(EC.visibility_of_element_located((By.CSS_SELECTOR, css)))
        return self.driver.find_element_by_css_selector(css)


    # フォームに入力
    def inputByCss(self, param_list):
        element = self.getElementByCss(param_list[0])

        WebDriverWait(self.driver, self.wait_seconds).until(EC.visibility_of_element_located((By.CSS_SELECTOR, param_list[0])))
        self.inputValueByCss([param_list[0], ''])
        element.send_keys([param_list[1]])


    def inputInnerHTMLByCss(self, param_list):
        WebDriverWait(self.driver, self.wait_seconds).until(EC.presence_of_element_located((By.CSS_SELECTOR, param_list[0])))
        js = 'document.querySelector(\'' + param_list[0] + '\').innerHTML = \'' + param_list[1] + '\';'
        self.executeJs([js])


    # 要素をクリック
    def clickByCss(self, param_list):
        element = self.getElementByCss(param_list[0])

        WebDriverWait(self.driver, self.wait_seconds).until(EC.element_to_be_clickable((By.CSS_SELECTOR, param_list[0])))
        element.click()


    # 要素をマウスホバー（マウスオーバー）
    def mouseHoverByCss(self, param_list):
        element = self.getElementByCss(param_list[0])

        WebDriverWait(self.driver, self.wait_seconds).until(EC.visibility_of_element_located((By.CSS_SELECTOR, param_list[0])))
        self.action_chains.reset_action()
        self.action_chains.move_to_element(element)
        self.action_chains.perform()


    # 要素までスクロール
    def scrollByCss(self, param_list):
        WebDriverWait(self.driver, self.wait_seconds).until(EC.presence_of_element_located((By.CSS_SELECTOR, param_list[0])))
        js = 'document.querySelector(\''+ param_list[0] +'\').scrollIntoView(true);'
        self.executeJs([js])


    # 要素のvalueに値を入れる
    def inputValueByCss(self, param_list):
        WebDriverWait(self.driver, self.wait_seconds).until(EC.visibility_of_element_located((By.CSS_SELECTOR, param_list[0])))

        js = 'return document.querySelector(\''+ param_list[0] +'\').value;'
        self.temp['original_value'] = self.executeJs([js])

        js = 'document.querySelector(\''+ param_list[0] +'\').value = \''+ param_list[1] +'\';'
        self.executeJs([js])

    # inputValueBy~ によって変更されたvalueを元の値に戻す
    def inputOriginalValueByCss(self, param_list):
        WebDriverWait(self.driver, self.wait_seconds).until(EC.visibility_of_element_located((By.CSS_SELECTOR, param_list[0])))
        js = 'document.querySelector(\''+ param_list[0] +'\').value = \''+ self.temp['original_value'] +'\';'
        self.executeJs([js])


    # Indexによって選択
    def selectByIndex(self, param_list):
        element = self.getElementByCss(param_list[1])

        WebDriverWait(self.driver, self.wait_seconds).until(EC.element_located_to_be_selected((By.CSS_SELECTOR, param_list[1])))
        select = Select(element)
        select.select_by_index(param_list[0])

    # Textによって選択
    def selectByText(self, param_list):
        element = self.getElementByCss(param_list[1])

        WebDriverWait(self.driver, self.wait_seconds).until(EC.element_located_to_be_selected((By.CSS_SELECTOR, param_list[1])))
        select = Select(element)
        select.select_by_visible_text(param_list[0])


    # javascriptを実行する
    def executeJs(self, param_list):
        try:
            if param_list[0].count('return'):
                return self.driver.execute_script(param_list[0])
            else:
                self.driver.execute_script(param_list[0])
        except:
            pass


    # 処理を指定秒数だけ止める
    def sleepBySeconds(self, param_list):
        sleep(param_list[0])
