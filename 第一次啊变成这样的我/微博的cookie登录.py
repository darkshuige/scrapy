# @Time : 2024/1/5 13:26
import urllib.parse
import urllib.request
url='https://weibo.cn/comment/NApaz4kmN?ckAll=1'
headers={
    # ':authority': 'weibo.cn',
    # ':method': 'GET',
    # ':path': '/comment/NApaz4kmN?ckAll=1',
    # ':scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    'cookie': '_T_WM=921f859cc319f44ae3c96b9a9fcbdbf2; MLOGIN=1; M_WEIBOCN_PARAMS=luicode%3D20000174; SUB=_2A25Ik-ucDeRhGeFG6loZ9inKzT6IHXVr0WFUrDV6PUJbkdCOLWfMkW1NfjR3PJmc7Wm3M7VxPHUrjz7s9cUJSv1P; SCF=Anhrzy7kEGBvMenMkdNxQeIZ3sWUR-HTn_JEt141qaJm4xi33sLOt5t-dVnDAEq_5OqWdOTsWWCyCEeEZ_MtD8A.; SSOLoginState=1704434637',
    'referer': 'https://weibo.cn/u/2671109275',
    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}
request=urllib.request.Request(url=url,headers=headers)
response=urllib.request.urlopen(request)
content=response.read().decode('utf-8')
with open('weibo.html','w',encoding='utf-8') as fp:
    fp.write(content)
