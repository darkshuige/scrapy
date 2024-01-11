# @Time : 2023/12/17 15:39
import urllib.request
import urllib.parse
import json
headers={
    'Accept': '*/*',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Acs-Token': '1702785669236_1702800085008_2Hhtq6HW4wBqVS4gOHPWap8TZBkwkbDlWLOaDunmbQWnmd3d2nE8smWckC+GmqrOuAkTAnvCJStjimrmaWqPzMxSZrA2sigULLzXk7fS3lzZWyFSoPuc/SAQ4Bkc9tfGeb4IWNMDsf0qSlcgbav1BNAvPiGQPe0zNv3cGHwGoAQgDv67VbGsMb4ERAd0T7Am8oID3cyWWUmr1j38LFFrQ0NjlUu4GUifwrtInZsJvQxXTNxotv8r5B4uSwuD9Kk6n6HBGI+pZMb/sC4tF3RVxupDkz8MMQFJ0F3DA/LZcfiSRfEfGFi0SPhnGr6G+CQvKLzsLRDh+fWmVp8CRy+GRLx6YZIZ0HBaCBwFTR6rus+vqG2xteWo5AtHKjPKNyrygoIhHAbJYSVftipFpXGkiiDLmYt3HQVSF0MnnQt/pn51xlkYrk0KqrgEiucCkNFy56w7na52MVIr0QALPlwhSuRqx9woG8+b08rFDPrLueYlzsF9/ucGLwCWa9f5yB1h',
    'Connection': 'keep-alive',
    'Content-Length': '153',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'BAIDUID=DD2D6BA53605E57D58E6642CC6284C52:FG=1; BAIDUID_BFESS=DD2D6BA53605E57D58E6642CC6284C52:FG=1; __bid_n=1869d596520e62299d4207; BDUSS=VuTTdVS2VvTHdleWNyTTRacC1STXFUampEbFJ3VFlQRmJHbXA2ODJ3ZllDQ2RrSVFBQUFBJCQAAAAAAAAAAAEAAABoE~HQZGFya3NodWlnZQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANh7~2PYe~9jYV; BDUSS_BFESS=VuTTdVS2VvTHdleWNyTTRacC1STXFUampEbFJ3VFlQRmJHbXA2ODJ3ZllDQ2RrSVFBQUFBJCQAAAAAAAAAAAEAAABoE~HQZGFya3NodWlnZQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANh7~2PYe~9jYV; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1677819162,1677997821,1678003420,1678265353; BAIDU_WISE_UID=wapp_1678335824248_357; FPTOKEN=FpPDst4VCVVrOn7pwb3cTME5nMeDw5MACZXavcfWgbzUHUB8QwTshkTkOZ3nKP2QEMVwFHCxFC5ufIbCLG5ekpWEp+IxXEs3f526JP8jlM7FeGoy9znYDrvO/N30yq/pwFw2hY0vCwwEd5fXmdhXYZwfCQksDZe4dapsbFjussNXMEbEx1NtVAPe4ICmu9MBtx7hAGP1FyOB4SppR/43/hj+Wwl+y3ROJ+aQTUlEczmpvY7gOXgFVkCQuYsKzvHHmfAds9PPVJcmuJktUA9REoj205frd6ThzIkuAq5Ni8INoxAL2VRVQqUOjZuyalKnqBGuBmAfVnzIx2YRtT8CqX2meuzu+iR+unCN7hzHsjhAXDRWGelvH7IQPtk0UJ0KNweAUs4lzwbRL8dk+FKXJA==|DLzQ8Hj4SKnqOlYDohOJGSTQEsGOKB2P+fr2wukz8F4=|10|39efb47eea64e79c09eccc19423f0e82; APPGUIDE_10_6_6=1; APPGUIDE_10_6_9=1; ZFY=LwI4XY:AYZPU9G6fMKbT8TD5LCdYi3QVWAF6mfgHd9Vo:C; BIDUPSID=DD2D6BA53605E57D58E6642CC6284C52; PSTM=1702477660; arialoadData=false; RT="z=1&dm=baidu.com&si=c5b2ee2a-034a-4d01-ad98-ba7c123713dd&ss=lq83qadj&sl=3&tt=744&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=9w0&ul=4fet&hd=4ff5"; H_PS_PSSID=39713_39834_39839_39903_39819_39909_39934_39937_39933_39942_39941_39939_39930_39732_39783_39974_39662; BA_HECTOR=0500akal250425a4a1a1a02g1int6hr1q; ab_sr=1.0.1_YzE5OTAwZDk1NDg1ZTFiYjMzMmM2ZGNlYWI2ODQ5YTJiZmZmYWZkNDc2OWU0NjgzZTJkY2E3YTk3ZmQ0Yzc2ZWFlNzBkNTk2YjIxMzBlZGZiZmYzYTI0ZjE5MTFjZjg1OGM3ZjE5YTk0NTY1NzNlY2Y2Zjc2YmMzOWRmZjBkMWQzODRkYjBjODUxYjBjZGNmY2FhMjZiZWI4NGM3NDlhYmIyZjJiYzU4YjJkODBkMmQ3ZThkZmMyMDgyYTIyYzJh',
    'Host': 'fanyi.baidu.com',
    'Origin': 'https://fanyi.baidu.com',
    'Referer': 'https://fanyi.baidu.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Microsoft Edge";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
url='https://fanyi.baidu.com/v2transapi?from=en&to=zh'
data={
    'from': 'en',
    'to': 'zh',
    'query': 'spider',
    'transtype': 'realtime',
    'simple_means_flag': '3',
    'sign': '63766.268839',
    'token': 'e34e250ebbf4d5f7f0db3e972ac3cb38',
    'domain': 'common',
    'ts': '1702800084985',
}
data=urllib.parse.urlencode(data).encode('utf-8')
request=urllib.request.Request(url=url,data=data,headers=headers)
response=urllib.request.urlopen(request)
content=response.read().decode('utf-8')
print(content)