#coding=utf-8
'''
Created on 2016年1月19日

@author: hadoop
'''
from bs4 import BeautifulSoup
import re
res = "<h1>欺诈游戏 第185话 | 攻击与防御</h1>"
soup = BeautifulSoup(res,'html.parser',from_encoding='utf-8')
print "获取h1"
div_nodes = soup.h1
print div_nodes.string
