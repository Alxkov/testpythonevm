#!/usr/bin/python

import csv
import itertools
import sys

from random import randrange, sample
from random import *

def random_insert(lst, item):
    lst.insert(randrange(len(lst)+1), item)

def getlogvalue(opnd, row):
    if(opnd == '1'):
       return '1'
    if(opnd == '0'):
       return '0'
    if(row[opnd] == '1'):
       return '1'
    if(row[opnd] == '0'):
       return '0'

def neg(opnd):
    if(opnd == '1'):
       return '0'
    if(opnd == '0'):
       return '1'

def con(opnd1, opnd2):
    if(opnd1 == '1' and opnd2 == '1'):
       return '1'
    else:
       return '0'   

def dis(opnd1, opnd2):
    if(opnd1 == '0' and opnd2 == '0'):
       return '0'
    else:
       return '1'  

def checkcorrect(opndList, opsList, table):
    #return false if doesn't correspond with table
    #print("before")
    #print(opndList)
    for row in table:
        tmp1 = list(opndList)
        tmp2 = list(opsList)
        while len(tmp1) > 1:
            curOpr = tmp2.pop()
            curOpnd1 = tmp1.pop()
            if(curOpr == 'not'):
                tmp1.append(neg(getlogvalue(curOpnd1, row)))
            if(curOpr == 'and'):
                curOpnd2 = tmp1.pop()
                tmp1.append(con(getlogvalue(curOpnd1, row),getlogvalue(curOpnd2, row)))    
            if(curOpr == 'or'):
                curOpnd2 = tmp1.pop()
                tmp1.append(con(getlogvalue(curOpnd1, row),getlogvalue(curOpnd2, row))) 
        
        if(getlogvalue(tmp1[0], row) != row[len(row)-1]):
           #print("after")
           #print(opndList)
           return False
        #print("opndList:")
        #print(opndList)    
    #print("after")
   # print(opndList) 
    return True

def printcorrect(opndList, opsList, table):
    #return false if doesn't correspond with table
    #print("before")
    #print(opndList)
    res = ""
    for row in table:
        tmp1 = list(opndList)
        tmp2 = list(opsList)
        res = chr((tmp1.pop()) + ord('A'))
        while len(tmp1) >= 1 or len(tmp2) >= 1:
            curOpr = tmp2.pop()
            #curOpnd1 = tmp1.pop()
            if(curOpr == 'not'):
                res = "(" + " not" + res + ")"
            if(curOpr == 'and'):
                curOpnd1 = tmp1.pop()
                #curOpnd2 = tmp1.pop()
                #tmp1.append(con(getlogvalue(curOpnd1, row),getlogvalue(curOpnd2, row)))    
                res = "(" + res + " and " + chr(curOpnd1 + ord('A') ) + ")"
            if(curOpr == 'or'):
                curOpnd1 = tmp1.pop()  
                #curOpnd2 = tmp1.pop()
                #tmp1.append(con(getlogvalue(curOpnd1, row),getlogvalue(curOpnd2, row))) 
                res = "("+ res +" or " + chr(curOpnd1 + ord('A')) + ")"
        

        #print("opndList:")
        #print(opndList)    
    #print("after")
   # print(opndList) 
    return res

	
with open('test.csv', 'r') as fp:
    reader = csv.reader(fp, delimiter=',', quotechar='"')
    # next(reader, None)  # skip the headers
    data_read = [row for row in reader]
data_list = []
for i in data_read:
    data_list.append(list(i))

#print(data_read)
nOpnd = len(data_read[0]) - 1
x = range(nOpnd)

curnOpnd = 4

nFound = 0
N = sys.argv[1]
while nFound < int(N) :
  opndListList = [list(p) for p in itertools.product(x, repeat= curnOpnd)]
  for i in opndListList:
      if(nFound >= int(N)):
         break
      y = {'and','or'}
      oprListList = [list(t) for t in itertools.product(y, repeat=curnOpnd - 1)]
      for j in oprListList:
         if(random() > 0.5):
           random_insert(j,'not')
         if(random() > 0.3):
           random_insert(j,'not')
         if(random() > 2.1):
           random_insert(j,'not')
         if checkcorrect(i,j,data_list) == True:
           nFound = nFound + 1
           print("expr: " + repr(nFound))
           #print(i)
           #print(j) 
           print(printcorrect(i,j,data_list))
           if(nFound >= int(N)):
              break
    #print(oprListList)
  curnOpnd = curnOpnd + 1
print(nFound)



