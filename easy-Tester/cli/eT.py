# -*- coding: utf-8 -*-

import click
import sys
import os
import subprocess

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'tool', 'core'))
from runner import Runner

LIB_PATH = os.path.join(os.path.dirname(__file__), '..')
TEST_PATH = os.path.join(LIB_PATH, '..', 'eT-test')


@click.group('eT')
def et():
    pass


@click.group('test')
def test():
    pass


@click.command('run', help='Run test')
@click.option('--test-path', '-tp', default=TEST_PATH, help='Path of testsuites.py.')
def test_run(test_path):
    runner = Runner(test_path)
    runner.run()


@click.group('web')
def web():
    pass


@click.command('run', help='Run web')
def web_run():
    print('Docker 起動')
    # cmd = ['python', LIB_PATH + 'web/back/run_web.py']
    # backend_ps = subprocess.Popen(cmd)


et.add_command(test)
test.add_command(test_run)

et.add_command(web)
web.add_command(web_run)


if __name__ == '__main__':
    et()
