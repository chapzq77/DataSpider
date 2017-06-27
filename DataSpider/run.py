#encoding:utf-8
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from DataSpider.spiders.BaiduSpider import BaiduSpider
#from DataSpider.spiders.BingSpider import BingSpider
#from DataSpider.spiders.SogouSpider import SogouSpider

# 获取settings.py模块的设置
settings = get_project_settings()
process = CrawlerProcess(settings=settings)

# 可以添加多个spider
#process.crawl(BingSpider)
#process.crawl(SogouSpider)
process.crawl(BaiduSpider)

# 启动爬虫，会阻塞，直到爬取完成
process.start()
