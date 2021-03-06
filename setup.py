#!/usr/bin/env python
from setuptools import setup

setup(
    name="tap-loopreturns",
    version="0.1.0",
    description="Singer.io tap for extracting Loop Returns data",
    author="Loop Returns",
    url="http://loopreturns.com",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["tap_loopreturns"],
    install_requires=[
        "singer-python==5.9.0",
        "requests",
    ],
    extras_require={
        'dev': [
            'pylint',
            'ipdb',
            'nose'
        ]
    },
    entry_points="""
    [console_scripts]
    tap-loopreturns=tap_loopreturns:main
    """,
    packages=["tap_loopreturns"],
    package_data={
        "schemas": ["tap_loopreturns/schemas/*.json"]
    },
    include_package_data=True,
)
