import scrapy

class KrouzekSpiderLuzanky(scrapy.Spider):
    name = 'svc_Helceletka'
    start_urls = ['https://helceletka.cz/krouzky/']

    def parse(self, response):
        print(f"Scraping page: {response.url}")
        for link in response.css('a::attr(href)'):
            # yield response.follow(link, callback=self.parse_krouzek)
            yield response.follow(link.get(), callback=self.parse_krouzek)
    
    def parse_krouzek(self, response):
        yield{
            # 'name':response.css('h1::text').get(),
            # 'category':response.css('h2::text').get(),
            # # 'location':response.css('span.icon-map + p::text').get(),
            # # 'place':response.xpath('//h2[@id="funplace"]/following-sibling::p[1]/text()').get(),
            # 'age_group':response.css('div.h3.mb-1::text')[2].getall(),
            # 'capacity':response.css('div.h3.mb-1::text')[3].getall(),
            # 'price':response.css('div.h3.mb-1::text')[4].getall(),
            # 'time':response.css('div.mt-2 ::text').get(),
            # 'day':response.css('div.mb-1.h3::text').get()
        }
