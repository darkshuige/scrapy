# @Time : 2024/1/8 16:11
from selenium import webdriver
import time
path = 'chromedriver.exe'
browser = webdriver.Chrome(path)
url = 'https://www.baidu.com'
browser.get(url)
time.sleep(2)
input = browser.find_element_by_id('kw')
input.send_keys('周杰伦')
time.sleep(2)
button = browser.find_element_by_id('su')
button.click()
time.sleep(2)
js_bottom = 'document.documentElement.scrollTop=100000'
browser.execute_script(js_bottom)
time.sleep(2)
next = browser.find_element_by_xpath('//a[@class="n"]')
next.click()
time.sleep(2)
browser.back()
time.sleep(1)
browser.forward()
time.sleep(1)
browser.quit()