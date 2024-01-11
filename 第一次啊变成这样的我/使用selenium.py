# @Time : 2024/1/8 2:40
from selenium import webdriver
path = 'chromedriver.exe'
browser = webdriver.Chrome(path)
url = 'https://www.jd.com'
browser.get(url)
content = browser.page_source
print(content)