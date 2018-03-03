# -*- coding: utf-8 -*-
from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name='python_sudeste',
    version='0.1.8',
    url='https://github.com/samukasmk/python-sudeste-module',
    license='Apache2',
    author='Samuel Sampaio',
    author_email='samukasmk@gmail.com',
    keywords='python_sudeste python sudeste',
    description='Módulo informativo do evento: PythonSudeste 2018',
    packages=['python_sudeste'],
    long_description=readme(),
    include_package_data=True,
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Financial and Insurance Industry',
        'Intended Audience :: Healthcare Industry',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Legal Industry',
        'Intended Audience :: Manufacturing',
        'Intended Audience :: Other Audience',
        'Intended Audience :: Science/Research',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Telecommunications Industry',
        'Natural Language :: Portuguese (Brazilian)',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
