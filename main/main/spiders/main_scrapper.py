import scrapy

class managerNames(scrapy.Spider):
    name = "managerNames"
    start_url = ['wwww.rlandesman.github.io']

    def parse(self, response):
        
