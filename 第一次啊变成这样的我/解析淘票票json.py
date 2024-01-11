# @Time : 2024/1/6 20:33
import urllib.request
url='https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1704544714357_108&jsoncallback=jsonp109&action=cityAction&n_s=new&event_submit_doGetAllRegion=true'
headers={
    # ':authority': 'dianying.taobao.com',
    # ':method': 'GET',
    # ':path': '/cityAction.json?activityId&_ksTS=1704544714357_108&jsoncallback=jsonp109&action=cityAction&n_s=new&event_submit_doGetAllRegion=true',
    # ':scheme': 'https',
    'accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'bx-v': '2.5.6',
    'cookie': 't=f795ea8786ead503f9bd8c232a9c6089; cookie2=19c498df025cfa70df982c40ab04cc58; v=0; _tb_token_=e3de30dee43b5; cna=5TYgHn5W3mUCAXAOTawGVR4K; xlly_s=1; l=fBxe2ykuPAyxERBdBO5Clurza7796Idb8sPzaNbMiIEGa61P9FG2oNCOCKFMWdtjgTCv2e-zmSrNYd36lEadAxDDBeV-1NK0gxvtaQtJe; tfstk=eULp306QDAD3HewVj2nian4FQ7himedEtpRbrTX3Vdp93phFqkxH28B9GXWn4DJJXL9Nx9TJazCWNLlFEXoMTB7PPxDceqAeTfHC_ug0fBU2AaMmnVqg1MkhPHV9YnSf_qnIf5z2CU1IDWc5rkb246IdezXTyG8_oM6jnOa8y9CdvWACBzaWWg8MoE3KU-XAZkGt6urPA1WPuSOLt3Q7D1BmsCqz4Gmf6tct6urPA15OnfXg4uSic; isg=BEREMC5a_a6Tu0niRjOSHXgYFcI2XWjHNKC1hl7lDo_SieVThmsPV2FvySFRkaAf',
    'referer': 'https://dianying.taobao.com/',
    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}
request=urllib.request.Request(url=url,headers=headers)
response=urllib.request.urlopen(request)
content=response.read().decode('utf-8')
content=content.split('(')[1].split(')')[0]
with open('解析淘票票的json.json','w',encoding='utf-8') as fp:
    fp.write(content)

import json
import jsonpath
obj=json.load(open('解析淘票票的json.json','r',encoding='utf8'))
city_list=jsonpath.jsonpath(obj,'$..regionName')
print(city_list)
