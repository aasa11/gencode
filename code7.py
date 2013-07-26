'''
Created on 2013/07/22

@author: huxiufeng
'''
#coding=gbk
import urllib2
import string



def getNewAnswer(ThisTermId):  
    update_url='http://www.js-lottery.com/excel/ck7ws.php'  
    idTag='<td class="font-12"><img src="http://img.js-lottery.com/image/point1.gif" mce_src="http://img.js-lottery.com/image/point1.gif" width="10" height="10">'  
    numTag='<td background="http://img.js-lottery.com/newimg/ball.png" align="center">'  
    html=urllib2.urlopen(update_url)  
    for line in html:  
        if idTag in line:  
            line=html.next()  
            line=line.replace(" ","")  
            itemId=string.atoi(line[0:5])  
            ThisTermId=string.atoi(ThisTermId)  
            if itemId==ThisTermId:  
                break;  
            else:  
                return None   
    icount=0  
    newAnswer=''  
    for line in html:  
        if numTag in line:  
            begin=line.find(numTag)+len(numTag)  
            newAnswer=newAnswer+line[begin]  
            if len(newAnswer)==7:  
                return newAnswer   
    return  None 


ThisTermId = 2013051 
newAnswer= getNewAnswer(ThisTermId)  
if newAnswer:  
    print '/n================================ %s serier is %s ================================/n'%(ThisTermId,newAnswer)  

#----------------------It is a split line--------------------------------------

def main():
    pass
    
#----------------------It is a split line--------------------------------------

if __name__ == "__main__":
    main()
    print "It's ok"