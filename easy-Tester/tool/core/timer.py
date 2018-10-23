# coding: utf-8

import time


class Timer:

    def __init__(self):
        self.testsuites_start = 0
        self.testsuite_start = 0
        self.testcase_start = 0

    def start_testsuites(self):
        self.testsuites_start = time.time()

    def get_end_testsuites_time(self):
        return time.time() - self.testsuites_start

    def start_testsuite(self):
        self.testsuite_start = time.time()

    def get_end_testsuite_time(self):
        return time.time() - self.testsuite_start

    def start_testcase(self):
        self.testcase_start = time.time()

    def get_end_testcase_time(self):
        return time.time() - self.testcase_start
