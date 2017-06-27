# encoding:utf-8
import scrapy
from DataSpider.items import DataspiderItem
import urllib
import re
import sqlite3
import chardet


class BaiduSpider(scrapy.Spider):
    # name设置
    name = "BaiduSpider"
    # 爬出的url地址
    allowed_domanis = ["www.baidu.com"]
    # 要检索的人名的输入，从这里开始！
    words = ["周奇"]
    start_urls = []
    #conn = sqlite3.connect('baidu_data.db')
    #c = conn.cursor()
    #c.execute('''CREATE TABLE IF NOT EXISTS scrapydata(id integer primary key autoincrement, title text, url varchar(1000), content text, name text)''')

    def __init__(self):
        self.count = 0

    for word in words:
        # 该url没有出现重定向的的情况（302）
        url = "http://www.baidu.com/s?q=&tn=baiduhome_pg&ct=0&si=&ie=utf-8&cl=3&wd=%s" % urllib.quote(word)
        print url
        #url = 'http://ww.baidu.com/s?wd=%s&pn=0&ie=utf-8&cl=3&rn=10&rsv_bp=0&rsv_idx=1&ct=0&&rsv_spt=1&tn=baiduhome_pg' % urllib.quote(word)
        start_urls.append(url)


    def __get_url_query(self, url):
        #m = re.search("wd=(.*)", url).group(1)
        m = re.search("wd=([^&]*)",url).group(1)
        return m


    def parse(self, response):
        self.count += 1
        item = DataspiderItem()
        #items = []
        # 匹配中文,数字和英文的形式。。
        #xx = u"[\u4e00-\u9fa5a-zA-Z0-9]+"
        xx=u"[\u4e00-\u9fa5]+"
        pattern = re.compile(xx)
        # 按照div/id值来进行抽取
        a = []
        for i in range(1, 101):
            a.append(['%d' % i])
        for t in response.xpath('//div[@id="content_left"]/div'):
            # 获得查询的词，便于数据库的索引
            query = urllib.unquote(self.__get_url_query(response.url))
            #print query 
            if t.xpath('./@id').extract() in a:
                item['title'] = (
                    ''.join(t.xpath('./h3/a//text()').extract()).strip()).encode('utf-8')
                # print items['title'].encode('utf-8')
                item['url'] = t.xpath('./h3/a/@href').extract()[0].encode('utf-8')
                item['content'] = (' '.join(pattern.findall(
                    ''.join(t.xpath('./div[1]//text()').extract())))).encode('utf-8')
                #print item['content']
                #print chardet.detect(item['content'])['encoding']
                item['word'] = query
                #items.append(item)
                #self.c.execute("INSERT INTO scrapydate(title,url,content,name) VALUES(?,?,?,?)", (items[
                               #'title'], items['url'], items['content'], query))
                #self.conn.commit()
                yield item

        nextpage = u'下一页>'
        url = response.xpath(
            "//a[contains(text(),'%s')]/@href" % (nextpage)).extract()
        if url and self.count <= 10:
            page = "http://www.baidu.com" + url[0]
            #print page
            yield scrapy.Request(page, callback=self.parse)

    # 初始化计数器
    def closed_count(self):
        self.count = 0
        self.conn.close()
