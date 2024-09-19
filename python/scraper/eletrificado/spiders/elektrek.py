from scrapy import Spider, Request

MAIN_PAGE_URL = 'https://electrek.co/'


class ElectrekSpider(Spider):
    name = "electrek"
    posts_urls = []
    
    def start_requests(self):
        yield Request(url=MAIN_PAGE_URL, callback=self.parse_posts_urls)
        
    def parse_posts_urls(self, response):
        posts_urls = response.css('article.article.standard a.article__title-link::attr(href)').getall()
                
        # Para cada URL, faz um novo request para capturar o conteúdo
        for url in posts_urls:
            yield Request(url=url, callback=self.parse_post, meta={'url': url})
        
    def parse_post(self, response):
        url = response.meta['url']
        title = response.css('h1.h1::text').get()
        author = response.css('span.author-name a::text').get()
        image = response.css('div.container.med.post-content img::attr(src)').get()
        paragraphs = response.css('div.container.med.post-content p::text').getall()
        text = "\n\n".join(paragraphs)
        
        for img in response.css('img.skip-lazy.wp-post-image::attr(src)').getall():
            img_url = response.urljoin(img)
        
        yield {
            'title': title,
            'author': author,
            'text': text,
            'url': url,
            'image': img_url
        }
