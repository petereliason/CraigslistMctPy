from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from craigslist_mcy.items import CraigslistMcyItem
import re, string
			
     
			
class MySpider2(BaseSpider):
  name = "craigmcy2"
  allowed_domains = ["craigslist.org"]
  start_urls = ["http://minneapolis.craigslist.org/search/mca?query=vulcan+900",
                "http://phoenix.craigslist.org/search/mca?query=vulcan+900",
                "http://phoenix.craigslist.org/search/mca?query=vulcan+900&s=100"]

  def parse(self, response):
      hxs = HtmlXPathSelector(response)
      
      titles = hxs.select("//p[@class='row']")
      items = []
      for title in titles:
          item = CraigslistMcyItem()
          item ["title"] = title.select("span[@class='txt']/span[@class='pl']/a/text()").extract()
          item ["link"] = title.select("span[@class='txt']/span[@class='pl']/a/@href").extract()
          item ["postedDt"] = title.select("span[@class='txt']/span[@class='pl']/time/@datetime").extract()
          item ["price"] =title.select("a[@class='i']/span[@class='price']/text()").extract()
          item ["debug"] = "" #blank for now...before, it was: title.select("a[@class='i']").extract()
          item ["location"] = re.split('[\s"]+',string.strip(str(hxs.select("//title/text()").extract())))
          items.append(item)
      return items			      