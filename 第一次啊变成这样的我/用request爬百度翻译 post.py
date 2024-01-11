# @Time : 2024/1/8 20:35
import requests
import  urllib.request
import urllib.parse
url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'
headers={
       'Accept': '*/*',
       'Accept-Language': 'zh-CN,zh;q=0.9',
       'Acs-Token': '1704712100874_1704726335416_Y2WfgJXET4rjbhs0xoOA+RuGhsbBYjb5/aG6TFN6sjnUUNulvLxLe+z07KvGzxjWlUmpx0DqhjEiMCKeCnCRM/DGwAgHn4ewH92K4UAunVx9CwfDReDM5GgTW5HYFAtQ0JOD1SR4yGlWxH7G9L09b9bO/lp7RBP8jndUdRrfF5y+18V/O2psdDUPu9QItCjiqBT8nPLhUW1VfA/D7uaE1hofsuWJxfYuzPHlxi72W7ZSvS+nK7QPxXoSlhKDYwyWazFuPdOiI/J0n+NQcmk1JXpYk1uzWOLDJFf01bip8xYPqopeHcDI8tFijJN4vA/ijx2amUZYfcMPoqkt6ZCn7hYGR99MhV6BwIyZKv4cNt8dCG9Xw1SrnfMHZxybcAjKdx+5PtL7hbI1ocuSI0OZ4QTPvs6pk/Py+ZddhrD+r7j//BtoJp6Ame5UDxXGxaOxNtdlnvOcp5KwEY2xE7o1E+LVGEgc+yiqKPUNomra4u8=',
       'Connection': 'keep-alive',
       'Content-Length': '132',
       'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
       'Cookie': 'PSTM=1704701629; BAIDUID=AC9A2E51E08BF26DE5869F55D733288B:FG=1; BIDUPSID=47971AA86116264EDCCCA11A88CF3A10; BA_HECTOR=al84052181a52g8ha405058hurj9u21ipnblu1s; BAIDUID_BFESS=AC9A2E51E08BF26DE5869F55D733288B:FG=1; ZFY=EPYnyxtel:B8:A8306XHNn:Bk3v:AAADoHR1IwnRA:BvZYS4:C; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=40009_40043; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1704716738,1704726325; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1704726335; ab_sr=1.0.1_MWVmYzIxMTViYWUzYTlhZWY4YzJlZWUxNzIxMTAyYzlhMmZlOTQ4YmQzMzA4MjJiYzI1M2RiYTVlNzc0MDM4Mjk4N2NmNmE1MTQ0NTAxNTJkMTg2NTUyZmU4ZTRjNmJhNWQ3NjZhNDI0YTI0OWZhNjVhZDcyMzUxMDc1OTQyMWQxZmY0MmE1ZjExYjk4YjUyNzhlNTU5Y2MxMjdmODVhNA==',
       'Host': 'fanyi.baidu.com',
       'Origin': 'https://fanyi.baidu.com',
       'Referer': 'https://fanyi.baidu.com/?aldtype=16047',
       'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
       'sec-ch-ua-mobile': '?0',
       'sec-ch-ua-platform': '"Windows"',
       'Sec-Fetch-Dest': 'empty',
       'Sec-Fetch-Mode': 'cors',
       'Sec-Fetch-Site': 'same-origin',
       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
       'X-Requested-With': 'XMLHttpRequest',
}
data = {
       'from': 'en',
       'to': 'zh',
       'query': 'luck',
       'simple_means_flag': '3',
       'sign': '278635.41818',
       'token': 'd6183b4ff3a2a8c3cd0c1b321fc81503',
       'domain': 'common',
       'ts': '1704726335403',
}
response = requests.post(url=url,data=data,headers=headers)
content = response.text
print(type(content))
import json
print(json.loads(content))
# data=urllib.parse.urlencode(data).encode('utf-8')
# request=urllib.request.Request(url=url,data=data,headers=headers)
# response=urllib.request.urlopen(request)
# content=response.read().decode('utf-8')
# print(content)