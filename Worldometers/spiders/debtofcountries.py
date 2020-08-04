# -*- coding: utf-8 -*-
import scrapy


class DebtofcountriesSpider(scrapy.Spider):
    name = 'debtofcountries'
    allowed_domains = ['www.worldpopulationreview.com/countries/countries-by-national-debt/']
    start_urls = ['https://worldpopulationreview.com/countries/countries-by-national-debt//']

    def parse(self, response):
        rows= response.xpath("//tbody/tr")
        for row in rows:
            Country_name = row.xpath(".//td[1]/a/text()").get()
            debt = row.xpath(".//td[2]/text()").get()
            population = row.xpath(".//td[3]/text()").get()
            
            yield{
                'Country Name': Country_name,
                'Debt of Country': debt,
                'Population of Country':population
                }
        
    
    
    
