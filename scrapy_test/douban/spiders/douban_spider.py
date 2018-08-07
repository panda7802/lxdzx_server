# -*- coding: utf-8 -*-
import scrapy

from douban.items import DoubanItem


class DoubanSpiderSpider(scrapy.Spider):
    name = 'douban_spider'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        print "+++++++++++++++ start parse +++++++++++++++\n"
        # print response.text#.encode('gbk', 'ignore')
        movie_list = response.xpath(".//*[@id='wrapper']/div[@id='content']/div"
                                    "/div[@class='article']/ol[@class='grid_view']/li")

        for item in movie_list:
            db_item = DoubanItem()
            db_item['serial_num'] = item.xpath("./div/div[1]/em/text()").extract_first()
            db_item['movie_name'] = item.xpath("./div/div[2]/div[1]/a/span[1]/text()").extract_first()
            cont = item.xpath("./div/div[2]/div[2]/p[1]/text()").extract()
            s_introduce = []
            for i_cont in cont:
                s_introduce.append("".join(i_cont.split()))
            db_item['introduce'] = "\n".join(s_introduce)
            db_item['start'] = item.xpath("./div/div[2]/div[2]/div/span[2]/text()").extract_first()
            db_item['evaluate'] = item.xpath("./div/div[2]/div[2]/div/span[4]/text()").extract_first()
            db_item['desc'] = item.xpath("./div/div[2]/div[2]/p[2]/span/text()").extract_first()
            # print db_item.encode('gbk', 'ignore')
            # print str(db_item).decode('unicode-escape', 'ignore'), "\n"
            yield db_item
        # next_link = response.xpath("//span[@class='next']/link/@href").extract()
        # if next_link:
        #     next_link = next_link[0]
        #     yield scrapy.Request("https://movie.douban.com/top250" + next_link, callback=self.parse)

        print "+++++++++++++++ parse over +++++++++++++++\n"
