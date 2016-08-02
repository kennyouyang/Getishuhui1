#coding=utf-8
'''
Created on 2016年1月12日

@author: hadoop
'''


class UrlManager(object):
    def __init__(self):#构造函数
        self.new_urls=set()
        self.old_urls=set()
        
    
    
    def add_new_url(self,url):#在管理器中添加一个新的url
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:#url既不在新urls中，也不在已爬取的urls中
            self.new_urls.add(url)
    
    '''def add_new_urls(self,urls):#在管理器中添加新的url
        print "正在添加新的url..."
        if urls is None or len(urls)==0:#None or 列表为空
            return
        for url in urls:
            self.add_new_url(url)'''
            
    def add_all_urls(self,urls):#在管理器中添加所有要下载的url
        print "正在添加新的url..."
        if urls is None or len(urls)==0:#None or 列表为空
            return
        for url in urls:
            self.add_new_url(url)
           
    
    
    def has_new_url(self):#判断管理器中是否有新的待爬取的url
        return len( self.new_urls)!=0

    
    def get_new_url(self):#从url管理器中获取一个新的待爬取的url
        print "正在获取待爬取的url..."
        #print "出栈前",self.new_urls
        new_url = self.new_urls.pop() #出栈
        #print "出栈后",self.new_urls
        self.old_urls.add(new_url)
        return new_url
        

    

    
    
    
    
    
    
    
