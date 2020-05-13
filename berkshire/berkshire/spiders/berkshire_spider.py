import scrapy
import pdfkit
import wget
from os import listdir
from os.path import isfile, join
from PyPDF2 import PdfFileMerger
import re


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
            letterUrl = domain + data
            if (data.endswith("html")):
                #Download as pdf
                path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
                config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
                pdfkit.from_url(letterUrl, data + '.pdf', configuration=config)
                self.log('Saved html file %s' % data)
            elif (data.endswith("pdf")):
                wget.download(letterUrl, 'C:/Users/Peter/git/scrapy/berkshire/' + data)
                self.log('Saved pdf file %s' % data)
        self.log('Downloading is done. Pdf merging start now.')
        self.pdfMerger()
        self.log('For loop done. Files are in C:/Users/Peter/git/scrapy/berkshire/.')

    def pdfMerger(self):
        path = 'C:/Users/Peter/git/scrapy/berkshire/'
        pattern = re.compile("(?:[0-9]{4}.*[html|pdf])")
        pdfs = [f for f in listdir('C:/Users/Peter/git/scrapy/berkshire/.') if
                isfile(join('C:/Users/Peter/git/scrapy/berkshire/.', f))]
        merger = PdfFileMerger()
        lastYear = 'ErrorYear'
        for pdf in pdfs:
            if (pattern.match(pdf)):
                merger.append(path + pdf)
                print('Merge append with ' + pdf)
                lastYear = pdf[0:4]
        print('LastYear: ' + lastYear)
        merger.write("BerkshireHathawayLetters" + lastYear + ".pdf")
        merger.close()




#response.css('table.MsoNormalTable a').re("(?:[0-9]{4}.*[html|pdf])")
#scrapy crawl berkshire -o berkshire.jl
