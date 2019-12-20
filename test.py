import requests

from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# 書類一覧APIのエンドポイント
url = "https://disclosure.edinet-fsa.go.jp/api/v1/documents.json"

# 書類一覧APIのリクエストパラメータ
params = {
  "date" : "2019-04-25",
  "type" : 2
}

# 書類一覧APIの呼び出し
res = requests.get(url, params=params, verify=False)

# レスポンス（JSON）の表示
print(res.text)