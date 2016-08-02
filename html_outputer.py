#coding=utf-8
'''
Created on 2016年1月12日

@author: hadoop
'''

import datetime
import os
import MySQLdb
import urllib
class HtmlOutputer(object):
    def __init__(self):
        self.datas = [] 
        self.title=''
    
    def collect_data(self,new_title,data):#收集数据
        print "正在收集数据..."
        if data is None:
            return
        for dat in data:
            self.datas.append(dat)
        self.title = new_title
        

    
    def output_html(self,count):#写出到文件（如html）中

        print '文件存在,正在追加...',
        fout = open('output.html','a') 
        #ascii
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % count)
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['title'].encode('utf-8'))
            fout.write("<td>%s</td>" % data['summary'].encode('utf-8'))
            fout.write("</tr>")
        #fout.write("</table>")
        #fout.write("</body>")
        #fout.write("</html>")
        #fout.close()
        print "追加完成！"
        self.datas = [] #输出后清空搜集器

    
    def output_html_time(self,time3):
        
        fout = open('output.html','a')#追加时间
        #ascii
   
        fout.write("</table>")
        
        #print time3
        #print str(time3)
        fout.write("耗时："+str(time3))
        
        fout.write("</body>")
        fout.write("</html>")
        fout.close()   
        self.datas = []

    
    def output_new_html(self,count):#创建文件
        print '文件不存在，准备创建文件...'
        fout = open('output.html','w')
        fout.write("<html>")
        fout.write("<head>")
        fout.write("<meta charset=\"UTF-8\">")
        fout.write("</head>")
        fout.write("<body>")
        fout.write("<table>")
        #ascii
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % count)
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['title'].encode('utf-8'))
            fout.write("<td>%s</td>" % data['summary'].encode('utf-8'))
            fout.write("</tr>")
        #fout.write("</table>")
        #fout.write("</body>")
        #fout.write("</html>")
        #fout.close()
        print "创建完成！"
        self.datas = []  #输出后清空搜集器
        
    def output_images(self):#下载图片到本地
        print '正在下载到本地...'
        x=1
        print '正在创建文件夹...',self.title
        os.mkdir(self.title)
        print 'self.datas',self.datas
        for imgurl in self.datas:
            
            print 'imgurl',imgurl
            urllib.urlretrieve(imgurl,self.title+'/pic_%s.png' %x)
            x+=1
        
    def output_mysql(self,count):#输出到数据库中
        print '正在写入数据库...'
        try:
            conn=MySQLdb.connect(host='localhost',user='root',passwd='123456',db='test',port=3306,charset="utf8")
            cur=conn.cursor()
            #cur.execute('create database if not exists baike')
            conn.select_db('baike')
            #cur.execute('create table baike(id int,url varchar(255),title varchar(255),text text(255))')
            count = cur.execute('select * from baike') 
            '''print 'there has %s rows record' % count
            result=cur.fetchone()
            print result
            #print 'ID: %s info %s %s %s %s %s %s %s %s %s' % result
            sqli="insert into baike values(%s,%s,%s,%s)"
            cur.execute(sqli,('3','Huhu','2 year 1 class','7'))'''
            
            print '准备写入数据库...'
            for data in self.datas:
                value=[count,data['url'],data['title'].encode('utf-8'),data['summary'].encode('utf-8')]
                #print 'insert into baike values(%s,%s,%s,%s)', value
                cur.execute('insert into baike values(%s,%s,%s,%s)', value)

            conn.commit()
            print '写入数据库成功！'
            cur.close()
            conn.close()
        except MySQLdb.Error,e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    
        
    
    
    
    



