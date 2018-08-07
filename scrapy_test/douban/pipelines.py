# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import traceback

import time

from douban.tutils.tglobal_data import lxdzx_bili_show_list


class DoubanPipeline(object):
    def __init__(self):
        print "init spider-----------------"

    def close_spider(self, sqider):
        print "------close db------"

    def process_item(self, item, spider):
        return item


class LxdzxBiliPipeline(object):
    def __init__(self):
        print "------__init__ LxdzxBiliPipeline------"
        path = "../static/files/lxdzx_bili.csv"
        self.filename = open(path, "wb")
        for show_item in lxdzx_bili_show_list:
            try:
                key = show_item[1]
                self.filename.write(key + ",")
            except Exception, e:
                traceback.print_exc()
        self.filename.write("\n")

    def process_item(self, item, spider):
        value = ""
        for show_item in lxdzx_bili_show_list:
            try:
                key = show_item[0]
                value = item[key].replace("\n", " ").replace("\r", " ").replace(",", " ").strip()
                if key == 'created':  # 时间转换
                    self.filename.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(long(value))) + ",")
                else:
                    self.filename.write(value + ",")
            except Exception, e:
                traceback.print_exc()
        self.filename.write("\n")
        return item

    def close_spider(self, sqider):
        print "------close_spider LxdzxBiliPipeline------"
        self.filename.close()
