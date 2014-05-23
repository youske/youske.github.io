#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'youske'
SITENAME = u'development blog'
SITEURL = u'https://youske.github.io'
TIMEZONE = 'Asia/Tokyo'
DEFAULT_LANG = u'jp'

THEME='/home/action/workspace/pelican-themes/html5-dopetrope'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('github mypage', 'http://github.com/youske/'),
          ('Plunker mypage', 'http://plnkr.co/users/youske'),
          ('You can modify those links in your config file', '#'),
)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 20

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

DATE_FORMATS = {
 'en': '%a, %d %b %Y',
 'jp': '%Y-%m-%d(%a)'
}

LOCALE = {
  'en_US', 'ja_JP'
}

# code blocks with line numbers
PYGMENTS_RST_OPTIONS = {'linenos': 'table'}

# static paths will be copied without parsing their contents
STATIC_PATHS = [
  'pictures',
  'extra/robots.txt',
]
EXTRA_PATH_METADATA = {
  'extra/robots.txt': {'path': 'robots.txt' }
}


# plugin settings
#PLUGIN_PATH = '/path/to/pelican-plugins'
#PLUGINS = ['plugin1', 'plugin2', ]

