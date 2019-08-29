import csv
import copy
import time
import os
start=time.clock()
fp=open('kkk3.csv','w+')
writer=csv.writer(fp)
header=['bowler','batsman','runs']
writer.writerow(header)
dir1='C:/Users/test/Downloads/BTECH/SEM 5/Big Data/output'
files = os.listdir(dir1)
#files=['aaa0.csv','aaa0.csv']

list=[]

dic=dict()
for file in files:
    with open('C:/Users/test/Downloads/BTECH/SEM 5/Big Data/output/'+file,'r') as f:
    #with open(file,'r') as f:
        string=f.read()
        l=string.split('\n')
        list1=[j.split(',') for j in l] 
        list1.pop()
        #print (list1)
        
        for row in list1:
            if(len(row)==1) :
                continue
            t=(row[4],row[3])
            if t in dic:
                dic[t]=dic[t]+int(row[6])
            else:
                dic[t]=int(row[6])
    
#print(dic)                 
for s in dic:
    l=[]
    l.append(s[0])
    l.append(s[1])
    l.append(dic[s])
    list.append(l)
list=sorted(list,key=lambda x:(-x[2])) 
for s in list:
        writer.writerow(s)
print("time taken = ",time.clock())             
