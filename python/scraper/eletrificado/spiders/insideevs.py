from scrapy import Spider, Request

MAIN_PAGE_URL = "https://insideevs.com/news/"

class InsideevsSpider(Spider):
    name = "insideevs"

    def start_requests(self):
        yield Request(MAIN_PAGE_URL, callback=self.parse_main_page)
        
    def parse_main_page(self, response):
        item_wcom = set(response.css('div.item.wcom a.thumb.zoom::attr(href)').getall())
        item_deep_wcom = set(response.css('div.item.deep.wcom a.thumb.zoom::attr(href)').getall())
        
        posts = list(item_wcom | item_deep_wcom)
        
        for post in posts:
            yield Request(url=post, callback=self.parse_post)

    def parse_post(self, response):
        pass