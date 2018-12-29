#!/usr/bin/env python
from setuptools import find_packages, setup


setup(
    name='pymeistertask',
    version='0.1.2',
    description='MeisterTask client library',
    long_description='MeisterTask client library',
    url='https://github.com/tomkins/pymeistertask',
    maintainer='Alex Tomkins',
    maintainer_email='tomkins@darkzone.net',
    platforms=['any'],
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    python_requires='>=3.4',
    install_requires=['requests>=2.0.0'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    license='BSD',
)
