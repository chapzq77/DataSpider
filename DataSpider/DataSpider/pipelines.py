#encoding:utf-8

#from os import path
#from scrapy import signals
import json
from scrapy.exceptions import DropItem
#from scrapy.xlib.pydispatch import dispatcher
class DataspiderPipeline(object):
    def __init__(self):
        self.file = open("baidu.json",'w+')

    def process_item(self,item,spider):
        line = json.dumps(dict(item),ensure_ascii=False)+"\n"
        self.file.write(line)
        return item


