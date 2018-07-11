# coding=utf-8
import scrapy
import re
import os
import urllib
import pymysql
import sys
from scrapy.selector import Selector
from scrapy.http import HtmlResponse, Request
from webCrawler_scrapy.items import  LrldSpiderItem

class LrldSpider(scrapy.spiders.Spider):
    name = 'lrld'
    allowed_domains = ["bnu.edu.cn"]
    start_urls = ["http://www.bnu.edu.cn/xxgk/lrld/index.htm" ]
    print ("------------------------------")
    print (len("按顺序"))
    print (len("按  序"))

    def parse(self, response):
        se = Selector(response)  # 创建查询对象，HtmlXPathSelector已过时
        src = response.xpath("//div[@class='Successive_leader']/h3")
        for i in range(len(src)):  # 遍历li个数
            if(i == 0):
                src_zw = response.xpath("//div[@class='sucLeader-con']")
                for j in range(len(src_zw)):
                    jj = j + 1
                    src_zwd = response.xpath("//div[@class='sucLeader-con'][%d]/ul/li"% jj)
                    for k in range(len(src_zwd)):
                        kk = k + 1
                        string ="".join(se.xpath("//div[@class='sucLeader-con'][%d]/ul[@class='sec-con sec-con02']/li[%d]/a/text()" %(jj,kk)).extract())
                        print string
                        print (len(string))

                        if len(string) < 18:
                            name = string[0:4]
                            rzsj = string[-9:-1]
                        elif len(string) > 22:
                            name = string[0:8]
                            rzsj = string[-15:-1]
                        else:
                            name = string[0:4]
                            rzsj = string[-15:-1]
                        #name,rzsj=string.split('	',1)
                        item = LrldSpiderItem()
                        item['zwmc'] = se.xpath("//div[@class='sucLeader-con'][%d]/p/strong/text()" % jj).extract()
                        item['rzsj'] = rzsj
                        item['name'] = name
                        item['lb'] = se.xpath("//div[@class='Successive_leader']/h3[1]/text()").extract()
                        item['rzdmc'] = ("北京师范大学党组织")
                        yield item

            if(i ==1):
                print "------------00-------"
                src_a = response.xpath("//table[@class='statistics SuccessiveLeaders']/tr")
                for t in range(len(src_a)):
                    if t != 0:
                        tt = t + 1
                        item = LrldSpiderItem()
                        src_b = response.xpath("//table[@class='statistics SuccessiveLeaders']/tr[%d]/td"% tt)
                        if len(src_b) == 3:
                            string1 = se.xpath("//table[@class='statistics SuccessiveLeaders']/tr[%d]/td[1]/text()" % tt).extract()
                            string2 = se.xpath( "//table[@class='statistics SuccessiveLeaders']/tr[%d]/td[2]/text()" % tt).extract()
                            item['rzsj'] = se.xpath("//table[@class='statistics SuccessiveLeaders']/tr[%d]/td[3]/text()" % tt).extract()
                            item['lb'] = se.xpath("//div[@class='Successive_leader']/h3[2]/text()").extract()
                            if len(string1) > 10:
                                item['rzdmc'] = string1
                                item['name'] = string2
                                item['zwmc'] = string2
                            else:
                                item['rzdmc'] = string
                                item['name'] = string1
                                item['zwmc'] = string2
                            yield item
                        else:
                            item = LrldSpiderItem()
                            item['rzdmc'] = se.xpath("//table[@class='statistics SuccessiveLeaders']/tr[%d]/td[1]/text()" % tt).extract()
                            string = item['rzdmc']
                            item['name'] = se.xpath("//table[@class='statistics SuccessiveLeaders']/tr[%d]/td[2]/text()" % tt).extract()
                            item['zwmc'] = se.xpath( "//table[@class='statistics SuccessiveLeaders']/tr[%d]/td[3]/text()" % tt).extract()
                            item['rzsj'] = se.xpath("//table[@class='statistics SuccessiveLeaders']/tr[%d]/td[4]/text()" % tt).extract()
                            item['lb'] = se.xpath("//div[@class='Successive_leader']/h3[2]/text()" ).extract()
                            yield item  # 返回item,这时会自定解析item

