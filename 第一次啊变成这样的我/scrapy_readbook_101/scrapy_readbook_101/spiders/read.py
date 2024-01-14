import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_readbook_101.items import ScrapyReadbook101Item

class ReadSpider(CrawlSpider):
    name = "read"
    allowed_domains = ["www.dushu.com"]
    start_urls = ["https://www.dushu.com/book/1611_1.html"]

    rules = (Rule(LinkExtractor(allow=r"/book/1611_\d+\.html"), callback="parse_item", follow=True),)

    def parse_item(self, response):
        img_list = response.xpath('//div[@class="book-info"]/div/a/img')
        for img in img_list:
            name = img.xpath('./@alt').extract_first()
            src =img.xpath('./@data-original').extract_first()
            book = ScrapyReadbook101Item(name=name,src=src)
            yield book
