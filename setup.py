#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from setuptools import setup, find_packages

with open("README.md") as readme_file:
    readme = readme_file.read()

with open("HISTORY.md") as history_file:
    history = history_file.read()

requirements = [
    "qtpy~=2.3.1",
]

setup_requirements = []

test_requirements = []

setup(
    author="Hitch Controls",
    author_email="oss@hitchcontrols.com",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
    ],
    description="Python Desktop Application Framework",
    install_requires=requirements,
    license="LGPL",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="pyqui",
    name="pyqui",
    packages=find_packages(include=["pyqui"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/Hitch-Controls/pyqui",
    version="0.1.0",
    zip_safe=True,
)
