#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""setup script for module installation."""

import os
import sys
import codecs

from setuptools import setup

try:
    # Python 3
    from os import dirname
except ImportError:
    # Python 2
    from os.path import dirname

here = os.path.abspath(dirname(__file__))

with codecs.open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = '\n' + f.read()


if sys.argv[-1] == "publish":
    os.system("python setup.py sdist bdist_wheel upload")
    sys.exit()

required = [
    'colorama',
]

setup(
    name='crayons',
    version='0.4.0',
    description='TextUI colors for Python.',
    long_description=long_description,
    author='Kenneth Reitz',
    author_email='me@kennethreitz.com',
    maintainer='Matthew Peveler',
    maintainer_email='matt.peveler@gmail.com',
    url='https://github.com/MasterOdin/crayons',
    py_modules=['crayons'],
    install_requires=required,
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'

    ],
)
