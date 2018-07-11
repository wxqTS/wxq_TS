# coding=utf-8
import scrapy
import re
import os
import urllib
import pymysql
import sys
from scrapy.selector import Selector
from scrapy.http import HtmlResponse, Request
from webCrawler_scrapy.items import  XsyqSpiderItem

class XsyqSpider(scrapy.spiders.Spider):
    name = 'xsyq'
    allowed_domains = ["bnu.edu.cn"]
    start_urls = ["http://www.bnu.edu.cn/xxgk/xsyg/index.htm" ]

    def parse(self, response):
        se = Selector(response)  # 创建查询对象，HtmlXPathSelector已过时
        src = response.xpath("//div[@class='history_row clear']/p")
        for i in range(len(src)):
            ii = i+1
            item = XsyqSpiderItem()
            item['fssj'] = se.xpath("//div[@class='history_row clear']/p[%d]/text()" % ii).extract()
            yield item  # 返回item,这时会自定解析item

