import scrapy
from scrapy_dangdang_095.items import ScrapyDangdang095Item

class DangSpider(scrapy.Spider):
    name = "dang"
    allowed_domains = ["category.dangdang.com"]
    start_urls = ["http://category.dangdang.com/cp01.01.02.00.00.00.html"]
    base_url = 'https://category.dangdang.com/pg'
    page = 1
    def parse(self, response):
        # scr = '//ul[@id="component_59"]/li/a/img/@data-original'
        # alt = '//ul[@id="component_59"]/li/a/img/@alt'
        # price ='//ul[@id="component_59"]/li/p/span[@class="search_now_price"]/text()'
        li_list = response.xpath('//ul[@id="component_59"]/li')
        for li in li_list:
            scr = li.xpath('./a/img/@data-original').extract_first()
            if scr:
                src = scr
            else:
                scr = li.xpath('./a/img/@src').extract_first()
            name = li.xpath('./a/img/@alt').extract_first()
            price = li.xpath('./p/span[@class="search_now_price"]/text()').extract_first()
            book = ScrapyDangdang095Item(scr=scr,name=name,price=price)
            yield book
        if self.page < 100:
            self.page = self.page + 1
            url = self.base_url + str(self.page) + '-cp01.01.02.00.00.00.html'
            yield scrapy.Request(url=url,callback=self.parse)
