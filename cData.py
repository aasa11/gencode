'''
Created on 2013/07/23

@author: huxiufeng
'''


class cData:
    def __init__(self, series, datas, d2):
        if len(datas)<6 :
            print str(datas),' is error length'
            return False
        #series
        self.series = int(series)
        #read datas , 6
        self.a = []
        for i in range(6) :
            self.a.append(int(datas[i]))
        #blue datas, 1
        self.b = int(d2)
     
    def samea(self,d):
        if self.a == d.a:
            return True
        return False    
        
    def __str__(self):
        '''return print str the data'''
        strs =  'series : '+ str(self.series)+ " red : "+ str(self.a)+ " blue : "+ str(self.b)
        return strs
        
    def sum(self):
        '''return a1+...a6'''
        datasum = 0
        for i in range(6):
            datasum += self.a[i]
        return datasum
    
    def gap(self):
        '''return a6-a1'''
        return self.a[5]-self.a[0]
    
    def cup(self):
        cup = 0
        for i in range(5):
            cup1 = self.a[i+1]-self.a[i]
            if cup1 > cup:
                cup = cup1
        return cup
    
    def odd(self):
        odd = 0 
        for i in range(6):
            if self.a[i] % 2 == 0 :
                odd +=1
        return odd
    
    def arr(self):
        arr = 0
        for i in range(6):
            if self.a[i] < 12:
                arr += 1
            elif self.a[i] < 23:
                arr +=10
            else :
                arr += 100
        return arr
    
    def ctn(self):
        ctn = 0
        for i in range(5):
            if self.a[i+1] - self.a[i] == 1:
                ctn +=1
        return ctn
    
    def tail(self):
        tail = 0
        for i in range(5):
            for j in range(i+1,6):
                if self.a[i]% 10 == self.a[j] % 10:
                    tail +=1
        return tail
    
    def first(self):
        return self.a[0]
    
    def last(self):
        return self.a[5]
    
    def idx(self,idx):
        return self.a[idx]
    
    def rept(self, d):
        rept = 0
        for i in range(6):
            for j in range(6):
                if self.a[i] == d.a[j] :
                    rept += 1
        return rept
        
                
        

#----------------------It is a split line--------------------------------------

def main():
    series =100
    datas = [1,2,3,4,5,6,16]
    d1 = cData(100, datas,datas[6])
    print d1
    print d1.sum()
    print d1.gap()
    
#----------------------It is a split line--------------------------------------

if __name__ == "__main__":
    main()
    print "It's ok"