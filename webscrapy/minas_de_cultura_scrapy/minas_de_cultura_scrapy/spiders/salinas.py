import re
import datetime

import scrapy

class SalinasSpider(scrapy.Spider):
    name = 'salinas'
    start_urls = ['https://www.salinas.mg.gov.br/portal/diario-oficial']


    def parse(self, response):
        editions = response.xpath('//div[contains(@class, "dof_download")]/@data-href')
        for edition in editions:
            # str('https://www.salinas.mg.gov.br'+ edition.extract())
            yield {
                    'diario':  str('https://www.salinas.mg.gov.br'+ edition.extract())
            }

        next_page = response.xpath('//div[contains(@class, "sw_area_paginacao")]//div//a[3]/@href').get()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)
