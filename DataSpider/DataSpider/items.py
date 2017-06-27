#encoding:utf-8

import scrapy
class DataspiderItem(scrapy.Item):
    #输入人名返回的title
    title = scrapy.Field()
    #返回的content
    content = scrapy.Field()
    #title中的url
    url = scrapy.Field()
    #查询的词
    word = scrapy.Field()
    
class RelatedItem(scrapy.Item):
    #返回页面右边的相关描述
    relate_describe =scrapy.Field()
    #相关描述对应的人名
    relate_name =scrapy.Field()
    #相关描述对应人名的url
    relate_url =scrapy.Field()
