# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class LsmrSpiderItem(scrapy.Item):
    '''定义需要格式化的内容（或是需要保存到数据库的字段）'''

    name = scrapy.Field()   #修改你所需要的字段
    url = scrapy.Field()

class LrldSpiderItem(scrapy.Item):
    name = scrapy.Field()
    lb = scrapy.Field()
    rzsj = scrapy.Field()
    zwmc = scrapy.Field()
    rzdmc = scrapy.Field()

class XrldSpiderItem(scrapy.Item):
    name = scrapy.Field()
    zwmc = scrapy.Field()

class XsyqSpiderItem(scrapy.Item):
    fssj = scrapy.Field()

class ZmxzSpiderItem(scrapy.Item):
    name = scrapy.Field()
    zwmc = scrapy.Field()