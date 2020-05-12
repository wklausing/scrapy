import scrapy
import pdfkit


class BerkshireSpider(scrapy.Spider):
    name = "berkshire"
    start_urls = [
        'https://www.berkshirehathaway.com/letters/letters.html'
    ]


    def parse(self, response):
        filename = 'berkshire-letters.html'
        domain = 'https://www.berkshirehathaway.com/letters/'
        responseData = response.css('table.MsoNormalTable a').re("(?:[0-9]{4}.*[html|pdf])")
        f = open(filename, 'w')
        for data in responseData:
            f.write(data + '\n')
            #Download as pdf
            path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
            config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
            letterUrl = domain + data
            pdfkit.from_url(letterUrl, data + '.pdf', configuration=config)
        self.log('Saved file %s' % filename)










#response.css('table.MsoNormalTable a').re("(?:[0-9]{4}.*[html|pdf])")
#scrapy crawl berkshire -o berkshire.jl
