# -*- coding: utf-8 -*-
import scrapy
import logging

class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        Countries = response.xpath("//td/a")
        
        for country in Countries:
            Name = country.xpath(".//text()").get()
            Link = country.xpath(".//@href").get()
            yield response.follow(url=Link , callback = self.parse_country , meta={'country_name' : Name})
            
    def parse_country(self,response):
        Name = response.request.meta['country_name']
        rows =  response.xpath('(//table[@class="table table-striped table-bordered table-hover table-condensed table-list"])[1]/tbody/tr')
        for row in rows:
            Year = row.xpath(".//td[1]/text()").get()
            population = row.xpath(".//td[2]/strong/text()").get()
            
            yield {
                'Country Name ': Name,
                'Year' : Year,
                'population' : population
                }
        
        