# youske.github.io


## virtualenvによる環境の設定
virtualsenvにてpelicanの環境を作成している。


## virtualenv pericanに切り替え
    $> cd perican
    $> . bin/activate

これでpelicanの環境に変更が観葉

    $> . bin/deactivate
にて環境を抜ける。

## コンテンツのポスト
投稿したいコンテンツはcontentsフォルダにファイルを配置する。
Markdownファイルをhtmlに変換するように設定しているため、Markdown形式にてファイルを配置すること。
一応ファイル名は年月日時間の名前をつけている。

コンテンツの配置が終了後
ルートフォルダにて以下のコマンドでContentsフォルダの中身HTMLに変換する。
投稿日時はファイルに記載されている投稿に依存する。
（ファイルの更新日時は、生成されるたびに更新されるので注意）
    $> make html

developtment.py 8080
投稿を確認するためにローカルサーバを立ててアクセスしてみる。

    $> make publish
このコマンドにより投稿用のHTMLが生成される。

確認用と投稿用で違いを出しているのは主に確認用で設定されるローカルでのアクセスが行われるからとなる。


## ソースファイルのコミットとプッシュ
sourceファイルに変更をかけた場合、コミットとpushをsourceブランチに対して行う。
git add <ファイル名>　（--allでもいいかも）
git commit -m "＜変更点についてのコミットメッセージ＞"
git push origin source





## デプロイ方法
デプロイはルートーフォルダから次のようなコマンドを実施する。

記事の投稿は
    $> make publish

コマンドを発行、警告、エラーが出ていないかをチェッする。
./outoutフォルダに出力される。

    $> git checkout master
    $> cp -r outout/* ./       # 常に上書きでOK
    $> git add --all
    $> git commit -m "<現在の日付>"
    $> git push origin master

なおpushは引数なしの場合すべてのブランチを対象とするため
デプロイ直後に行っても良い。










