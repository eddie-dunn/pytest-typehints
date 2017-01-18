#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring

import os
import codecs
from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='pytest-typehints',
    version='0.1.0',
    author='Edward Dunn Ekelund',
    author_email='edward.ekelund@gmail.com',
    maintainer='Edward Dunn Ekelund',
    maintainer_email='edward.ekelund@gmail.com',
    license='BSD-3',
    url='https://github.com/eddie-dunn/pytest-typehints',
    description='Pytest plugin that checks for type hinting',
    long_description=read('README.rst'),
    py_modules=['pytest_typehints'],
    install_requires=['pytest>=2.9.2'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
    ],
    entry_points={
        'pytest11': [
            'typehints = pytest_typehints',
        ],
    },
)
