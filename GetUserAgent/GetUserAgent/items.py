# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class UserAgentItem(scrapy.Item):
    """
    user agent的item
    """
    ua_type = scrapy.Field()
    ua = scrapy.Field()
