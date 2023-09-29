import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        numerical_index_table = response.css('section[id="numerical-index"]')
        pep_links = (numerical_index_table.css('td a::attr(href)').getall())
        for link in pep_links:
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        data = {
            'name': response.css('h1.page-title::text').get(),
            'status': response.css('abbr::text').get(),
            'number': response.css(
                'header').css('li::text').getall()[2].split()[1]
        }
        yield PepParseItem(data)
