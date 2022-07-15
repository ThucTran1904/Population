from turtle import title
import scrapy


class ConNhenSpider(scrapy.Spider):
    name = 'con_nhen'
    allowed_domains = ['www.worldometers.info/']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        title = response.xpath("//h1/text()").get()
        countries = response.xpath("//table[@id='example2']/tbody/tr/td[2]/a/text()").getall()

        yield {
            'title': title,
            'countries': countries
        }
