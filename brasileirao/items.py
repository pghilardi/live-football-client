# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class BrasileiraoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    rodada = Field()
    home_team = Field()
    away_team = Field()
    home_score = Field()
    away_score = Field()
    date = Field()
    id = Field()
