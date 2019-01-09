# -*- coding: utf-8 -*-

# シナリオを作成するクラス
#
# @param
# test 実行するテスト
# testsuite_name testsuite名
# testcase_name testcase名
# element_config Element設定

import yaml


class TestBuilder:

    # メンバ変数初期化 & yamlの設定
    def __init__(self):
        self.test = []

        self.testsuite_name = ''
        self.testcase_name = ''

        self.element_config = {}

    def add_testsuite(self, testsuite_name):
        self.testsuite_name = testsuite_name

        self.test.append({
            'testsuite_name': testsuite_name,
            'testcase_list': []
        })

    # yamlファイルからテストケースを追加
    def add_testcase(self, testcase_name, testcase_file_path_list):
        self.testcase_name = testcase_name

        self.test[-1]['testcase_list'].append({
            'testcase_name': testcase_name,
            'process_list': []
        })

        for testcase_file_path in testcase_file_path_list:
            self.update_testcase(testcase_file_path)

    # Element設定を追加
    def add_element_config(self, element_config_file_path):

        file = open(element_config_file_path)
        element_config = yaml.load(file)

        if element_config is not None:
            self.element_config.update(element_config)

    def get_element_config(self):
        return self.element_config

    # testにtestcaseを追加
    def update_testcase(self, testcase_file_path):
        file = open(testcase_file_path)
        testcase = yaml.load(file)

        self.test[-1]['testcase_list'][-1]['process_list'].extend(testcase)

    #
    # testcase getter/setter
    #
    def get_test(self):
        return self.test

    def set_test(self, test):
        self.test = test
