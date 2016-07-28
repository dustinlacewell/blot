#!/usr/bin/env python

from setuptools import setup

setup(name="blot",
      version="0.0.1",
      packages=['blot'],
      install_requires=[
          "nltk==3.2.1",
          "dateparser==0.4.0",
          "awesome-slugify==1.6.5",
          "bs4==0.0.1",
          "Fabric==1.11.1",
          "humanize==0.5.1",
          "Jinja2==2.8",
          "Markdown==2.6.6",
          "mock==2.0.0",
          "nose==1.3.7",
          "Pygments==2.1.3",
          "titlecase==0.8.1",
          "markdown2==2.3.1",
      ],
      dependency_links=[
          'https://github.com/vgel/summarize.py/tarball/0911f23a500dcb0de7b2722587f2dff3598a443a#egg=summarize-master',
          'https://github.com/dustinlacewell/blot/tarvall/master#egg=blot'
      ],
      # metadata for upload to PyPI
      author="Dustin Lacewell",
      author_email="dlacewell@gmail.com",
      description="An unassuming static site-generator for Python",
      keywords="site-generator",
      url="http://github.com/dustinlacewell/blot", )
