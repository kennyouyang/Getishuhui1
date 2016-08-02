#coding=utf-8
'''
Created on 2016年1月14日

@author: hadoop
'''
import urllib
import urllib2
import cookielib
import os
from bs4 import BeautifulSoup
import re

class GetLinks(object):
    def geturls(self):
        url="http://www.ishuhui.com/page/"
        isexist =  os.path.exists(r'output.txt')
        j=0
        set1 = set()
        for i in range(1, 10):
            
            print "第",i,"页"
            response2=urllib2.urlopen(url+str(i))
            print response2.getcode()
            if response2.getcode()==200:
                res = response2.read()
                #print res
                soup = BeautifulSoup(res,'html.parser',from_encoding='utf-8')
                print "获取div内容"
                div_nodes = soup.find_all('a',href=re.compile(r"http://www.ishuhui.com/archives/3"))#.find('a',href=re.compile(r"http://www.ishuhui.com/archives/"))
                #print div_nodes
                for div_node in div_nodes:
                    #print div_node,"***********\n"
                    #print div_node.get('href'),"------href\n"
                    #print div_node.get('title'),"------title\n"
                    print 'j:',j
                    j+=1 
                    set1.add(div_node.get('href')+"\r\n")
                    '''if(isexist==False):
                        fout = open('output.txt','w')
                        isexist=True
                    else: 
                        fout = open('output.txt','a')
                    
                    fout.write(div_node.get('href')+"\r\n")'''
        if(isexist==False):
            fout = open('output.txt','w')
            isexist=True
        else: 
            fout = open('output.txt','a')
        print set1
        for set2 in set1:
            fout.write(set2)
            print set2
        fout.close() 
        return set1


