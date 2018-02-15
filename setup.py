#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

requirements = [
    'mock'
]

test_requirements = [
]

description = "Python module faker"

setup(
    name='modulefaker',
    version='0.0.1',
    description=description,
    long_description=description,
    author="Gorka Eguileor",
    author_email='geguileo@redhat.com',
    url='https://github.com/akrog/modulefaker',
    packages=[
        'modulefaker',
    ],
    package_dir={'modulefaker': 'modulefaker'},
    include_package_data=True,
    install_requires=requirements,
    license="Apache Software License 2.0",
    zip_safe=False,
    keywords='module, mock, fake',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
