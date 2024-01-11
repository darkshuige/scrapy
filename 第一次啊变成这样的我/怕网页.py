# @Time : 2023/12/17 14:57
import urllib.request
url='https://www.baidu.com/'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
}
a=urllib.request.Request(url=url,headers=headers)
response=urllib.request.urlopen(a)
content=response.read().decode('utf-8')
print(content)