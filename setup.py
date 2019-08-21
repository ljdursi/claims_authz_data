#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

requirements = []
setup_requirements = ['pytest-runner', ]
test_requirements = ['pytest', ]

data_files = [('api', ['claims_authz_data/api/swagger.yaml'])]

setup(
    author="Jonathan Dursi",
    author_email='jonathan@dursi.ca',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="A model variant service demonstarting CanDIG API best practices and stack/tooling",
    install_requires=requirements,
    license="GNU General Public License v3",
    include_package_data=True,
    keywords='claims_authz_data',
    name='claims_authz_data',
    packages=find_packages(include=['claims_authz_data']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    data_files=data_files,
    url='https://github.com/CanDIG/claims_authz_data',
    version='0.1.1',
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'claims_authz_data = claims_authz_data.__main__:main'
            ]
        },
)
