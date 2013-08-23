#!/usr/bin/
#coding=gbk
'''
Created on 2013/08/23

@summary: 

@author: huxiufeng
'''
import xlsHelper


class AddCode:
    def __init__(self, clst, xlsfile,sheetname):
        self.clst = clst
        self.xlsfile = xlsfile
        self.sheetname = sheetname
    
    def writetoxls(self):
        xls = xlsHelper.ExcelHelper(self.xlsfile)
        sheetnum = xls.getSheetCount()
        bsheetexist = False
        for i in range(sheetnum):
            xls.getSheet(i+1)
            sheetname = xls.GetSheetName()
            #print sheetname
            if sheetname == self.sheetname :
                bsheetexist = True
                break
        if not bsheetexist:
            print "no sheet: ", self.sheetname
            return False
            
        xls.activateSheet(self.sheetname)
        rows = xls.GetUsedRowsNum()
        
        rows +=1
        for idx, v in enumerate(self.clst):
            newrows = rows + idx
            print newrows, v
            for idx2 , v2 in enumerate(v):
                xls.setCell(newrows, idx2+1, str(v2))
        xls.saveandclose()



#----------------------It is a split line--------------------------------------

def main():
    xlsfile = r"F:\Code\ecprj\gencode\base.xls"
    sheetname  =r'color'
    clst = [ [2013098, 7, 15,18,19,20,26,14], 
             
             ]
    ad = AddCode(clst, xlsfile, sheetname)
    ad.writetoxls()
    
#----------------------It is a split line--------------------------------------

if __name__ == "__main__":
    main()
    print "It's ok"