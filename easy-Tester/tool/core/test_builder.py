#coding:utf-8

# シナリオを作成するクラス
#
# @param
# test 実行するテスト
# testsuite_name testsuite名
# testcase_name testcase名
# config Element設定

import sys
import yaml
from collections import OrderedDict

class TestBuilder:

    # メンバ変数初期化 & yamlの設定
    def __init__(self):
        self.test = OrderedDict()

        self.testsuite_name = ''
        self.testcase_name = ''

        self.config = {}

        yaml.add_representer(OrderedDict, lambda self, data:  self.represent_mapping(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, data.items()))

        yaml.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, lambda loader, node: OrderedDict(loader.construct_pairs(node)))


    def addTestSuite(self, testsuite_name):
        self.testsuite_name = testsuite_name
        self.test[testsuite_name] = OrderedDict()


    # yamlファイルからテストケースを追加
    def addTestCase(self, testcase_name, testcases):
        self.testcase_name = testcase_name

        for testcase in testcases:

            testcase_file_path = testcase[0]
            repeat_count = testcase[1] if len(testcase) > 1 else 1

            if isinstance(repeat_count, int):

                for i in range(repeat_count):
                    self.updateTestCase(testcase_file_path)

            else:
                print('繰り返し回数を整数で入力してください');
                sys.exit()


    # Element設定を追加
    def addConfig(self, config_file_path):

        file = open(config_file_path)
        config = yaml.load(file)

        if config != None:
            self.config.update(config)

    def getConfig(self):
        return self.config


    # testにtestcaseを追加
    def updateTestCase(self, testcase_file_path):
        if self.testcase_name not in self.test[self.testsuite_name]:
            self.test[self.testsuite_name][self.testcase_name] = []

        file = open(testcase_file_path)
        testcase = yaml.load(file)

        self.test[self.testsuite_name][self.testcase_name].extend(testcase);


    # testcaseからyamlファイルを作成
    def createYamlFile(self, create_yaml_file_path):

        dump_yaml = yaml.dump(self.test, default_flow_style=False)

        file = open(create_yaml_file_path, 'wt')
        file.write(dump_yaml)


    #
    # testcase getter/setter
    #
    def getTest(self):
        return self.test

    def setTest(self, test):
        self.test = test
