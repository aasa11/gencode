#!/usr/bin/
#coding=gbk
'''
Created on 2013/08/23

@summary: 

@author: huxiufeng
'''

import webdata
import addcode
import impExcel
import compare
import genCode
import random


#----------------------It is a split line--------------------------------------

def main():
    #const para set
    urls = r'http://www.baidu.com/s?wd=%CB%AB%C9%AB%C7%F2'
    moredata = []
    xlsfile = r'F:\Code\ecprj\gencode\base.xls'
    sheetname = r'color'
    writefilename = r'color.txt'
    filebase = r'choose.txt'
    filereal = r'color.txt'
    fileout = r'c.txt'
    
    #var para set
    excludedata = (7, 25, )
    includedata = (3,33)
    excluderange = (132,231)
    rulematchs = {genCode.CHECKCTN : 0,
                  genCode.CHECKTAIL : 1}
    getcount = 5
    
    
    #get from web
    print "(1) get data from web...."
    wd = webdata.webdata(urls)
    wd.getdata()
    
    #get if continue
    nextstep = raw_input("conutinue ?(press n to exit)...")
    if nextstep == 'n':
        return
    
    #add to excel
    print "(2) add data to xls...."
    insertdata = []
    for idx, w in enumerate(moredata):
        insertdata.append(w)
    insertdata.append(wd.onedata)
    ad = addcode.AddCode(insertdata, xlsfile, sheetname)
    ad.writetoxls()
    
    #readfromexcel to txt
    print "(3) read data from xls to txt...."
    d = impExcel.cDataImp(xlsfile, sheetname)
    d.importdata()
    d.writetofile(writefilename)
#    st = impExcel.statcode(xlsfile)
#    st.importdata()
#    print st.getcount()
    
    #choose data form
    print "(3.5) gene choose data"
    genCode.dochoosetxt(filebase)
    
    #gendata
    print "(4) gene availabel data...."
    cmps = compare.ccmp(filebase, filereal)
    cmps.impdata()
    ch = compare.cchoice(fileout, cmps.realdata)
    ch.setexcludeNum(excludedata)
    ch.setincludeNum(includedata)
    ch.setexcludeRange(excluderange)
    ch.setrulematchs(rulematchs)
    ch.choose()
    
        
    #random choose some data 
    print "(5) choose random data...."
    for _ in xrange(getcount):
        idx = random.randint(0, ch.totalchosen)
        print ch.chosen[idx]
    
        
        
    
    
#----------------------It is a split line--------------------------------------

if __name__ == "__main__":
    main()
    print "It's ok"