import scrapy

date=raw_input("Δώσε την ημερομηνία dd/mm/yyyy:")
date=date.split("/")
day=int(date[0])
month=int(date[1])
year=int(date[2])

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['http://applications.opap.gr/DrawsRestServices/kino/drawDate/day-month-year.json']

    def parse(self, response):
        for url in response.css('ul li a::attr("href")').re('.*/category/.*'):
            yield scrapy.Request(response.urljoin(url), self.parse_titles)
			
for i in range(1,80):		
 s(i)=results.count (i)
 print "Αριθμός:",s(i)