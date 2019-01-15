#-*- coding:UTF-8 -*-
'''
Created on 2019/01/15

@author: T.Wakasugi
'''

import requests
from urllib import quote, quote_plus

#指定したURLに対するGETリクエスト
url = 'http://www.webscrapingfordatascience.com/paramhttp/?query=a query with a space'
r = requests.get(url)

#サーバーから返されたHTTPステータスコード
print(r.status_code)
#テキストのステータスメッセージ
print(r.reason)
#HTTPレスポンスヘッダー
print(r.headers)
#リクエスト情報はr.requestにPythonオブジェクトとして保存される
print(r.request)
#HTTPリクエストヘッダー
print(r.request.headers)
#HTTPレスポンスのコンテンツ
print(r.text)

print
print('-------')
print

raw_string = 'a query with /, space and?&'

#特殊文字をエンコードしてくれる
print(quote(raw_string))
print(quote_plus(raw_string))

print
print('-------')
print

url = 'http://www.webscrapingfordatascience.com/paramhttp/?query='

print('¥nUsing quote:')
#「/」も含め安全な文字はないので、全てエンコードする
r = requests.get(url + quote(raw_string, safe=''))
print(r.url)
print(r.text)
print('¥nUsing quote_plus:')
r = requests.get(url + quote_plus(raw_string, safe=''))
print(r.url)
print(r.text)
