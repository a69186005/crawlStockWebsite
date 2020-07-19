# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlwebsiteItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    stock_name = scrapy.Field()
    stock_id = scrapy.Field()
    stock_website = scrapy.Field()
    company_nature = scrapy.Field()
