'''
Created on 2013/07/24

@author: huxiufeng
'''
import cData
import genCode

class ccmp:
    def __init__(self, filebase, filereal):
        self.filebase = filebase
        self.filereal = filereal
        
    def impdata(self):
        self.basedata = []
        f = open(self.filebase, 'r')
        for line in f.readlines():
            data = line.split(' ')
            #print data
            d = cData.cData(data[0], data[1:],data[6])
            self.basedata.append(d)          
        f.close()
        print "base data len : ", len(self.basedata)
        
        self.realdata = []
        f = open(self.filereal, 'r')
        for line in f.readlines():
            data = line.split(' ')
            #print data
            d = cData.cData(data[0], data[1:],data[6])
            self.realdata.append(d)          
        f.close()
        print "real data len : ", len(self.realdata)
        
        
    def matched(self):
        self.matched = 0
        for d1 in self.basedata:
            for d2 in self.realdata:
                if d1.samea(d2):
                    self.matched +=1
        return self.matched
    
    def realinrule(self):
        self.dictreal = {}
        rule = genCode.crule()
        for d in self.realdata:
            rule.checkrule(d)
            part = rule.matched
            if part in self.dictreal.keys():
                self.dictreal[part] +=1
            else :
                self.dictreal[part] = 1
        rule.printstat()
        
        for k, v in self.dictreal.items():
            print "k : ", k, ", v : ",v
        print '\n'
            
    def realrept0(self):
        self.dictrept = {}
        d0 = self.realdata[0]
        for d1 in self.realdata:
            if d0.a ==d1.a:
                continue
            rept = d1.rept(d0)
            if rept in self.dictrept.keys():
                self.dictrept[rept] += 1
            else:
                self.dictrept[rept] = 1
            d0 = d1
        
        for k, v in self.dictrept.items():
            print "k : ", k, ", v : ",v
        print '\n'
        
    def realrept(self, idx):
        self.dictrept = {}
        count = len(self.realdata)
        for i in range(count-idx):
            d0 = self.realdata[i+idx-1]
            rept = 0
            for j in range(i, i+idx-1):
                d = self.realdata[j]
                rept += d0.rept(d)
            if rept in self.dictrept.keys():
                self.dictrept[rept] += 1
            else:
                self.dictrept[rept] = 1
        for k, v in self.dictrept.items():
            print "k : ", k, ", v : ",v
        print '\n'
        
    def realcover(self,idx):
        count = len(self.realdata)
        self.dictcover = {}
        for i in range(count-idx):
            dic = {}
            for j in range(i, i+idx):
                d = self.realdata[j]
                for p in d.a:
                    if p in dic.keys():
                        dic[p] += 1
                    else:
                        dic[p] = 1
            num = len(dic)
            if num in self.dictcover.keys():
                self.dictcover[num] += 1
            else :
                self.dictcover[num] = 1
        
        for k, v in self.dictcover.items():
            print "k : ", k, ", v : ",v
        print '\n'
        
#----------------------It is a split line--------------------------------------

class cchoice:
    def __init__(self,filename, datas):
        self.filename = filename
        self.datas = datas
        self.rule = genCode.crule()
        self.incodes = ()
        self.excode = ()
        self.exrange = ()
        
    def setincludeNum(self, values):
        self.incodes = values
        
    def setexcludeNum(self, values):
        self.excode = values
        
    def setexcludeRange(self, values):
        self.exrange = values
        
    def isIncludeCode(self, d):
        if self.incodes is None or len(self.incodes) <= 0:
            return True
        for i in d.a:
            if i in self.incodes :
                return True
        return False
    
    def isExcludeCode(self, d):
        if self.excode is None or len(self.excode) <= 0:
            return False 
        for i in d.a:
            if i in self.excode :
                return True
        return False
    
    def isExcludeRange(self, d):
        if self.exrange is None or len(self.exrange) <= 0:
            return False     
        if d.arr() in self.exrange :
            return True
        return False
    
    def choose(self):
        f = open(self.filename, 'w')
        gen = genCode.genCode(33,6)
        total = 0
        for d in gen.gencode():
            if d is None:
                continue
            
            #include & exclude
            if not self.isIncludeCode(d) :
                continue
            if self.isExcludeCode(d) :
                continue
            if self.isExcludeRange(d) :
                continue
            
            #range
            if not self.inrange(d):
                continue
            
            #kppi
            kpi = self.kpi(d)
            if not self.checkkpi(kpi):
                continue
            #rept
            rept2 = self.rept(d, 2)
            if not self.checkrept(rept2, 2):
                continue
            rept3 = self.rept(d, 3)
            if not self.checkrept(rept3, 3):
                continue
            rept4 = self.rept(d, 4)
            if not self.checkrept(rept4, 4):
                continue
            rept5 = self.rept(d, 5)
            if not self.checkrept(rept5, 5):
                continue
            
            #cover
            cover5 = self.cover(d, 5)
            if not self.checkcover(cover5, 5):
                continue
            cover10 = self.cover(d, 10)
            if not self.checkcover(cover10, 10):
                continue
            cover15 = self.cover(d, 15)
            if not self.checkcover(cover15, 15):
                continue
            cover20 = self.cover(d, 20)
            if not self.checkcover(cover20, 20):
                continue
            
            #print data
            oneline = ' data : '
            for i in d.a:
                oneline += str(i) + ' '
            oneline += ', kpi : '+ str(kpi)+', '
            oneline += 'rept: '+ str(rept2)+' '+ str(rept3)+' '+ str(rept4)+' '+ str(rept5)+', '
            oneline += 'cover: '+str(cover5)+ ' '+str(cover10)+ ' '+str(cover15)+ ' '+str(cover20)+ '\n '
            #print oneline
            f.write(oneline)
            total +=1
        
        f.close()
        print 'total : ', total
        
    def inrange(self,d):
        if d.first()<=6 and d.last()>=28:
            return True
        return False
     
     
    def kpi(self,d):
        self.rule.checkrule(d)    
        return self.rule.matched
    
    def checkkpi(self,kpi):
        if kpi >=5 and kpi <=6:
            return True
        return False
            
     
    def rept(self,d, idx):
        count = len(self.datas)
        rept = 0
        for i in range(count-idx,count):
            d0 = self.datas[i]
            rept += d.rept(d0)
        return rept
    
    def checkrept(self,d, idx):
        if idx<=2:
            if d>=1 and d<=1:
                return True
            else:
                return False
        elif idx==3:
            if d >=2 and d<=2:
                return True
            else:
                return False
        elif idx ==4:
            if d>=2 and d<=5:
                return True
            else :
                return False
        elif idx == 5:
            if d>=3 and d<=6:
                return True
            else :
                return False
        else :
            if d >=5:
                return True
            else:
                return False
            
            
    
    def cover(self, d, idx):
        count = len(self.datas)
        cover = 0
        dic = {}
        for i in range(count-idx, count):
            d0 = self.datas[i] 
            for j in d0.a:
                if j in dic.keys():
                    dic[j]+=1
                else:
                    dic[j]  =1
        for j in d.a:
            if j in dic.keys():
                dic[j]+=1
            else:
                dic[j]  =1 
        return len(dic)   
    
    def checkcover(self,d, idx):
        if idx <= 5:
            if d>=19 and d <=23:
                return True
            else:
                return False
        elif idx <= 10:
            if d >=27 and d <=30:
                return True
            else:
                return False
        elif idx <=15:
            if d >=30 and d <=33:
                return True
            else :
                return False
        elif idx <=20:
            if d >=32:
                return True
            else:
                return False
        else:
            if d >=33:
                return True
            else :
                return False

#----------------------It is a split line--------------------------------------

def main():
    filebase = r'choose.txt'
    filereal = r'color.txt'
    fileout = r'c.txt'
    cmps = ccmp(filebase, filereal)
    cmps.impdata()
#    print cmps.matched()
#    cmps.realinrule()
#    cmps.realrept(2)
#    cmps.realrept(3)
#    cmps.realrept(4)
#    cmps.realrept(5)
#    cmps.realcover(5)
#    cmps.realcover(10)
#    cmps.realcover(15)
#    cmps.realcover(20)
    ch = cchoice(fileout, cmps.realdata)
    excludedata = (25,21,24,19)
    includedata = (1, 17,33)
    excluderange = (123,132,231)
    ch.setexcludeNum(excludedata)
    ch.setincludeNum(includedata)
    ch.setexcludeRange(excluderange)
    ch.choose()
    
#----------------------It is a split line--------------------------------------

if __name__ == "__main__":
    main()
    print "It's ok"