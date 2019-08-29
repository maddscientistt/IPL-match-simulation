import yaml
import csv
import os
import time
start=time.clock()
dir1='C:/Users/test/Downloads/BTECH/SEM 5/Big Data/ipl_male/'
yaml_file_names = os.listdir(dir1)
i='0'
for files in yaml_file_names:
   
   fp1=open('C:/Users/test/Downloads/BTECH/SEM 5/Big Data/output/aaa'+i+'.csv','w')
   i=int(i) 
   i=i+1
   i=str(i)
   
   #fp1=open('aaa.csv','w')
   writer=csv.writer(fp1)
   #header=['innings','ball_no','team','batsman','bowler','non-striker','run_batsman','extras','total'] 
   #writer.writerow(header)
   
   with open(dir1+'/'+files,'r') as f:
       
       innings = yaml.load(f)
       #print(innings.keys())
       for inning in innings['innings']:
           
           for first in  inning:
                for ee in inning[first]:
                    if(ee=='deliveries'):
                      for num in inning[first][ee]:
                        for ii in num:
                            list1=[]
                            
                            list1.append(first)
                            list1.append(ii) 
                            list1.append(inning[first]['team'])
                            flag=0
                            ls=['1','2','3'] 
                            for jj in num[ii]:
                               
                              if(jj=='batsman'):
                                    ls[0]=(num[ii][jj])
                              if(jj=='bowler'):
                                    ls[1]=(num[ii][jj])
                              if(jj=='non_striker'):
                                    ls[2]=(num[ii][jj])
                              if(jj=='wicket'):
                                flag=1
                              #if(jj=='runs') :
                            list1.extend(ls)  
                            list1.append(num[ii]['runs']['batsman'])
                            list1.append(num[ii]['runs']['extras'])
                            list1.append(num[ii]['runs']['total'])
                            if(flag==1):
                                list1.append(num[ii]['wicket']['kind'])
                                list1.append(num[ii]['wicket']['player_out'])
                            writer.writerow(list1)                                 


print("time taken = ",time.clock())
