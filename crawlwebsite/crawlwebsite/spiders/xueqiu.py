# -*- coding: utf-8 -*-
import scrapy
import csv

from crawlwebsite.items import CrawlwebsiteItem

# https://xueqiu.com/snowman/S/SZ300385/detail#/GSJJ
BASE_HEAD_URL = 'http://vip.stock.finance.sina.com.cn/corp/go.php/vCI_CorpInfo/stockid/'
BASE_END_URL = '.phtml'
class XueqiuSpider(scrapy.Spider):
    name = 'xueqiu'
    allowed_domains = ['xueqiu.com']
    start_urls = []
    with open('/root/crawlStockWebsite/crawlwebsite/stock_stock_base.csv', 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            code = row[0]
            stock_code = code[:6]
            website = BASE_HEAD_URL + stock_code + BASE_END_URL
            start_urls.append(website)
    
    def parse(self, response):
        item = CrawlwebsiteItem()
        try:
            self.get_name(response, item)
            self.get_website(response, item)
            self.get_nature(response, item)
            self.get_id(response, item)
        except:
            print(response)

        return item
    
    def get_name(self, response, item):
        name = response.css('#stockName::text').extract()
        if name:
            # print('name:{}'.format(name[0]))
            item['stock_name'] = name[0]
    
    def get_website(self, response, item):
        website = response.css('a[target="_blank"]::text').extract()
        # print('website:{}'.format(website[-8]))
        item['stock_website'] = website[-8]
    
    def get_id(self, response, item):
        stock_id = response.css('#stockName span::text').extract()[0].replace('(', '').replace(')', '')
        # print('stock_id:{}'.format(stock_id))
        item['stock_id'] = stock_id

    def get_nature(self, response, item):
        nature = response.xpath('//td[contains(text(), "组织形式：")]/following-sibling::td/text()').extract()
        if nature:
            # print('nature:{}'.format(nature[0]))
            item['company_nature'] = nature[0]
        else:
            item['company_nature'] = '未知'

