# coding=gbk
'''
Created on 2013/07/23

@author: huxiufeng
'''
import cData

class crule:
    def __init__(self):
        self.sumcount = 0
        self.gapcount = 0
        self.cupcount = 0
        self.oddcount = 0
        self.arrcount = 0
        self.ctncount = 0
        self.tailcount = 0
    
    def printstat(self):
        print ' self.sumcount   ', self.sumcount    
        print ' self.gapcount   ', self.gapcount    
        print ' self.cupcount   ', self.cupcount    
        print ' self.oddcount   ', self.oddcount    
        print ' self.arrcount   ', self.arrcount    
        print ' self.ctncount   ', self.ctncount    
        print ' self.tailcount  ', self.tailcount   

    
    def checkrule(self, d):
        self.matched = 0
        if  self.checksum(d):
            self.matched += 1
        if  self.checkgap(d):
            self.matched += 1
        if  self.checkcup(d):
            self.matched += 1
        if  self.checkodd(d):
            self.matched += 1
        if  self.checkarr(d):
            self.matched += 1
        if  self.checkctn(d):
            self.matched += 1
        if  self.checktail(d):
            self.matched += 1
        
        if self.matched == 7:
            return True
        else :
            return False
    
    def checksum(self, d):
        if d.sum() <= 125 and d.sum() >= 95:
            self.sumcount += 1
            return True
        return False
    
    def checkgap(self, d):
        if d.gap() <= 30 and d.gap() >= 21:
            self.gapcount += 1
            return True
        return False
    
    def checkcup(self, d):
        if d.cup() <= 13 and d.cup() >= 7:
            self.cupcount += 1
            return True
        return False
    
    def checkodd(self, d):
        if d.odd() <= 4 and d.odd() >= 2:
            self.oddcount += 1
            return True
        return False
    
    def checkarr(self, d):
        arr = d.arr()
#        if arr == 123 or arr == 132 \
#            or arr == 213 or arr == 231 \
#            or arr ==312 or arr ==321 \
#            or arr ==222:
        if arr in (123, 132, 213, 231, 222, 321, 312):
            self.arrcount += 1
            return True
        return False
    
    def checkctn(self, d):
        if d.ctn() == 1 or d.ctn() == 0:
            self.ctncount += 1
            return True
        return False
    
    def checktail(self, d):
        if d.tail() == 1 or d.tail() == 0:
            self.tailcount += 1
            return True
        return False


class genCode:
    def __init__(self, maxone, count):
        self.maxone = maxone
        self.count = count
        self.total = 0
        
    def gencode(self):
        d = []
        for i in range(self.count):
            d.append(i + 1)
        while True:
            d = self.getnext(d)
            if d is not None:
                cd = cData.cData(0, d, 0)
                self.total += 1
                yield cd
            else : 
                break
        yield None
        
        
    def getnext(self, now):
        isuseful = False
        if now[self.count - 1] < self.maxone:
            now[self.count - 1] += 1
            return now
        else :
            
            for i in range(1, self.count):
                if now[self.count - 1 - i] < self.maxone - i:
                    isuseful = True
                    now[self.count - 1 - i] += 1
                    p = self.count - 1 - i
                    for j in range(p + 1, self.count):
                        now[j] = now[j - 1] + 1
                    break
            if isuseful:
                return now
            else:
                return None

#----------------------It is a split line--------------------------------------

def main():
    filename = r'choose.txt'
    gen = genCode(33, 6)
    f = open(filename, 'w')
    rule = crule()
    matched = 0
    dictpart = {}
    for d in gen.gencode():
        # print d
        if d is None:
            break
        elif rule.checkrule(d):
            oneline = str(d.series) + ' '
            for i in range(6) :
                oneline += str(d.a[i]) + ' '
            oneline += str(d.b) + ' \n'
            f.write(oneline)
            matched += 1
            # print d
         
        part = rule.matched
        if part in dictpart.keys():
            dictpart[part] +=1
        else:
            dictpart[part] = 1
    
    f.close()
    print gen.total
    print matched
    rule.printstat()
    for k,v in dictpart.items():
        print "k : ", k, ", v : ", v
    
#----------------------It is a split line--------------------------------------

if __name__ == "__main__":
    main()
    print "It's ok"
