# coding=utf-8
import scrapy
import re
import os
import urllib
import pymysql
import sys
from scrapy.selector import Selector
from scrapy.http import HtmlResponse, Request
from webCrawler_scrapy.items import  XrldSpiderItem

class XrldSpider(scrapy.spiders.Spider):
    name = 'xrld'
    allowed_domains = ["bnu.edu.cn"]
    start_urls = ["http://www.bnu.edu.cn/xxgk/xrld/index.htm" ]

    def parse(self, response):
        se = Selector(response)  # 创建查询对象，HtmlXPathSelector已过时
        src_a = response.xpath("//div[@class='leader_row']" )
        print("----------------------------")
        print(len(src_a))
        for i in range(len(src_a)):  # 遍历li个数
            ii = i+1
            src_list1 = response.xpath("//div[@class='leader_row'][%d]/ul/li"% ii)
            for m in range(len(src_list1)):
                mm = m+1
                item = XrldSpiderItem()
                item['zwmc'] = se.xpath("//div[@class='leader_row'][%d]/h4/text()" % ii).extract()
                item['name'] = se.xpath("//div[@class='leader_row'][%d]/ul/li[%d]/a/p/text()" % (ii,mm)).extract()
                yield item

        src_b = response.xpath("//div[@class='leader_row last-noborder']")
        print(len(src_b))
        for j in range(len(src_b)):  # 遍历li个数
            jj = j+1
            src_list2 = response.xpath("//div[@class='leader_row last-noborder'][%d]/ul/li"% jj)
            for n in range(len(src_list2)):
                nn = n+1
                item = XrldSpiderItem()
                item['zwmc'] = se.xpath("//div[@class='leader_row last-noborder'][%d]/h4/text()" % jj).extract()
                item['name'] = se.xpath("//div[@class='leader_row last-noborder'][%d]/ul/li[%d]/a/p/text()" % (jj,nn)).extract()
                yield item

