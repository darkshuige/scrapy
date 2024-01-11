import scrapy


class CarSpider(scrapy.Spider):
    name = "car"
    allowed_domains = ["www.autohome.com.cn"]
    start_urls = ["https://www.autohome.com.cn/p/"]

    def parse(self, response):
        name_list = response.xpath('//ul[@class="rank-list-ul"]//li//h4/a/text()')
        for name in name_list:
            print(name.extract())
