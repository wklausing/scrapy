import scrapy

class BerkshireSpider(scrapy.Spider):
    name = "berkshire"
    start_urls = [
        'https://www.berkshirehathaway.com/letters/letters.html'
    ]

    def parse(self, response):
        filename = 'berkshire-letters.html'
        responseData = response.css('table.MsoNormalTable a').re("(?:[0-9]{4}.*[html|pdf])")

        f = open(filename, 'w')
        for data in responseData:
            f.write(data + '\n')
        self.log('Saved file %s' % filename)







#response.css('table.MsoNormalTable a').re("(?:[0-9]{4}.*[html|pdf])")
#scrapy crawl berkshire -o berkshire.jl
