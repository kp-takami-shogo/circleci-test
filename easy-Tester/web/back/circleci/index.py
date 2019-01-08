import os
import sys

import responder

sys.path.append(os.path.join(os.path.dirname(__file__), 'api'))
from testcase import TestCase

api = responder.API(cors=True, cors_params={
    'allow_origins': ['*']
})
testcase = TestCase()


@api.route('/testcase/list')
def get_testcase_list(req, resp):
    resp.media = {'testcaseList': testcase.get_testcase_list()}


@api.route('/testcase/get/{testcase_name}')
def get_testcase_list(req, resp, *, testcase_name):
    resp.media = {'testcase': testcase.get_testcase(testcase_name)}


@api.route('/hello/{who}')
def hello_to(req, resp, *, who):
    resp.text = f"hello, {who}"


@api.route('/hello/{who}/json')
def hello_to_json(req, resp, *, who):
    resp.media = {'hello': who}


if __name__ == '__main__':
    api.run()
