#coding=utf-8
'''
Created on 2016年1月12日

@author: hadoop
'''
from ishuihui import Getlinks


'''import datetime
import time
import os
#from baikespider import url_manager, html_downloader, html_outputer, html_parser
import url_manager, html_downloader, html_outputer, html_parser
class SpiderMain(object):
    def __init__(self):#构造函数 初始化
        self.urls=url_manager.UrlManager()#管理器
        self.downloader = html_downloader.HtmlDownloader()#下载器
        self.parser = html_parser.HtmlPaser()#解析器
        self.outputer = html_outputer.HtmlOutputer()#输出器
    def craw(self,root_url):#爬虫调度程序
        
        time1 = datetime.datetime.now()  #计时 
        isexist =  os.path.exists(r'output.html')#是否存在输出文件
        print "开始时间:",time1.strftime("%Y-%m-%d %H:%M:%S")
        
        
        
        count =0
        self.urls.add_new_url(root_url)#将入口url添加进url管理器中
        while self.urls.has_new_url():#启动 爬取循环  如有待爬取的url
            try:
                if count >= 10000: #爬取1000个
                    break
                new_url=self.urls.get_new_url()#获取一个待爬取的url（并出栈）
                print "获取成功！"
                print 'craw %d:%s' % (count+1,new_url)
                html_cont=self.downloader.download(new_url)#启动下载器
                print "下载完成！"
                new_urls, new_data=self.parser.parse(new_url,html_cont)#调用解析器解析数据（当前url，下载好的数据）
                print "解析完成！"
                self.urls.add_new_urls(new_urls)#添加新的url，补充
                print "添加完成！"
                self.outputer.collect_data(new_data)#收集数据，补充新的数据 
                print "收集完成！"
               #self.outputer.output_mysql(count+1)#写到数据库
                if(isexist==False):#文件不存在，创建
                    self.outputer.output_new_html(count+1)
                    
                    isexist = True
                else:#文件存在，追加
                    self.outputer.output_html(count+1)
                    
                count = count + 1
            except:
                print 'craw failed'
        time2= datetime.datetime.now()
        print "结束时间:",time2.strftime("%Y-%m-%d %H:%M:%S") 
        time3 = time2-time1
        print "耗时:",time3
        self.outputer.output_html_time(time3)#写时间

if __name__=="__main__":
    root_url="http://baike.baidu.com/view/21087.htm"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
   
'''
#   多线程
import datetime
import threading
import thread
import time
import os
from ishuihui.global_variables import URLS, COUNT,ROOT_URL
import url_manager, html_downloader, html_outputer, html_parser
count = 0
mylock = thread.allocate_lock()
class SpiderMain(threading.Thread):
    def __init__(self,num, interval):#构造函数 初始化
        threading.Thread.__init__(self)
        self.thread_num = num  
        self.interval = interval  
        self.thread_stop = False
        #self.urls=url_manager.UrlManager()#管理器
        self.downloader = html_downloader.HtmlDownloader()#下载器
        self.parser = html_parser.HtmlPaser()#解析器
        self.outputer = html_outputer.HtmlOutputer()#输出器
        #self.allurls = Getlinks.GetLinks()
    def run(self):#爬虫调度程序
        global count  
        time1 = datetime.datetime.now()  #计时 
        isexist =  os.path.exists(r'output.html')#是否存在输出文件
      
        
        while URLS.has_new_url():#self.urls.has_new_url():#启动 爬取循环  如有待爬取的url
            print '\nThread(%s) 等待爬取, Number: %s'%(self.thread_num, time.ctime())
            try:
                print 'Thread Object(%d), Time:%s\n' %(self.thread_num, time.ctime())
                #time.sleep(self.interval) 
                #if count >= 50: #爬取1000个
                    #break;
                mylock.acquire()
                new_url=URLS.get_new_url()#获取一个待爬取的url（并出栈）
                mylock.release()
                print "获取成功！",new_url
                print 'craw %d:%s' % (count+1,new_url)
                html_cont=self.downloader.download(new_url)#启动下载器
                print "下载完成！"
                new_title,new_data=self.parser.parse(new_url,html_cont)#调用解析器解析数据（当前url，下载好的数据）
                print "解析完成！"
                self.outputer.collect_data(new_title,new_data)#收集数据，补充新的数据 
                print "收集完成！"
                #self.outputer.output_mysql(count+1)#写到数据库
                self.outputer.output_images()#下载到本地 
                if(isexist==False):#文件不存在，创建
                    self.outputer.output_new_html(count+1)
                    isexist = True
                else:#文件存在，追加
                    self.outputer.output_html(count+1)
                count+=1
                print count
                
                #thread.exit_thread()
                print 'exit'
            except:
                print 'craw failed',self.thread_num
            print '\nThread(%s) released, Number: %d'%(self.thread_num, count)
            if mylock.locked():
                mylock.release() 
        time2= datetime.datetime.now()
        time3 = time2-time1
        print self.thread_num,"耗时:",time3 
        self.outputer.output_html_time(time3)#写时间
    def stop(self):  
        self.thread_stop = True 
    def craw(self,isexist):#爬虫调度程序
        pass
def test():  
    thread1 = SpiderMain(1, 1)  
    thread2 = SpiderMain(2, 2)
    thread3 = SpiderMain(3, 3)
    #thread4 = SpiderMain(4, 4)  
    #thread5 = SpiderMain(5, 5)    
    thread1.start()
    time.sleep(10)
    thread2.start()
    #time.sleep(2)  
    thread3.start() 
    #thread4.start()
    #thread5.start()
    #time.sleep(10)  
    thread1.stop()  
    thread2.stop()  
    thread3.stop()  
    #thread4.stop() 
    return 
if __name__=="__main__":
    print "开始时间:",time.strftime("%Y-%m-%d %H:%M:%S")
    all_urls=Getlinks.GetLinks().geturls()
    URLS.add_all_urls(all_urls)#将urls添加进url管理器中 
    test()
    print "结束时间:",time.strftime("%Y-%m-%d %H:%M:%S")
    #root_url="http://baike.baidu.com/view/21087.htm"
    #obj_spider = SpiderMain()
    #obj_spider.craw(root_url)