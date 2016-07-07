import sys
import csv
import scrapy
from markov_python.cc_markov import MarkovChain
from scrapy.http import FormRequest
from scrapy.crawler import CrawlerProcess


class MyItem(scrapy.Item):
    test = scrapy.Field()


class Spider(scrapy.Spider):
    start_urls = [
        "blah.com",
    ]

    def parse(self, response):
        blahblah = MyItem()
        # Some Code
        yield blahblah


class crawler:
    def start(self):
        process = CrawlerProcess({
            'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
            'LOG_LEVEL': 'INFO',
            'FEED_FORMAT': 'csv',
            'FEED_URI': 'Output.csv'
        })
        process.crawl(Spider)
        process.start()

app = crawler()
app.start()