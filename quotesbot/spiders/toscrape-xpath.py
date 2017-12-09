# -*- coding: utf-8 -*-
import scrapy


class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'deviant'

    def __init__(self, tag, *args, **kwargs):
        super(ToScrapeSpiderXPath, self).__init__(*args, **kwargs)
        self.tag = tag
        self.start_urls = ['https://www.deviantart.com/tag/%s' % tag]

    # title, artist, created_at, tag, url, image

    def parse(self, response):
        for item in response.xpath('//span[@class="thumb"] | //span[@class="thumb wide"] | //span[@class="thumb narrow-thumb"]'):
            yield {
                'url': item.xpath('./a[@class="torpedo-thumb-link"]/@href').extract_first(),
                'image': item.xpath('./a[@class="torpedo-thumb-link"]/img/@src').extract_first(),
            }

        next_page_url = response.xpath('//li[@class="next"]/a/@href').extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))

