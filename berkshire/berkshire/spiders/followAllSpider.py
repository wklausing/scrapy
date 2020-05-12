import scrapy

class FollowAllSpider(scrapy.Spider):
    name = 'follow_all'

    start_urls = ['https://example.com']
    rules = [Rule(LinkExtractor(), callback='parse_item', follow=True)]

    def parse_item(self, response):
        pass
