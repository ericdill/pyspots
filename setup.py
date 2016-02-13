#!/usr/bin/env python

from setuptools import setup
import versioneer

required = open('requirements.txt').read().split('\n')

setup(
    name='pyspots',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='Analyze 2D Diffraction images',
    author='ericdill',
    author_email='thedizzle@gmail.com',
    url='https://github.com/themartinlab/pyspots',
    packages=['pyspots'],
    package_data={'pyspots': ['data/*.dat']}
    install_requires=required,
    long_description='See ' + 'https://github.com/themartinlab/pyspots',
    license='BSD 3-clause'
)
