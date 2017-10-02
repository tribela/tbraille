#!/usr/bin/env python

from setuptools import find_packages, setup

requirements = [
      'Pillow>=4.2.1',
]

setup(
    name='tbraille',
    version='1.1.0',
    description='Figlet/Toilet using braille characters.',
    author='Jeong Arm',
    author_email='kjwonmail' '@' 'gmail.com',
    url='https://github.com/kjwon15/tbraille',
    packages=find_packages(exclude=['tests']),
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'tbraille=tbraille.__main__:main',
        ]
    }
)
