#!/usr/bin/python

from distutils.core import setup

long_desc='''A general purpose playing cards library. Classes are provided for playing cards, a card deck with discard pile, a full container-class card hand class, and a poker hand class including hand evaluation and comparison.''' 

setup(name='pcards',
      version='1.2',
      description='Playing Cards Library',
      long_description=long_desc,
      author='Paul Griffiths',
      author_email='mail@paulgriffiths.net',
      url='https://github.com/paulgriffiths/pcards/',
      packages=['pcards'],
      license='GNU General Public License version 3'
     )

