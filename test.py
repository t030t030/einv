import requests

# 書類管理番号
docid = "S100H7TT"

# 書類取得APIのエンドポイント
url = "https://disclosure.edinet-fsa.go.jp/api/v1/documents/" + docid

# 書類取得APIのリクエストパラメータ
params = {
  "type" : 2
}

# 出力ファイル名
filename = docid + ".zip"

# 書類取得APIの呼び出し
res = requests.get(url, params=params, verify=False)

# ファイルへ出力
if res.status_code == 200:
  with open(filename, 'wb') as f:
    for chunk in res.iter_content(chunk_size=1024):
      f.write(chunk)