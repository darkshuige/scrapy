# @Time : 2024/1/9 0:29
# __VIEWSTATE: oK4pgocguvMjbkKYNrtSJrVnO7UERQOA5EUi0fnjEHS/vsuCQyGo4BOGBJffIpoXCnftLDAY7v3bKAf2/uPhsmH5do47j9dUQJLrO9eUo77nwnMQ0YzvSubYXjTv9Qa3PnBfjE4SpKMfwVmFAJ+EOwAIAtQ=
# __VIEWSTATEGENERATOR: C93BE1AE
# from: http://so.gushiwen.cn/user/collect.aspx
# email: 1597590247@qq.com
# pwd: 45646456464
# code: qqqq
# denglu: 登录
import requests
from bs4 import BeautifulSoup
url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}
response = requests.get(url=url,headers=headers)
content = response.content
soup = BeautifulSoup(content,'lxml')
VIEWSTATE = soup.select('#__VIEWSTATE')[0].attrs.get('value')
VIEWSTATEGENERATOR = soup.select('#__VIEWSTATEGENERATOR')[0].attrs.get('value')
code_url = 'http://so.gushiwen.cn' + soup.select('#imgCode')[0].attrs.get('src')
session = requests.session()
response_code = session.get(code_url)
content_code = response_code.content
with open('code.jpg','wb') as fp:
    fp.write(content_code)
code_name = input('请输入验证ma:')
url_post = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'
data_post = {
    '__VIEWSTATE': VIEWSTATE,
    '__VIEWSTATEGENERATOR': VIEWSTATEGENERATOR,
    'from': 'http://so.gushiwen.cn/user/collect.aspx',
    'email': '1597590247@qq.com',
    'pwd': 'a113464',
    'code': code_name,
    'denglu': '登录',
}
response_post = session.post(url=url,headers=headers,data=data_post)
content_post = response_post.text
with open('gushiwen.html','w',encoding='utf8') as fp:
    fp.write(content_post)
