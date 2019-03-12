# -*- coding: utf-8 -*-
import scrapy


class DesktopSpider(scrapy.Spider):
    name = 'desktop'
    allowed_domains = ['www.newegg.com/Desktop-Computers/SubCategory/ID-10']
    start_urls = ['http://www.newegg.com/Desktop-Computers/SubCategory/ID-10/']

    def parse(self, response):
    	title = response.css('.item-title::text').extract()
    	price = response.css('.price-was-data::text').extract()
    	save = response.css('.price-save-percent::text').extract()
    	image = response.css('.item-img::attr(href)').extract()
    	

    	for item in zip(title,price,save,image):
            #create a dictionary to store the scraped info
            scraped_data = {
                'title' : item[0],
                'price' : item[1],                
                'save' : item[2],
                'imageUrl': item[3]
            }
        yield scraped_data
