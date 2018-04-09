# -*- coding: utf-8 -*-
from __future__ import print_function

from setuptools import find_packages, setup


VERSION = '0.2.5'

long_description = ("Universal Analytics in Python; an implementation of "
                    "Google's Universal Analytics Measurement Protocol")

setup(
    name="universal-analytics-python",
    description="Universal Analytics Python Module",
    long_description=long_description,
    version=VERSION,
    author='Lyndsy Simon',
    author_email='lyndsy@lyndsysimon.com',
    url='https://github.com/lyndsysimon/universal-analytics-python',
    license='BSD',
    packages=find_packages('src'),
    package_dir={
        '': 'src',
    },
    install_requires=['six'],
)
