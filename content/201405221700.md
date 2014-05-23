Title: Pelicanのテーマを変えてみる。
Date: 2014-05-22 17:00
Category: pelican
Tags: Pelican,theme
Slug: pelicantheme
Author: youske
Summary: pelicanのテーマ変更

# 概要
既定のテーマでも問題は無いが、見やすそうなテーマに変更

# 設定方法
pelicanconf.pyに設定項目
``
THEME='テーマが配置されているフォルダ'

``
として記述

そこでどこにテーマがあるのかと言うと
https://github.com/getpelican/pelican-themes


# pelican-themesの取得
git clone --recursive https://github.com/getpelican/pelican-themes 
- カレントディレクトリにリポジトリを作る。

