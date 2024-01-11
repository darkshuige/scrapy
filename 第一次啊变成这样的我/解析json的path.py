# @Time : 2024/1/6 17:39
import jsonpath
import json
obj=json.load(open('解析json的path.json','r',encoding='utf-8'))
author_list=jsonpath.jsonpath(obj,'$.store.book[*].author')

book_list=jsonpath.jsonpath(obj,'$..book[?(@.price>10)]')
print(book_list)