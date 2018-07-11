#coding=utf-8
import scrapy
import re
import os
import urllib
import pymysql
import sys
from urlparse import urljoin
from scrapy.selector import Selector
from scrapy.http import HtmlResponse,Request

from webCrawler_scrapy.items import LsmrSpiderItem #导入item对应的类，crawlPictures是项目名，items是items.py文件，import的是items.py中的class，也可以import *

class Spdier_pictures(scrapy.spiders.Spider):
    name="lsmr"    #定义爬虫名，要和settings中的BOT_NAME属性对应的值一致
    allowed_domains = ["bnu.edu.cn"]
    start_urls=["http://www.bnu.edu.cn/xxgk/lsmr/index.htm"]   #开始爬取的地址
    
    #该函数名不能改变，因为Scrapy源码中默认callback函数的函数名就是parse
    def parse(self, response):
        se=Selector(response) #创建查询对象，HtmlXPathSelector已过时
        src = response.xpath("//ul[@class='leader_list01 leader_list02 leader_list03']/li")#匹配到ul下的所有小li
        for i in range(len(src)):#遍历li个数
            imgURLs=se.xpath("//ul[@class='leader_list01 leader_list02 leader_list03']/li[%d]/a/span/img/@src"%i).extract() #依次抽取所需要的信息
            titles=se.xpath("//ul[@class='leader_list01 leader_list02 leader_list03']/li[%d]/a/p/text()"%i).extract()
            print (imgURLs)
            print (titles)
            if imgURLs:
                relativeUrl=imgURLs[0]
                realUrl = urljoin("http://www.bnu.edu.cn/images/content/2018-03/20180305110227082271.jpg", relativeUrl)
                file_name=u"%s.jpg"%titles[0] #要保存文件的命名
                    
                path=os.path.join("D:\pics",file_name)#拼接这个图片的路径，我是放在F盘的pics文件夹下
                    
                type = sys.getfilesystemencoding()
                print (file_name.encode(type) )
                    
                item=LsmrSpiderItem()  #实例item（具体定义的item类）,将要保存的值放到事先声明的item属性中
                item['name']=titles[0]
                item['url']=realUrl
                print (item["name"],item["url"] )
                    
                yield item  #返回item,这时会自定解析item

                urllib.urlretrieve(realUrl,path)  #接收文件路径和需要保存的路径，会自动去文件路径下载并保存到我们指定的本地路径
            

