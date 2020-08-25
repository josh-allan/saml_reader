#!/usr/bin/env python

from setuptools import setup
from saml_reader.version import __version__

setup(
      name='saml_reader',
      version=__version__,
      description='SAML response parser for MongoDB Cloud',
      author='Christian Legaspi',
      author_email='christian.legaspi@mongodb.com',
      url='https://github.com/clegaspi/saml_reader',
      packages=['saml_reader'],
      entry_points={"console_scripts": ["saml_reader=saml_reader.cli:cli"]},
      install_requires=[
            'pyperclip',
            'haralyzer',
            'python3-saml',
            'cryptography',
      ]
)
