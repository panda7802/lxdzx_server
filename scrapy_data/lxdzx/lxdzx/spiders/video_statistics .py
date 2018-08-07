# coding=utf-8

import scrapy
import sqlite3

# //*[@id="qy_list_cont"]/div[1]/dl/dd[2]/span[3]/i[1]
from scrapy import Spider

from scrapy_test.items import ScrapyTestItem

import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class video_tj_bfl(scrapy.Spider):
    name = "tj_bfl"
    start_urls = [
        "http://space.bilibili.com/22500342?from=search&seid=2714400427622356730#/video?tid=0&page=1&keyword=&order=click"]

    def parse(self, response):
        print response
        title_list = response.xpath('//*[@id="submit-video-list"]/ul[2]/li[1]/a[2]').extract()
        bfl_list = response.xpath(
            '//*[@id="submit-video-list"]/ul[2]/li[1]/div/span[1]').extract()
        # for i, j in zip(title_list, price_list):
        #     print i, ":", j
        item = ScrapyTestItem()
        for i, j in zip(title_list, bfl_list):
            print i, ":", j
            # item['title'] = i
            # item['money'] = j
            # # print item
            # yield item


if "__main__" == __name__:
    # scrapy crawl maifang
    db_mf = sqlite3.connect("st.db")
    sql_create_table = "create table if not EXISTS t_maifang (title  varchar(512) , money VARCHAR(128))"
    db_mf.execute(sql_create_table)
    db_mf.close()
