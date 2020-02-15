# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoutuItem(scrapy.Item):
    title = scrapy.Field()

    pic_url = scrapy.Field()
