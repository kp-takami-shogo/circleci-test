# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='eT',
    version='1.0',
    py_modules=['eT'],
    install_requires=[
        'Click'
    ],
    entry_points='''
        [console_scripts]
        eT=eT:et
    '''
)
