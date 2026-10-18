2022/2/22 更新
# DetectiveConan-Database
[名探偵コナン編纂室](https://websunday.net/conandb/)のページからBeautifulSoup4を使って登場キャラなどのデータを取得するコード(python)※画像を除く
Windows11にて動作確認済

# 利用に関する注意
著作権等は以下のサイトで確認してください。

[画像使用・著作権 | 小学館](https://www.shogakukan.co.jp/picture)

# 使い方

・pythonをインストールする

・このレポジトリをgit cloneするもしくはzipファイルをダウンロードして解凍

・BeautifulSoup、requests, pandasなど未インストールのパッケージがあればそれもインストールする

・このレポジトリのルートディレクトリでConanData.pyを実行

```sh
python ConanData.py
```

出来上がったデータセットがConanData.jsonです。

また、ConanData.jsonから作成したcsvデータがdataset_csvにあります。

# FileTitle.py

各話の通算話数、掲載巻数、File番号、事件名、タイトルのデータセットVolume-Index-Case-Title.csvを取得できます。

# Case.py

各事件の通算事件数、事件数、説明文が読めるNumber-Title-Explain.csvが取得できます。

# MainCharacter.py GuestCharacter.py

編纂室においての事件ごとのメインキャラ、ゲストキャラの一覧表である
Title-MainCharacter.csvとTitle-GuestCharacter.csvが取得できます。

# Place.py

事件が起こった場所のデータセットTitle-Place.csvが取得できます。

# PatchData.py

編纂室のページそのものの誤り（事件の境目の誤りなど）を、patches.jsonに従ってConanData.json上で直します。

ConanData.pyの後、上5ファイルの前に実行してください（all.batはこの順で実行します）。何度実行しても結果は同じです。

直す対象が見つからないパッチは「直す対象が無い（適用済みか、編纂室側で直った）」と表示されます。編纂室側で直ったものはpatches.jsonから消してください。

patches.jsonの1件は、id・case（事件名）・op・reason（直す理由と確かめた日）と、opごとの項目で書きます。

- remove_file：事件から話を外す（volume・index）。2つの事件に重なって載っている話に使う
- rename_title：話タイトルの誤りを直す（volume・index・from・to。from・toは「」も含めてConanData.jsonの表記のまま書く）
- add_main／add_guest：メイン・ゲストキャラを足す（name。afterに人物名を書くとその後ろ、beforeならその前に入れる）
- rename_guest：ゲストキャラの呼び名を、編纂室がほかの事件で使っている名前にそろえる（from・to）
- remove_main／remove_guest：編纂室の一覧にあるが原作に出ない人物を外す（name）

noteに消す時期などの注意書き（単行本の発売前の暫定パッチなど）を書くと、実行のたびに表示されます。

# ConanData.pyとPatchData.pyと上5ファイルを一気に実行する方法

以下のコマンドを実行してください。
```sh
.\all.bat
```
