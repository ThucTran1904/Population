from turtle import title
import scrapy


class ConNhenSpider(scrapy.Spider):
    name = 'con_nhen'
    allowed_domains = ['www.worldometers.info/']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        title = response.xpath("//h1/text()").get()
        countries = response.xpath("//table[@id='example2']/tbody/tr/td[2]/a/text()").getall()
        population = response.xpath("//table[@id='example2']/tbody/tr/td[3]/text()").getall()
        yearly_change = response.xpath("//table[@id='example2']/tbody/tr/td[4]/text()").getall()
        net_change = response.xpath("//table[@id='example2']/tbody/tr/td[5]/text()").getall()
        density = response.xpath("//table[@id='example2']/tbody/tr/td[6]/text()").getall()
        land_area = response.xpath("//table[@id='example2']/tbody/tr/td[7]/text()").getall()
        migrants = response.xpath("//table[@id='example2']/tbody/tr/td[8]/text()").getall()
        fert_rate = response.xpath("//table[@id='example2']/tbody/tr/td[9]/text()").getall()
        med_age = response.xpath("//table[@id='example2']/tbody/tr/td[10]/text()").getall()
        urban_pop = response.xpath("//table[@id='example2']/tbody/tr/td[11]/text()").getall()
        world_share = response.xpath("//table[@id='example2']/tbody/tr/td[12]/text()").getall()

        # no_odd = response.xpath("//table[@id='example2']/tbody/tr[@class='odd']/td[@class='sorting_1']/text()").getall()


        yield {
            'title': title,
            'countries': countries,
            'population': population,
            'yearly_change': yearly_change,
            'net_change': net_change,
            'density' : density,
            'land_area': land_area,
            'migrants' : migrants,
            'fert_rate' : fert_rate,
            'med_age' : med_age,
            'urban_pop' : urban_pop,
            'world_share' : world_share
            # 'no_odd' : no_odd,
        }
