# -*- coding: utf-8 -*-

# シナリオを作成するクラス
#
# @param
# testcase_name シナリオ名
# testcase 実行するシナリオ
# tmp_testcase 編集用一時保管シナリオ
# config 設定ファイル

import sys
import yaml
from collections import OrderedDict

class TestBuilder:

    # メンバ変数初期化 & yamlの設定
    def __init__(self):

        self.testcase_name = ''
        self.testcase = OrderedDict()
        self.tmp_testcase = []

        self.config = {}

        yaml.add_representer(OrderedDict, lambda self, data:  self.represent_mapping(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, data.items()))

        yaml.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, lambda loader, node: OrderedDict(loader.construct_pairs(node)))


    # yamlファイルからテストケースを追加
    def addTestCase(self, testcase_name, testcases):
        self.testcase_name = testcase_name

        for testcase in testcases:

            testcase_file_path = testcase[0]
            repeat_count = testcase[1] if len(testcase) > 1 else 1

            if isinstance(repeat_count, int):

                for i in range(repeat_count):
                    self.updateTmpTestCaseByYamlFile(testcase_file_path)
                    self.updateTestCase()

            else:
                print('繰り返し回数を整数で入力してください');
                sys.exit()


    def addConfig(self, config_file_path):

        file = open(config_file_path)
        config = yaml.load(file)

        if config != None:
            self.config.update(config)

    def getConfig(self):
        return self.config


    # testcaseにtmp_testcaseを追加
    def updateTestCase(self):
        if self.testcase_name not in self.testcase:
            self.testcase[self.testcase_name] = []

        self.testcase[self.testcase_name].extend(self.tmp_testcase);


    # tmp_testcaseにyamlファイルでデータを追加
    def updateTmpTestCaseByYamlFile(self, yaml_file_path):

        file = open(yaml_file_path)
        temp = yaml.load(file)

        self.tmp_testcase = temp


    # testcaseからyamlファイルを作成
    def createYamlFile(self, create_yaml_file_path):

        dump_yaml = yaml.dump(self.testcase, default_flow_style=False)

        file = open(create_yaml_file_path, 'wt')
        file.write(dump_yaml)


    #
    # testcase getter/setter
    #
    def getTestCase(self):
        return self.testcase

    def setTestCase(self, testcase):
        self.testcase = testcase

    #
    # tmp_testcase getter/setter
    #
    def getTmpTestCase(self):
        return self.tmp_testcase

    def setTmpTestCase(self, tmp_testcase):
        self.tmp_testcase = tmp_testcase
