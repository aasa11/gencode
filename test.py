'''
Created on 2013/07/24

@author: huxiufeng
'''
import time

#----------------------It is a split line--------------------------------------

def main():
    now = time.time()
    print now
    time.sleep(1)
    new = time.time()
    print new
    a = new-now
    print a
        
    
#----------------------It is a split line--------------------------------------

if __name__ == "__main__":
    main()
    print "It's ok"