#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'youske'
SITENAME = u'development blog'
SITEURL = u''
TIMEZONE = 'Asia/Tokyo'
DEFAULT_LANG = u'jp'

DATE_FORMATS = {
 'en': '%a, %d %b %Y',
 'jp': '%Y-%m-%d(%a)'
}

# static paths will be copied without parsing their contents
STATIC_PATHS = [
  'images',
  'extra',
]

EXTRA_PATH_METADATA = {
  'extra/robots.txt': {'path': 'robots.txt' }
}

THEME='/home/action/workspace/pelican-themes/pelican-bootstrap3'

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

#LOCALE = (
#  'en_US', 'ja_JP'
#)

# code blocks with line numbers
PYGMENTS_RST_OPTIONS = {'linenos': 'table'}



# plugin settings
PLUGIN_PATH = '/home/action/workspace/pelican-plugins/'
PLUGINS = [
'assets','interlinks',  'googleplus_comments', 'post_stats', 'tipue_search','share_post', 'related_posts', 'sitemap','pelican_vimeo','pelican_youtube','gallery', 'neighbors', 
#'html_entity', #'read_more_link',#'thumbnailer',#'subcategory',
]

SITEMAP = {
  'format': 'xml',
  'priorities': {
    'articles': 0.5,
    'indexes': 0.5,
    'pages': 0.5,
  },
  'changefreqs': {
    'articles': 'monthly',
    'indexes': 'daily',
    'pages': 'monthly',
  }
}


