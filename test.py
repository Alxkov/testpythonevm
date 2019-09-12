#!/usr/bin/python

import csv

def checkcorrect(opndList, opsList, table):
    #return false если выражение не удовлетворяет некоторой строчке в таблице
    return True

with open('test.csv', 'r') as fp:
    reader = csv.reader(fp, delimiter=',', quotechar='"')
    # next(reader, None)  # skip the headers
    data_read = [row for row in reader]

print(data_read)
nOpnd = len(data_read[0])

