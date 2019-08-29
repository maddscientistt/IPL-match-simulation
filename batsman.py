import csv
import copy
import time
import os
start=time.clock()
fp=open('kkk4.csv','w+')
writer=csv.writer(fp)
header=['batsman','bowler','wicket']
writer.writerow(header)
dir1='C:/Users/test/Downloads/BTECH/SEM 5/Big Data/output'
files = os.listdir(dir1)


list=[]
dic=dict()
for file in files:
    with open('C:/Users/test/Downloads/BTECH/SEM 5/Big Data/output/'+file,'r') as f:
   
        string=f.read()
        l=string.split('\n')
        list1=[j.split(',') for j in l] 
        list1.pop()
        for row in list1:
            if(len(row)==1) :
                continue
            t=(row[3],row[4])
            if t in dic and len(row)>9:
                dic[t]=dic[t]+1
            elif len(row)>9:
                dic[t]=1
for s in dic:
    l=[]
    l.append(s[0])
    l.append(s[1])
    l.append(dic[s])
    list.append(l)        
        


list=sorted(list,key=lambda x: (x[2]),reverse=True)
                  
for s in list:
        writer.writerow(s)

print("time taken = ",time.clock())            
