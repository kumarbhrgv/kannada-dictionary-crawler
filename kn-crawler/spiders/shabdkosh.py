import scrapy
from scrapy.selector import Selector 
from scrapy.http import HtmlResponse
import os

class ExampleSpider(scrapy.Spider):
    name = "shabdkosh"

    def start_requests(self):
        alphabets = ['\u0C85','\u0C86','\u0C87','\u0C88','\u0C89','\u0C8A','\u0C8B','\u0C8C','\u0C8E','\u0C8F','\u0C90','\u0C92','\u0C93','\u0C94','\u0C95','\u0C96','\u0C97','\u0C98','\u0C99','\u0C9A','\u0C9B','\u0C9C','\u0C9D','\u0C9E','\u0C9F','\u0CA0','\u0CA1','\u0CA2','\u0CA3','\u0CA4','\u0CA5','\u0CA6','\u0CA7','\u0CA8','\u0CAA','\u0CAB','\u0CAC','\u0CAD','\u0CAE','\u0CAF','\u0CB0','\u0CB1','\u0CB2','\u0CB3','\u0CB5','\u0CB6','\u0CB7','\u0CB8','\u0CB9']
        
        urls=[]
        baseUrl = 'http://www.shabdkosh.com/kn/browse/'
        for letter in alphabets:
        	for i in range(1,10):
        		urls.append(baseUrl+letter+'/'+str(i))
        self.log(urls)
        for url in urls:
        	yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-1]
        letter = response.url.split("/")[-2]
        filename = 'kannada.txt' 
        #%(letter,page)
        with open(filename, 'a+b') as f:
            for line in response.xpath('//div[@class = "col-sm-3"]/a/text()').extract():
            	line = line + "\n"
            	line = line.encode('UTF-8')
            	f.write(line)
        f.close()
        self.log('Saved file %s' % filename)