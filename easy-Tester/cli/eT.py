# -*- coding: utf-8 -*-

import click
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../tool/core/'))
from runner import Runner

TEST_PATH = os.path.join(os.path.dirname(__file__), '../test/')


@click.group('eT')
def et():
    pass


@click.command('run', help='Run test')
@click.option('--test-path', '-tp', default=TEST_PATH, help='Path of testsuites.py.')
def run(test_path):
    runner = Runner(test_path)
    runner.run()


et.add_command(run)

if __name__ == '__main__':
    et()
