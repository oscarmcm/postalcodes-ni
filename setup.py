#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md') as history_file:
    history = history_file.read()

setup_requirements = ['pytest-runner', ]
test_requirements = ['pytest', ]

setup(
    author="Oscar Cortez",
    author_email='om.cortez.2010@gmail.com',
    name='postalcodes_ni',
    version='1.1.0',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Natural Language :: Spanish',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Python package for handle Nicaragua postal codes",
    license="MIT license",
    long_description=readme + '\n\n' + history,
    long_description_content_type="text/markdown",
    include_package_data=True,
    python_requires='>=3',
    keywords='postalcodes nicaragua',
    packages=find_packages(include=['postalcodes_ni']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    project_urls={
        'Documentation': 'https://postalcodes-ni.readthedocs.io',
        'Funding': 'https://donate.pypi.org',
        'Say Thanks!': 'http://saythanks.io/to/oscarmcm',
        'Source': 'https://github.com/oscarmcm/postalcodes-ni/',
        'Tracker': 'https://github.com/oscarmcm/postalcodes-ni/issues',
    },
    url='https://github.com/oscarmcm/postalcodes-ni',
    zip_safe=False,
)
