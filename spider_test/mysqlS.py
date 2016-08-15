# -*- coding:utf-8 -*-


import mysql.connector as MySQLdb
import time

class MysqlS:
    
    #获取当前时间
    def getCurrentTime(self):
        return time.strftime('[%Y-%m-%d %H:%M:%S]',time.localtime(time.time()))
    
    #数据库初始化
    def __init__(self):
        try:
            self.db = MySQLdb.connect(user='user',password='user',host='localhost',database='test')
            self.cur = self.db.cursor()
        except MySQLdb.Error,e:
             print self.getCurrentTime(),u"连接数据库错误，原因%d: %s".encode("GBK") % (e.args[0], e.args[1])

    #插入数据
    def insertData(self, table, my_dict):
         try:
             cols = ', '.join(my_dict.keys())
             values = '"," '.join(my_dict.values())
             sql = "INSERT INTO %s (%s) VALUES (%s)" % (table, cols, '"'+values+'"')
             try:
                 result = self.cur.execute(sql)
                 self.db.commit()
                 #判断是否执行成功
                 if result:
                     return "success"
                 else:
                     return 0
             except MySQLdb.Error,e:
                 #发生错误时回滚
                 self.db.rollback()
                 #主键唯一，无法插入
                 if "key 'PRIMARY'" in e.args[1]:
                     print self.getCurrentTime(),u"数据已存在，未插入数据".encode("GBK")
                 else:
                     print self.getCurrentTime(),u"插入数据失败，原因 %d: %s".encode("GBK") % (e.args[0], e.args[1])
         except MySQLdb.Error,e:
             print self.getCurrentTime(),u"数据库错误，原因%d: %s".encode("GBK") % (e.args[0], e.args[1])
		 		             

    
