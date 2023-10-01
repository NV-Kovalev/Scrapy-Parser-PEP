import scrapy

from pep_parse.settings import PEPSPIDER_CONFIGS
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = PEPSPIDER_CONFIGS['name']
    allowed_domains = PEPSPIDER_CONFIGS['allowed_domains']
    start_urls = PEPSPIDER_CONFIGS['start_urls']

    def parse(self, response):
        numerical_index_table = response.css('section[id="numerical-index"]')
        pep_links = (numerical_index_table.css('td a::attr(href)').getall())
        for link in pep_links:
            yield response.follow(f'{link}/', callback=self.parse_pep)

    def parse_pep(self, response):
        data = {
            'name': response.css('h1.page-title::text').get(),
            'status': response.css('abbr::text').get(),
            'number': response.css(
                'header').css('li::text').getall()[2].split()[1]
        }
        yield PepParseItem(data)
