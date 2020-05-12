import scrapy

class BerkshireSpider(scrapy.Spider):
    name = "hathaway"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        filename = 'berkshire-letters.html'
        responseData = response.css('table.MsoNormalTable a').re("(?:[0-9]{4}.*[html|pdf])")

        f = open(filename, 'w')
        for data in responseData:
            f.write(data + '\n')
        self.log('Saved file %s' % filename)





#response.css('table.MsoNormalTable a').re("(?:[0-9]{4}.*[html|pdf])")
#scrapy crawl hathaway -o hathaway.jl
