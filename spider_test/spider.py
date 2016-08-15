# -*- coding:utf-8 -*-

import urllib
import urllib2
import re
import time
import types
import sys
import mysqlS

class Spider:
	    #初始化
    def __init__(self):
        self.page_num = 1
        self.total_num = None
        #self.page_spider = page.Page()
        self.mysql = mysqlS.MysqlS()
        
    #获取当前时间
    def getCurrentTime(self):
        return time.strftime('[%Y-%m-%d %H:%M:%S]',time.localtime(time.time()))
    
    #获取当前时间
    def getCurrentDate(self):
        return time.strftime('%Y-%m-%d',time.localtime(time.time()))

    def getPageURLByNum(self, page_num):
    	if page_num == 1:
    		page_url = "http://www.ttmeishi.com/CaiXi/JiaChangCai/"
        else:
        	page_url = "http://www.ttmeishi.com/CaiXi/JiaChangCai/list" + str(page_num) + ".htm"
        return page_url

    #通过传入网页页码来获取网页的HTML
    def getPageByNum(self, page_num):
        return self.getPage(self.getPageURLByNum(page_num))        

    def getPage(self, url):
        request = urllib2.Request(url)
        try:
            response = urllib2.urlopen(request)
        except urllib2.URLError, e:
            if hasattr(e, "code"):
                print self.getCurrentTime(),u"获取页面失败,错误代号".encode("GBK"), e.code
                return None
            if hasattr(e, "reason"):
                print self.getCurrentTime(),u"获取页面失败,原因".encode("GBK"), e.reason
                return None
        else:
            page =  response.read()
            return page  

    #获取所有的页码数
    def getTotalPageNum(self):
        print self.getCurrentTime(),u"正在获取目录页面个数,请稍候".encode("GBK")
        page = self.getPageByNum(1)
        #匹配页码数,\u5c3e\u9875是尾页的Unicode编码
        pattern = re.compile(r'<a href="list\d*\.htm">\D{,5}</a>')
        m =  pattern.search(page,0)
        pattern2 = re.compile(r'\d+')
        numstr = m.group()
        match = pattern2.search(numstr,0)
        if match:
            return int(match.group())
        else:
            print self.getCurrentTime(),u"获取总页码失败".encode("GBK")

    #主函数
    def main(self):  
    	start_page = 1
        print self.getCurrentTime(),u"开始页码".encode("GBK"),start_page
        print self.getCurrentTime(),u"爬虫正在启动,开始爬取美食网".encode("GBK")
        self.total_num = self.getTotalPageNum()
        print self.getCurrentTime(),u"获取到目录页面个数".encode("GBK"),self.total_num,u"个".encode("GBK")
        for x in range(1, self.total_num + 1):            
            page = self.getPageByNum(x)
            items = re.findall( r'/CaiPu/.*\.htm', page)
            for index in range(len(items)):
                if index != 0:
                    try:
                        subPage = self.getPage("http://www.ttmeishi.com" + items[index]);
                        m = re.search(r'<div class="c_buzhou cbox">(.*?)</div>',subPage,re.S)
                        resule =  m.group(1)
                        #删除 <br />
                        replaceBR = re.compile('<br />')
                        #删除 h2
                        replaceh2 = re.compile('<h2>|</h2>')
                        #删除 nbsp;
                        replaceNbsp = re.compile('&nbsp;')
                        #替换img
                        replaceImg = re.compile(r'<img  alt=".*" src="|<img  alt=".*" hspace=2 src="')
                        replaceImg2 = re.compile(r'">|" vspace=2>')
                        resule = re.sub(replaceBR, "\n", resule)
                        resule = re.sub(replaceh2, "", resule)
                        resule = re.sub(replaceNbsp, "", resule)
                        resule = re.sub(replaceImg, "http://www.ttmeishi.com", resule)
                        resule = re.sub(replaceImg2, "", resule)

                        resule = unicode(resule,"gbk")

                        #插入数据库
                        my_dict = {
                            "no" : str(x) + "- 序号" + str(index),
                            "context" : resule.encode("utf-8"),
                        }
                        self.mysql.insertData("meishi", my_dict)
                    except BaseException as e:
                        print u"报错了没事, 继续跑!".encode("GBK")
                        print e


spider = Spider()
spider.main()
       