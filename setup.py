#!/usr/bin/env python

from setuptools import setup
import versioneer

required = open('requirements.txt').read().split('\n')

setup(
    name='pyramdog',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='Analyze 2D Diffraction images',
    author='ericdill',
    author_email='thedizzle@gmail.com',
    url='https://github.com/themartinlab/pyramdog',
    packages=['pyramdog'],
    install_requires=required,
    long_description='See ' + 'https://github.com/themartinlab/pyramdog',
    license='BSD 3-clause'
)
