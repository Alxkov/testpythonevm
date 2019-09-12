#!/usr/bin/python

import csv
def getlogvalue(opnd, row):
    if(opnd == 't'):
       return 't'
    if(opnd == 'f'):
       return 'f'
    if(row[opnd] == 't'):
       return 't'
    if(row[opnd] == 'f'):
       return 'f'

def neg(opnd):
    if(opnd == 't'):
       return 'f'
    if(opnd == 'f'):
       return 't'

def con(opnd1, opnd2):
    if(opnd1 == 't' and opnd2 == 't'):
       return 't'
    else:
       return 'f'   

def dis(opnd1, opnd2):
    if(opnd1 == 'f' and opnd2 == 'f'):
       return 'f'
    else:
       return 't'  

def checkcorrect(opndList, opsList, table):
    #return false if doesn't correspond with table
    for row in table:
        while len(opndList) > 1:
            curOpr = opsList.pop()
            curOpnd1 = opndList.pop()
            if(curOpr == 'n'):
                opndList.append(neg(getlogvalue(curOpnd1, row)))
            if(curOpr == 'c'):
                curOpnd2 = opndList.pop()
                opndList.append(con(getlogvalue(opnd1),getlogvalue(opnd2)))    
            if(curOpr == 'd'):
                curOpnd2 = opndList.pop()
                opndList.append(con(getlogvalue(opnd1),getlogvalue(opnd2))) 

        
    return True

with open('test.csv', 'r') as fp:
    reader = csv.reader(fp, delimiter=',', quotechar='"')
    # next(reader, None)  # skip the headers
    data_read = [row for row in reader]

print(data_read)
nOpnd = len(data_read[0])



