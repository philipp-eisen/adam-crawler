import scrapy
import string
import re
from bs4 import BeautifulSoup


class AdamSpider(scrapy.Spider):
    name = 'adam'
    start_urls = []
    for char in string.uppercase[:24]:
        start_urls.append('https://www.nlm.nih.gov/medlineplus/ency/encyclopedia_{}.htm'.format(char))

    def parse(self, response):
        for href in response.css('#index li a::attr(href)'):
            pattern = re.compile('^patientinstructions*')
            if pattern.match(href.extract()) is not None:
                continue
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url, callback=self.parse_article)

    def parse_article(self, response):
        article = {}
        article['Title'] = response.css('h1::text').extract()[0]
        article['URL'] = response.url
        for section in response.css('.section'):
            html = ' '.join(section.css('.section-body').extract())
            # Adding white space around tags. Helps for example if no spaces are added between <li> oder after <br>
            # is likely though to add to many white spaces. In this application doesn't hurt thou
            html = html.replace('>', '> ')
            html = html.replace('<', ' <')
            soup = BeautifulSoup(html)
            article[
                ''.join(section.css('.section-header .section-title h2::text').extract())] = soup.get_text().replace(
                '\n', ' ')
        yield article
