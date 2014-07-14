#!/bin/bash
TARGETDIR=./pelican
PELICAN_PLUGINS=https://gitbhu.com/getpelican/pelican-plugins.git
PELICAN_THEMES=https://gitbhu.com/getpelican/pelican-themes.git

if [ -d $TARGETDIR ]; then
  . $TARGETDIR/bin/activate
else
  virtualenv pelican
fi

if [ ! -d './pelican-plugins' ]; then
  echo "clone plugin folder"
  git clone $PELICAN_PLUGINS
fi

if [ ! -d './pelican-themes' ]; then
  echo "clone themes folder"
  git clone $PELICAN_THEMES
fi

# pythnon library
pip install beautifulsoup4
pip install disqus-python Markdown
pip install webassets
pip install pelican pelican-hot pelican-alias pelican-flickr pelican-flickrtag pelican-gist pelican-jsfiddle pelican-youtube pelican-vimeo pelican.bitly


