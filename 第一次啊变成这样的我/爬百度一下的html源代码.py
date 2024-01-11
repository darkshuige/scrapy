# @Time : 2023/12/13 22:23
import urllib.request
import urllib.parse
url='https://cn.bing.com/search?'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
}
data={
    'q':'蔡徐坤',
    'form':'ANNTH1',
}
url+=urllib.parse.urlencode(data)
request=urllib.request.Request(url=url,headers=headers)
response=urllib.request.urlopen(request)
content=response.read().decode('utf-8')
print(url)
print(content)