import scrapy


class DivanlightsSpider(scrapy.Spider):
    name = "divanlights"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://divan.ru/category/svet"]

    def parse(self, response):
        lights = response.css('div.lsooF')
        for light in lights:
            yield {
                'name': light.css('div.lsooF span::text').get(),
                'price': light.css('div.pY3d2 span::text').get(),
                'url': light.css('link[itemprop="url"]::attr(href)').get()
                  }


