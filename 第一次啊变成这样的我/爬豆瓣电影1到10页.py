# @Time : 2024/1/4 19:36
import urllib.parse
import urllib.request
def creat_request(page):
    base_url='https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
    }
    date={
        'start':(page-1)*20,
        'limit':20
    }
    data=urllib.parse.urlencode(date)
    url=base_url+data
    request=urllib.request.Request(url=url,headers=headers)
    return request
def get_content(request):
    response=urllib.request.urlopen(request)
    content=response.read().decode('utf-8')
    return content;
def down_load(page,content):
    with open('douban'+str(page)+'.json','w',encoding='utf-8') as fp:
        fp.write(content)

if __name__ == '__main__':
    start_page=int(input('请输入起始页码'))
    end_page=int(input('请输入结束页码'))
    for page in range(start_page,end_page+1):
        request=creat_request(page)
        content=get_content(request)
        down_load(page,content)
