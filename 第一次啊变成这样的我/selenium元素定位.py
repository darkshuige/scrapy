# @Time : 2024/1/8 15:28
from selenium import webdriver
path = 'chromedriver.exe'
browser = webdriver.Chrome(path)
url = 'https://www.baidu.com'
browser.get(url)
button = browser.find_element_by_id('su')
print(button)