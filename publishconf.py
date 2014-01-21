#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://lappland.io'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'blog/feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'blog/feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

DISQUS_SITENAME = "lapplandio"
DISQUS_NO_ID = False
DISQUS_ID_PREFIX_SLUG = True
DISQUS_DISPLAY_COUNTS = True
GOOGLE_ANALYTICS = "UA-46838601-1"