#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2016-08-05 10:24:56
# Project: test2_meishi

from pyspider.libs.base_handler import *
#from pyspider.user.Mysql import *

PAGE_START = 1
PAGE_END = 1
HOME_URL = "http://www.ttmeishi.com"


class Handler(BaseHandler):
    crawl_config = {
    }

    def __init__(self):
        self.base_url = HOME_URL + '/CaiXi/JiaChangCai/'
        self.page_num = PAGE_START
        self.total_num = PAGE_END
        self.mysql = Mysql()
        
        
    @every(minutes=24 * 60)
    def on_start(self):
        while self.page_num <= self.total_num:
            if self.page_num == 1:
                url = self.base_url
            else:
                url = self.base_url + "list" + str(self.page_num) + ".htm"
            self.crawl(url, callback=self.index_page)
            self.page_num += 1

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('.cx_liebiao li > a').items():
            self.crawl(each.attr.href, callback=self.detail_page)

    @config(priority=2)
    def detail_page(self, response):
        #查询数据库是否有值,防止重复插入
        if(self.mysql.queryForKey(response.url) < 1):
            #插入数据库 t_meishi 主表
            #主表id
            main_id = self.mysql.queryMaxPK("t_meishi", "id")
            main_dict = {
                "id" : str(main_id),
                "title" : response.doc('.content h1').text(),
                "summary" : response.doc('.c_jianjie').text(),
                "cailiao" : response.doc('.c_leibie .c_leibie_sc').text(),
                "sourceUrl" : response.url,
                "homeJpjUrl": response.doc('.c_img_show1 img').attr.src,
            } 
            self.mysql.insertData("t_meishi", main_dict)

            
            #插入子表 t_meishi_child
            imgs = response.doc('.c_bz_img img').items()
            contexts = response.doc('.c_bz_neirong').items()
            step = 1
            try: 
                while contexts:
                    child_id = self.mysql.queryMaxPK("t_meishi_child", "id")
                    child_dict = {
                        "id" : str(child_id),
                        "main_id" : str(main_id),
                        "step" : str(step),
                        "step_desc" : contexts.next().text(),
                        "jpgUrl" : imgs.next().attr.src,
                    }
                    self.mysql.insertData("t_meishi_child", child_dict)
                    step += 1
            except StopIteration as e:
               if step == 1:
                   child_id = self.mysql.queryMaxPK("t_meishi_child", "id")
                   child_dict = {
                       "id" : str(child_id),
                       "main_id" : str(main_id),
                       "step" : str(step),
                       "step_desc" : response.doc('.c_buzhou').text(),
                   }
                   self.mysql.insertData("t_meishi_child", child_dict)
                   step += 1
        


import MySQLdb
import time
 
class Mysql:
    
    #获取当前时间
    def getCurrentTime(self):
        return time.strftime('[%Y-%m-%d %H:%M:%S]',time.localtime(time.time()))
    
    #数据库初始化
    def __init__(self):
        try:
            self.db = MySQLdb.connect('localhost','user','user','test')
            self.cur = self.db.cursor()
        except MySQLdb.Error,e:
             print self.getCurrentTime(),"连接数据库错误，原因%d: %s" % (e.args[0], e.args[1])
 
    #插入数据
    def insertData(self, table, my_dict):
         try:
             self.db.set_character_set('utf8')
             cols = ', '.join(my_dict.keys())
             values = '"," '.join(my_dict.values())
             sql = "INSERT INTO %s (%s) VALUES (%s)" % (table, cols, '"'+values+'"')
             try:
                 result = self.cur.execute(sql)
                 insert_id = self.db.insert_id()
                 self.db.commit()
                 #判断是否执行成功
                 if result:
                     return insert_id
                 else:
                     return 0
             except MySQLdb.Error,e:
                 #发生错误时回滚
                 self.db.rollback()
                 #主键唯一，无法插入
                 if "key 'PRIMARY'" in e.args[1]:
                     print self.getCurrentTime(),"数据已存在，未插入数据"
                 else:
                     print self.getCurrentTime(),"插入数据失败，原因 %d: %s" % (e.args[0], e.args[1])
         except MySQLdb.Error,e:
             print self.getCurrentTime(),"数据库错误，原因%d: %s" % (e.args[0], e.args[1]) 

    #查询最大主键ID
    def queryMaxPK(self, table, pkey):
        try:
            sql = "select Max(%s) from %s" % (pkey, table)
            self.cur.execute(sql)
            result = self.cur.fetchall()[0][0]
            if result:
                    return result + 1
            else:
                    return 0 + 1
        except MySQLdb.Error,e:
            print self.getCurrentTime(),"数据库错误，原因%d: %s" % (e.args[0], e.args[1])                
            
    #查询是否有数据
    def queryForKey(self, sourceUrlValue):
        try:
            sql = "select id from t_meishi where sourceUrl = %s" % ('"'+sourceUrlValue+'"')
            self.cur.execute(sql)
            result = self.cur.fetchall()
            if result:
                return 1
            else:
                return 0
        except MySQLdb.Error,e:
            print self.getCurrentTime(),"数据库错误，原因%d: %s" % (e.args[0], e.args[1])             
