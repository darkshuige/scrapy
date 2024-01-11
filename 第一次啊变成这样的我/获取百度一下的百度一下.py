# @Time : 2024/1/5 17:05
from lxml import etree
import urllib.request
#本地文件 etree.parse
#服务器   etree.HTML()\
url='https://www.baidu.com/'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
}
request=urllib.request.Request(url=url,headers=headers)
response=urllib.request.urlopen(request)
content=response.read().decode('utf-8')
tree=etree.HTML(content)
result=tree.xpath('//input[@id="su"]/@value')
print(result)