# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os
from urllib import request
import random
class DoutuPipeline(object):
    def __init__(self):
        self.path = os.path.join(os.path.dirname(os.path.dirname(__file__)),'表情包')
        if not os.path.exists(self.path):
            os.mkdir(self.path)

    def process_item(self, item, spider):
        title = item['title']
        pic_url = item['pic_url']
        title_path = os.path.join(self.path,title)
        if not os.path.exists(title_path):
            os.mkdir(title_path)
        pic_name = pic_url.split('.')[-1]
        gfe = ['one','two','three','four','five','six','seven','eight','nene']
        name = str(random.choice(gfe))
        title = name + '.' + pic_name
        request.urlretrieve(pic_url, title_path+'/'+title)
        return item
