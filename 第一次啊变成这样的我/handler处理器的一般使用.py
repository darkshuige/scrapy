# @Time : 2024/1/5 14:52
import urllib.parse
import urllib.request
url='http://www.baidu.com'
headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}
request=urllib.request.Request(url=url,headers=headers)

#response=urllib.request.urlopen(request)
handler=urllib.request.HTTPHandler()
opener=urllib.request.build_opener(handler)
response=opener.open(request)

content=response.read().decode('utf-8')
print(content)
