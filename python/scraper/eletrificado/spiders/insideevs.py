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
            yield Request(url=f'https://insideevs.com{post}', callback=self.parse_post)

    def parse_post(self, response):
        title = response.css('h1.m1-article-title::text').get()
        author = response.css('span.name a::text').get()
        
        image = response.css('div.originalImage img::attr(src)').get()
        if image is None:
            image = response.css('div.video-player img::attr(src)').get()
        
        paragraphs = response.css('div.postContent p::text').getall()[:-1] # Last paragraph is not part of the article
        text = "\n\n".join(paragraphs)
        
        yield {
            'title': title,
            'author': author,
            'text': text,
            'url': response.url,
            'image': image
        }