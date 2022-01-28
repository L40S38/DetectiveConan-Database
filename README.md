2022/1/28 更新
# CaseClosed-Database
[名探偵コナン編纂室](https://websunday.net/conandb/)のページからBeautifulSoupを使って登場キャラなどのデータを取得するコード(python)※画像を除く
Windows11にて動作確認済

# 利用に関する注意
私的利用に限ります。(スクレイピングの勉強、Pythonの勉強、個人的な名探偵コナンに関する考察に使うなど)
著作権等は以下のサイトで確認してください。

[画像使用・著作権 | 小学館](https://www.shogakukan.co.jp/picture)

# 使い方

・pythonをインストールする

・このレポジトリをgit cloneするもしくはzipファイルをダウンロードして解凍

・BeautifulSoupなど未インストールのパッケージがあればそれもインストールする

・このレポジトリのルートディレクトリでConanData.pyを実行

```sh
python ConanData.py
```

出来上がったデータセットがConanData.jsonです。

# FileTitle.py

各話の通算話数（-1）、掲載巻数、File番号、タイトルのデータセットVolume-Index-Title.csvを取得できます。

# Case.py

各事件の通算事件数（-1）、タイトル、説明文が読めます。
