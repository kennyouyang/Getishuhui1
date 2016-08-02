#coding=utf-8
'''
Created on 2016年1月12日

@author: hadoop
'''
from bs4 import BeautifulSoup
import re
import urlparse

class HtmlPaser(object):#解析器
    
    
    '''def _get_new_urls(self, page_url, soup):#补充新的url
        new_urls = set()
        #/view/123.htm
        links = soup.find_all('a',href=re.compile(r"/view/\d+\.htm"))
        for link in links:
            new_url = link['href']
            new_full_url=urlparse.urljoin(page_url,new_url)#补全url
            new_urls.add(new_full_url)
        return new_urls'''
    
    
    #def _get_new_data(self, page_url, soup):#解析当前url的数据
    def _get_new_data(self, page_url,soup, html_cont):#解析当前url的数据
        res_data ={}
        #把url也放进数据中
        '''res_data['url']=page_url
        #<dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
        title_node = soup.find('dd',class_="lemmaWgt-lemmaTitle-title").find("h1")
        res_data['title'] = title_node.get_text()
        #<div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div',class_="lemma-summary")
        res_data['summary'] = summary_node.get_text()'''
        print "获取h1"
        title = soup.h1
        res_title=title.string
        print 'title：',res_title
        
        reg=r'src="(.+?\.png)" alt'
        imgre = re.compile(reg)
        res_data = re.findall(imgre,html_cont)
        
        return res_title,res_data
    
    
    def parse(self,page_url,html_cont):#解析
        print "正在解析中..."
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
        #new_urls = self._get_new_urls(page_url,soup)
        #new_data = self._get_new_data(page_url,soup) 
        new_title,new_data = self._get_new_data(page_url,soup,html_cont)
        print "解析完成...",new_title,new_data
        return new_title,new_data
    



