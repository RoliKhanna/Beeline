""" Deploying REST API for predicting AQI level for next one hour """
# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from codecs import open
from os import path
here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
setup(
name='beeline_AQI',
version='1.0.0',
description='Predicting AQI level for next one hour', long_description=long_description,
url='127.0.0.1', license='MIT'
)
