#coding=utf-8
'''
Created on 2016年1月12日

@author: hadoop
'''
from nltk.downloader import urllib2
import socket
from _mysql import NULL
class HtmlDownloader(object):
    
    
    def download(self,url): 
        print "正在下载中..."
        socket.setdefaulttimeout(9.0)
        res = ''
        if url is None:
            return None
        try:
            respone = urllib2.urlopen(url,'',timeout=10)
            if respone.getcode()!=200:
                return None
            print "res = respone.read()..."
            #while respone.read()==NULL:
            res = respone.read() 
            
            print '下载成功，正在return...'
        except socket.timeout:
            print '超时'
            return None
        return res
        
    
    



