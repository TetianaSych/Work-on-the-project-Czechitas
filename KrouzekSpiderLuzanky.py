import scrapy

class KrouzekSpiderLuzanky(scrapy.Spider):
    name = 'svc_luzanky'
    start_urls = ['https://www.luzanky.cz/aktivity?detail=1&nextPages=17&produkt=1&q=brno']
  

    def parse(self, response):
        print(f"Scraping page: {response.url}")
        for link in response.css('a::attr(href)'):
            yield response.follow(link.get(), callback=self.parse_krouzek)
            

    def parse_krouzek(self, response):
        yield{
            'name':response.css('h1::text').get(),
            'category':response.css('h2::text').get(),
            'age_group':response.css('div.h3.mb-1::text')[2].getall(),
            'capacity':response.css('div.h3.mb-1::text')[3].getall(),
            'price':response.css('div.h3.mb-1::text')[4].getall(),
            'time':response.css('div.mt-2 ::text').get(),
            'day':response.css('div.mb-1.h3::text').get()
        }
 
#pipenv shell
#scrapy crawl svc_luzanky -O svc_luzanky.csv
#.\venv\Scripts\Activate 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
      # # current_page_number = int(response.url.split('=')[-1]) if '=' in response.url else 1
        # # next_page_number = current_page_number + 1
        # # if next_page_number <= 18:
        # #     next_page = f'https://www.luzanky.cz/aktivity?detail=1&page={next_page_number}&produkt=1&q=brno'
       
        #   #    https://www.luzanky.cz/aktivity?detail=1&nextPages=17&produkt=1&q=brno
        #     # next_page = f'https://www.krouzkyatabory.cz/krouzky/brno/vsechny-krouzky?p={next_page_number}'
        #     yield response.follow(next_page, callback=self.parse)


#pipenv shell
#scrapy crawl svc_luzanky -O svc_luzanky.csv
#.\venv\Scripts\Activate
# fetch('https://www.luzanky.cz/aktivity?detail=1&produkt=1&q=brno')

