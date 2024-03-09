## 使用方法
1. Deepgram API keyを作成する（https://console.deepgram.com/project/bc7dd3ce-c0c8-457a-8d1a-d1930e235fd9/keys）
2. python用のdeepgram-sdkをターミナルからインストール（pip install deepgram-sdk）
3. このリポジトリをクローンする
4. このリポジトリ内にlocal_settings.pyファイルを作成
5. ファイル内にAPI Keyを記載 (DEEPGRAM_API_KEY = 'your_api_key')
6. ターミナルで"py -3.11 bias.py" or "python bias.py"を実行

## 使用要件
Deepgram-sdk 2.12.0をインストール
python 12以外なら動く？

## メモ
音声ファイルのパスをファイルに直書きしているのでlocal_settings.pyに記載する形に変更する
