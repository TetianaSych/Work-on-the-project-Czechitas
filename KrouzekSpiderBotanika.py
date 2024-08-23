import scrapy

class KrouzekSpiderBotanika(scrapy.Spider):
    name = 'svc_botanika'
    start_urls = ['https://botanka.cz/typy-kurzu/pro-deti/']

    def parse(self, response):
        print(f"Scraping page: {response.url}")
        for link in response.css('a::attr(href)'):
            yield response.follow(link.get(), callback=self.parse_krouzek)
            

  
    def parse_krouzek(self, response):
        yield{
            'name':response.css('h1.entry-title::text').get(),
            'category':response.css('aside#custom-widget h2::text').get(),
            'name_organization':response.css('h2.widget-title::text').get(),
            'place':response.css('div.textwidget.custom-html-widget::text').get(),
            'price':response.css('h3.p2 + ul li.p2::text').get(),
            'time_day':response.css('li.p2 p::text').get(),
        }

































              # current_page_number = int(response.url.split('=')[-1]) if '=' in response.url else 1
        # next_page_number = current_page_number + 1
        # if next_page_number <= 18:
        #     next_page = f'https://www.luzanky.cz/aktivity?detail=1&page={next_page_number}&produkt=1&q=brno'
           
            
            # yield response.follow(next_page, callback=self.parse)

#pipenv shell
#scrapy crawl svc_botanika -O svc_botanika.csv
#.\venv\Scripts\Activate
# fetch('https://www.luzanky.cz/aktivity?detail=1&produkt=1&q=brno')
