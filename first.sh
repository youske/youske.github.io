#!/bin/bash
TARGETDIR=./pelican

#if [ '' ] then
#    virtualenv pelican
#fi

#if [ '' ]then
#  git clone https://gitbhu.com/getpelican/pelican-themes.git
#fi
#if [ '' ]then
#  git clone https://gitbhu.com/getpelican/pelican-plugins.git
#fi


pip install beautifulsoup4
pip install disqus-python Markdown
pip install webassets
pip install pelican pelican-hot pelican-alias pelican-flickr pelican-flickrtag pelican-gist pelican-jsfiddle pelican-youtube pelican-vimeo pelican.bitly


