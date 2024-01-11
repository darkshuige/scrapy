# @Time : 2024/1/6 1:33
# 第一页 https://sc.chinaz.com/tupian/siwameinvtupian.html
#第二页  https://sc.chinaz.com/tupian/siwameinvtupian_2.html
import urllib.request
from lxml import etree
def creat_request(page):
    if(page==1):
        url='https://sc.chinaz.com/tupian/siwameinvtupian.html'
    else:
        url='https://sc.chinaz.com/tupian/siwameinvtupian_'+str(page)+'.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
    }
    request=urllib.request.Request(url=url,headers=headers)
    return request
def get_content(request):
    response=urllib.request.urlopen(request)
    content=response.read().decode('utf8')
    return content
def down_load(page,content):
    tree=etree.HTML(content)
    name_list=tree.xpath('//div[@class="container"]//img/@alt')
    src_list=tree.xpath('//div[@class="container"]//img/@data-original')
    for i in range(len(name_list)):
        name=name_list[i]
        src=src_list[i]
        url='https:'+src
        urllib.request.urlretrieve(url=url,filename='./站长素材图片/'+name+'.jpg')
if __name__ == '__main__':
    start_page=int(input('请输入起始页'))
    end_page=int(input('请输入结束页'))
    for page in range(start_page,end_page+1):
        request=creat_request(page)
        content=get_content(request)
        down_load(page,content)