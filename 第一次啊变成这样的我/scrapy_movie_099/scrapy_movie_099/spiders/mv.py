import scrapy
from scrapy_movie_099.items import ScrapyMovie099Item

class MvSpider(scrapy.Spider):
    name = "mv"
    allowed_domains = ["www.dy2018.com"]
    start_urls = ["https://www.dy2018.com/?wangan=3c7d8877d44c77accca5232163f7e6e721642514809_85681"]

    def parse(self, response):
        a_list = response.xpath('//div[@class="index_list"]/div/div[2]/ul/li/a')
        for a in a_list:
            name = a.xpath('./text()').extract_first()
            url = 'https://www.dy2018.com' + str(a.xpath('./@href').extract_first())
            yield scrapy.Request(url=url,callback=self.parse_second,meta={'name':name})

    def parse_second(self,response):
        src = response.xpath('//div[@id="Zoom"]/img[1]/@src').extract_first()
        name = response.meta['name']
        movie = ScrapyMovie099Item(src=src,name=name)
        yield movie