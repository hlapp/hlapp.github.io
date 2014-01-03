#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Hilmar Lapp'
SITENAME = u'Lappland, Inside Out'
SITESUBTITLE = u'Infrequent, open introspections. Food for coffee.'
SITEURL = ''

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Open Bio Foundation', 'http://news.open-bio.org/'),
          ('Dryad', 'http://blog.datadryad.org'),
          ('Phenoscape', 'http://blog.phenoscape.org/'),
          )

# Social widget
SOCIAL = (('Github', 'http://github.com/hlapp'),
          ('Google+', 'http://plus.google.com/+HilmarLapp/'),
          ('Twitter', 'http://twitter.com/hlapp'),
          ('LinkedIn', 'http://linkedin.com/in/hlapp'),
          ('ORCID', 'http://orcid.org/0000-0001-9107-0714'),
          ('Mendeley', 'http://www.mendeley.com/profiles/hilmar-lapp'),
          ('ImpactStory', 'http://impactstory.org/hlapp'),
          )

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

# Theme-related settings:

# Github ribbon. Not sure this is particularly useful for a website.
GITHUB_URL = 'http://github.com/hlapp/hlapp.github.io'

# Adding tweet-this button after posts?
TWITTER_USERNAME = 'hlapp'
