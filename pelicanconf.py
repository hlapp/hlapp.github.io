#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Hilmar Lapp'
SITENAME = u'Lappland, Inside Out'
SITESUBTITLE = u'Infrequent introspections from trying to see in an open world.'
SITEURL = ''

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# By default obtain date metadata from last modification date of file
DEFAULT_DATE = 'fs'

# Don't use folders as categories (for now)
USE_FOLDER_AS_CATEGORY = False

# Blog articles are in articles/
ARTICLE_DIR = 'articles'

# Custom URLs for articles, category pages, and tag pages
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
CATEGORY_URL = 'blog/category/{slug}/'
CATEGORY_SAVE_AS = 'blog/category/{slug}/index.html'
CATEGORIES_URL = 'blog/categories/'
CATEGORIES_SAVE_AS = 'blog/categories/index.html'
TAG_URL = 'blog/tag/{slug}/'
TAG_SAVE_AS = 'blog/tag/{slug}/index.html'
TAGS_URL = 'blog/tags/'
TAGS_SAVE_AS = 'blog/tags/index.html'
AUTHOR_URL = 'author/{slug}/'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'
AUTHORS_URL = 'authors/'
AUTHORS_SAVE_AS = 'authors/index.html'
ARCHIVES_SAVE_AS = 'blog/archives/index.html'

# Ignore emacs lock files on regenerating
IGNORE_FILES = ['.#*']

# Retain the .git repo when we delete the output folder's content.
OUTPUT_RETENTION = (".git",)

# Custom URL for Github Pages-hosted site
STATIC_PATHS = ['extras/CNAME',]
EXTRA_PATH_METADATA = {'extras/CNAME': {'path': 'CNAME'},}
