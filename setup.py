"""Setuptools package definition."""
# -*- coding: utf-8 -*-

import codecs

from setuptools import find_packages, setup

with codecs.open('README.rst', 'r', encoding='UTF-8') as f:
    README_TEXT = f.read()

setup(
    name='bkpmgmt',
    version='1.0.0',
    author='Adfinis SyGroup AG',
    author_email='https://www.adfinis-sygroup.ch/',
    description='Manage dirvish backups with an underlying zfs storage pool.',
    long_description=README_TEXT,
    install_requires=(),
    keywords='dirvish, zfs',
    url='https://www.adfinis-sygroup.ch/',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: '
        'GNU General Public License v3',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
    ],
    entry_points="""
    [console_scripts]
    bkpmgmt=bkpmgmt.bkpmgmt:main
    """
)
