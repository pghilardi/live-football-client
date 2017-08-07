# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo

from scrapy.conf import settings
from scrapy.exceptions import DropItem
from scrapy import log
import os

MONGODB_SERVER     = os.environ.get('MONGODB_SERVER') or settings['MONGODB_SERVER']
MONGODB_PORT       = int(os.environ.get('MONGODB_PORT') or settings['MONGODB_PORT'])
MONGODB_DB         = os.environ.get('MONGODB_DB') or settings['MONGODB_DB']
MONGODB_COLLECTION = os.environ.get('MONGODB_COLLECTION') or settings['MONGODB_COLLECTION']

class MongoDBPipeline(object):
    def __init__(self):
        connection = pymongo.MongoClient(
            MONGODB_SERVER,
            MONGODB_PORT
        )

        db = connection[MONGODB_DB]
        self.collection = db[MONGODB_COLLECTION]

    def process_item(self, item, spider):
        for data in item:
            if not data:
                raise DropItem("Missing data!")

        self.collection.update({'id': item['id']}, dict(item), upsert=True)
        log.msg("Game added to MongoDB database!", level=log.DEBUG, spider=spider)

        return item
