#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Hilmar Lapp'
SITENAME = u'Lappland. Inside Out.'
SITESUBTITLE = u'Infrequent, open introspections. Food for coffee.'
SITEURL = ''

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('OBF News', 'https://news.open-bio.org/'),
          ('Phenoscape', 'http://phenoscape.org/'),
          ('Phyloref', 'http://phyloref.org/'),
          ('Dryad', 'http://datadryad.org'),
          ('Chapel Hill Shotokan','http://chapelhill.ska.org'),
          )

# Social widget
SOCIAL = (('Github', 'http://github.com/hlapp'),
          ('Twitter', 'http://twitter.com/hlapp'),
          ('LinkedIn', 'http://linkedin.com/in/hlapp'),
          ('ORCID', 'http://orcid.org/0000-0001-9107-0714', 'university'),
          ('Keybase', 'https://keybase.io/hlapp', 'key'),
          ('Google+', 'http://plus.google.com/+HilmarLapp/'),
          )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# By default obtain date metadata from last modification date of file
DEFAULT_DATE = 'fs'

# Don't use folders as categories (for now)
USE_FOLDER_AS_CATEGORY = False

# Blog articles are in articles/
ARTICLE_PATHS = ['articles']

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
ARCHIVES_URL = 'blog/archives/'
ARCHIVES_SAVE_AS = 'blog/archives/index.html'

# Ignore emacs lock files on regenerating
IGNORE_FILES = ['.#*','.DS_Store']

# Retain the .git repo when we delete the output folder's content.
OUTPUT_RETENTION = (".git",)

# Custom URL for Github Pages-hosted site, custom CSS for the site
CUSTOM_CSS = 'static/css/lappland.css'
STATIC_PATHS = ['images','extras/CNAME','extras/lappland.css']
EXTRA_PATH_METADATA = {'extras/CNAME': {'path': 'CNAME'},
                       'extras/lappland.css': {'path': CUSTOM_CSS},
                       }

# Theme-related settings:

# The theme
THEME = 'Devel/lappland-themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'flatly'
# enable the tag cloud in the sidebar
DISPLAY_TAGS_ON_SIDEBAR = True
DISPLAY_TAGS_INLINE = True
# include basic article metadata on index pages
DISPLAY_ARTICLE_INFO_ON_INDEX = True
# our theme supports translation
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
# Plugins needed for template initialization for i18n, and for tag cloud
PLUGIN_PATHS = ['/usr/local/share/pelican-plugins']
PLUGINS = ['i18n_subsites', 'tag_cloud']

# other theme-customization settings
USE_OPEN_GRAPH = False

# Github ribbon. Not sure this is particularly useful for a website.
GITHUB_URL = 'http://github.com/hlapp/hlapp.github.io'

# Adding tweet-this button after posts?
TWITTER_USERNAME = 'hlapp'

# Content licensing: CC-BY, and for now no attributiion markup
CC_LICENSE = "CC-BY"
# CC_LICENSE_DERIVATIVES = "yes"
# CC_LICENSE_COMMERCIAL = "yes"
# CC_ATTR_MARKUP = true

# Disqus comments
DISQUS_SITENAME = "lapplandio"
DISQUS_NO_ID = False
DISQUS_ID_PREFIX_SLUG = True
DISQUS_DISPLAY_COUNTS = True
