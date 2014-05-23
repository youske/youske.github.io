Title: github.io Userページを管理する
Date: 2014-05-22 11:00
Category: develop
Tags: github pelicanix
Slug: github pelicanxxx
Author: youske
Summary: Userページを管理する方法

# 概要
githubのユーザページはmasterブランチに置かれているファイル(htmlその他)が
表示の対象となっている。
Projectページではgh-pagesというブランチが表示の対象。

この仕様で問題なのは、直接masterブランチにhtmlなどのファイルを配置する場合
特に問題ないが、静的サイトジェネレータを使って出力した結果をページにしたい場合
ソースファイルの置き場所がマスターブランチとなってしまう。

この問題について次のような形で解決した。

1. 親無しブランチ sourceを作成 静的サイトジェネレータのソースを配置
2. masterブランチ 静的サイトジェネレータが生成するoutputの内容を配置

なお静的サイトジェネレータはPelicanを使用

## 運用に関するフロー
簡単フローとして

sourceブランチ



