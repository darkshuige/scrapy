import scrapy


class BaiduSpider(scrapy.Spider):
    name = "baidu"
    allowed_domains = ["www.baidu.com"]
    start_urls = ["http://www.baidu.com"]

    def parse(self, response):
        print('我带你们打')
