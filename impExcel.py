#!usr/bin/python
#coding=GBK
'''
Created on 2013/07/23

@author: huxiufeng
'''
#coding=utf-8
import xlsHelper
import cData


class cDataImp:
    def __init__(self, filename, sheetname):
        self.filename = filename
        self.sheetname = sheetname
        self.datas = []
        
    def importdata(self):
        xls = xlsHelper.ExcelHelper(self.filename)
        sheetnum = xls.getSheetCount()
        bsheetexist = False
        for i in range(sheetnum):
            xls.getSheet(i+1)
            sheetname = xls.GetSheetName()
            print sheetname
            if sheetname == self.sheetname :
                bsheetexist = True
                break
        if not bsheetexist:
            print "no sheet: ", self.sheetname
            return False
            
        xls.activateSheet(self.sheetname)
        rows = xls.GetUsedRowsNum()
        for index in range(4, rows+1):
            onedata = []
            ser = xls.getCell(index, 1)
            if ser is None:
                continue
            try :
                ser = int(ser)
            except Exception, e:
                print ser, " transfer int err, ", e
                continue
            if ser <= 0:
                continue
            useful = True
            for col in range(2,9):
                ond = xls.getCell(index, col)
                if ond is None :
                    useful = False
                    break
                try :
                    ond = int(ond)
                except Exception, e:
                    print ond, " transfer int2 err, ", e
                    useful = False
                    break
                onedata.append(ond)
            if useful :
                d1 = cData.cData(ser, onedata,onedata[6])
                self.datas.append(d1)
        xls.close()
        return True
        
    def printdata(self):
        for d in self.datas:
            print str(d)
            
    def writetofile(self, filename):
        f = open(filename, 'w')
        for d in self.datas:
            oneline = str(d.series)+ ' '
            for i in range(6) :
                oneline += str(d.a[i])+ ' '
            oneline += str(d.b)+' \n'
            f.write(oneline)
        f.close()


class statcode:
    def __init__(self, filename):
        self.filename = filename
        
    def importdata(self):
        self.datas = []
        f = open(self.filename, 'r')
        for line in f.readlines():
            data = line.split(' ')
            #print data
            d = cData.cData(data[0], data[1:],data[6])
            self.datas.append(d)
            
        f.close()
    
    def getcount(self):
        return len(self.datas)
    
    
    def sumrange(self):
        dictsum = {}
        for d in self.datas :
            sum = d.sum()
            if sum in dictsum.keys() :
                dictsum[sum] += 1
            else :
                dictsum[sum] = 1
        return dictsum
    
    def gaprange(self):
        dictgap = {}
        for d in self.datas:
            gap = d.gap()
            if gap in dictgap.keys():
                dictgap[gap] +=1
            else :
                dictgap[gap] = 1
        return dictgap
    
    def cuprange(self):
        dictcup = {}
        for d in self.datas:
            gap = d.cup()
            if gap in dictcup.keys():
                dictcup[gap] +=1
            else :
                dictcup[gap] = 1
        return dictcup
    
    def oddrange(self):
        dictodd = {}
        for d in self.datas:
            odd = d.odd()
            if odd in dictodd.keys():
                dictodd[odd] += 1
            else :
                dictodd[odd] = 1
        return dictodd
    
    def arrrange(self):
        dictarr = {}
        for d in self.datas:
            arr = d.arr()
            if arr in dictarr.keys():
                dictarr[arr] += 1
            else :
                dictarr[arr] = 1
        return dictarr
    
    def ctnrange(self):
        dictctn = {}
        for d in self.datas:
            ctn = d.ctn()
            if ctn in dictctn.keys():
                dictctn[ctn] += 1
            else :
                dictctn[ctn] = 1
        return dictctn
    
    def tailrange(self):
        dicts = {}
        for d in self.datas:
            value = d.tail()
            if value in dicts.keys():
                dicts[value] += 1
            else :
                dicts[value] = 1
        return dicts 
    
    def firstrange(self):
        dicts = {}
        for d in self.datas:
            value = d.first()
            if value in dicts.keys():
                dicts[value] += 1
            else :
                dicts[value] = 1
        return dicts 
    
    def lastrange(self):
        dicts = {}
        for d in self.datas:
            value = d.last()
            if value in dicts.keys():
                dicts[value] += 1
            else :
                dicts[value] = 1
        return dicts 

    
#----------------------It is a split line--------------------------------------

def main():
    filename = r"F:\Code\ecprj\gencode\base.xls"
    writefilename = r'color.txt'
    sheetname = r'color'
    d = cDataImp(filename, sheetname)
    d.importdata()
    d.printdata()
    d.writetofile(writefilename)

    st = statcode(writefilename)
    st.importdata()
    print st.getcount()
#    dicts = st.sumrange()
#    count = 0
#    for k,v in dicts.items():
#        if v > 15:
#            print k, " : ", v
#            count += v
#    print 'count : ', count, ", percent : ", (float)(count)*100/st.getcount(),"%"
    
#    dicts = st.gaprange()
#    count = 0
#    for k,v in dicts.items():
#        if v > 70:
#            print k, " : ", v
#            count += v
#    print 'count : ', count, ", percent : ", (float)(count)*100/st.getcount(),"%"

#    dicts = st.cuprange()
#    count = 0
#    for k,v in dicts.items():
#        if v > 85:
#            print k, " : ", v
#            count += v
#    print 'count : ', count, ", percent : ", (float)(count)*100/st.getcount(),"%"

#    dicts = st.oddrange()
#    count = 0
#    for k,v in dicts.items():
#        if v > 150:
#            print k, " : ", v
#            count += v
#    print 'count : ', count, ", percent : ", (float)(count)*100/st.getcount(),"%"
    
#    dicts = st.arrrange()
#    count = 0
#    for k,v in dicts.items():
#        if v > 60:
#            print k, " : ", v
#            count += v
#    print 'count : ', count, ", percent : ", (float)(count)*100/st.getcount(),"%"

#    dicts = st.ctnrange()
#    count = 0
#    for k,v in dicts.items():
#        if v > 400:
#            print k, " : ", v
#            count += v
#    print 'count : ', count, ", percent : ", (float)(count)*100/st.getcount(),"%"

#    dicts = st.tailrange()
#    count = 0
#    for k,v in dicts.items():
#        if v > 300:
#            print k, " : ", v
#            count += v
#    print 'count : ', count, ", percent : ", (float)(count)*100/st.getcount(),"%"
    
    dicts = st.firstrange()
    print dicts
    count = 0
    for k,v in dicts.items():
        if v > 100:
            print k, " : ", v
            count += v
    print 'count : ', count, ", percent : ", (float)(count)*100/st.getcount(),"%"
    
    dicts = st.lastrange()
    count = 0
    for k,v in dicts.items():
        if v > 100:
            print k, " : ", v
            count += v
    print 'count : ', count, ", percent : ", (float)(count)*100/st.getcount(),"%"
    
#----------------------It is a split line--------------------------------------

if __name__ == "__main__":
    main()
    print "It's ok"