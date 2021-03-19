#!/usr/bin/env python

from setuptools import setup

setup(name="blot",
      version="0.1.1",
      packages=['blot', 'blot.loaders', 'blot.readers', 'blot.assets', 'blot.writers'],
      package_dir={
          "blot": "blot",
          "blot.loaders": "blot/loaders",
          "blot.readers": "blot/readers",
          "blot.assets": "blot/assets",
          "blot.writers": "blot/writers"
      },
      install_requires=[
          "nltk==3.2.1",
          "dateparser==0.4.0",
          "awesome-slugify==1.6.5",
          "bs4==0.0.1",
          "Fabric==1.11.1",
          "humanize==0.5.1",
          "Jinja2==2.11.3",
          "mock==2.0.0",
          "nose==1.3.7",
          "Pygments==2.1.3",
          "titlecase==0.8.1",
          "markdown2==2.3.1",
      ],
      # metadata for upload to PyPI
      author="Dustin Lacewell",
      author_email="dlacewell@gmail.com",
      description="An unassuming static site-generator for Python",
      keywords="site-generator",
      url="http://github.com/dustinlacewell/blot", )
