# @Time : 2024/1/5 15:59
from lxml import etree
#本地文件 etree.parse
#服务器   etree.HTML()\
tree=etree.parse('xpath的基本使用.html')
li_list=tree.xpath('//li[@id="li2"]/@class')
print(li_list)
print(len(li_list))