# @Time : 2024/1/8 15:36
from selenium import webdriver
path = 'chromedriver.exe'
browser = webdriver.Chrome(path)
url = 'https://www.baidu.com'
browser.get(url)
input =browser.find_element_by_id('su')
print(input.get_attribute('class'))