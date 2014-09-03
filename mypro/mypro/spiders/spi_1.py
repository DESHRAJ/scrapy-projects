import scrapy 
	
class Mypro(scrapy.Spider):
	name = "mypro"
	allowed_domains = ["gdgjss.herokuapp.com"]
	start_urls = [
		"http://gdgjss.herokuapp.com/check",
		"http://gdgjss.herokuapp.com/register"
		]

def parse(self, response):
	filename = response.url.split("/")[-2]
	with open(file.txt, 'wb') as f:
		f.write(response.body)
