# -*- coding: utf-8 -*-
import scrapy
from doutu.items import DoutuItem

class DoutulaSpider(scrapy.Spider):
    name = 'doutula'
    allowed_domains = ['bbsnet.com']
    start_urls = ['http://www.bbsnet.com/']

    def parse(self, response):
        lis = response.xpath("//div[@class='mainleft']//li")
        for li in lis:
            title = li.xpath(".//h2/a/@title").get()
            link = li.xpath(".//h2/a/@href").get()
            yield scrapy.Request(url=link,callback=self.parse_link,meta={'info':title})

        next_url = response.xpath("//div[@class='navigation container']/div[@class='pagination']/a[@class='next']/@href").get()
        if next_url:
            yield scrapy.Request(url=next_url,callback=self.parse)



    def parse_link(self,response):
        title = response.meta.get('info')
        ps = response.xpath("//div[@id='post_content']/p")
        for p in ps:
            pic_url = p.xpath(".//img/@src").get()
            print(pic_url)

            yield DoutuItem(pic_url=pic_url,title=title)








