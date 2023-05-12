import scrapy


class CarRepairsSpider(scrapy.Spider):
    name = "car_repairs"
    allowed_domains = ["www.cars.com"]
    start_urls = ["https://www.cars.com/auto-repair/"]

    def start_requests(self):
      URL = "https://www.cars.com/research/mazda-cx_5/recalls/"
      yield scrapy.Request(url = URL, callback = self.response_parser)

    def response_parser(self, response):
      for selector in response.css("section.sds-page-section"):
        yield{ 
          "title": selector.css("h3::text").get(),
          #"summary":selector.css("div.result-card__recall-summary::text").extract_first(), 
          #"consequence": selector.css(".result-card__recall-consequence::text").extract_first(), 
          #"correction":selector.css(".result-card__recall-action::text").extract_first()
           }
              
