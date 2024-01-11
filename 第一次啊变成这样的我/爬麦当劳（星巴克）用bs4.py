# @Time : 2024/1/7 13:18
import urllib.request
from bs4 import BeautifulSoup
url = 'https://www.mcdonalds.com.cn/index/Food/menu/burger'
response = urllib.request.urlopen(url)
content = response.read().decode('utf8')
soup = BeautifulSoup(content,'lxml')
#//div[@class="col-md-3 col-sm-4 col-xs-6"]//span/text()
name_list = soup.select('div[class="col-md-3 col-sm-4 col-xs-6"] span')
for name in name_list:
    print(name.string)