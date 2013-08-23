#!/usr/bin/
#coding=utf-8
'''
Created on 2013/08/23

@summary: 

@author: huxiufeng
'''
import urllib2
import re

class webdata:
    def __init__(self, urls):
        self.url = urls
        page = urllib2.urlopen(self.url)
        data = page.read()
        
    def getdata(self):
        page = urllib2.urlopen(self.url)
        data = page.read()
        #print data
        
        idx = data.find('百度乐彩</a><span class="tsuf tsuf-op" ')
        if idx <= 0:
            print "error data"
            return
        data = data[idx+5:]
        fd1 = r'<p class="op_caipiao_date">'
        fd2 = r'开奖日期'
        
        idx1 = data.find(fd1)
        idx2 = data.find(fd2)
        if idx <= 0 or idx2 <= idx1 :
            print "err data"
            return
        
        data = data[idx1: idx2+1]
        self.formdata(data)
        

    def formdata(self,data):
        self.onedata = []
        cmp1 = re.compile('第(\d*)期')
        n1 = cmp1.findall(data)
        if len(n1) <= 0:
            print "error now"
            return
        
        cmp2 = re.compile('<span class=\"op_caipiao_red\">(\d*)</span>')
        n2 = cmp2.findall(data)
        if len(n2)< 6:
            print "error red"
            return

        cmp3 = re.compile('<span class=\"op_caipiao_green\">(\d*)</span>')
        n3 = cmp3.findall(data)
        if len(n3)< 1:
            print "error blue"
            return

        self.onedata.append(n1[0])
        for i in xrange(6) :
            self.onedata.append(n2[i])
        self.onedata.append(n3[0])
        print self.onedata

#----------------------It is a split line--------------------------------------

def main():
    urls = r'http://www.baidu.com/s?wd=%CB%AB%C9%AB%C7%F2'
    wd = webdata(urls)
    wd.getdata()
    
#----------------------It is a split line--------------------------------------

if __name__ == "__main__":
    main()
    print "It's ok"