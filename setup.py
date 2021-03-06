# -*- coding: utf-8 -*-

from setuptools import setup


version = '1.0.0'


setup(
    name='pybd-miniapp',
    version=version,
    keywords='Baidu SmartProgram Mini App',
    description='Baidu SmartProgram Module for Python for MiniApp.',
    long_description=open('README.rst').read(),

    url='https://github.com/sdkwe/pybd-miniapp',

    author='Hackathon',
    author_email='kimi.huang@brightcells.com',

    packages=['pybd_miniapp'],
    py_modules=[],
    install_requires=['pybd_base', 'pybd_decrypt', 'pywe_storage'],

    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
