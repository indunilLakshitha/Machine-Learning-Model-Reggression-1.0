import pandas as pd
import numpy as np
import numpy

hot=50
csv_for_count =pd.read_csv("output.csv").values
csv_=open('output.csv')
l = (len(csv_.readlines())-5)  ##l is count of rows in csv
dt=np.arange(l)
week_list=np.arange(65520).reshape(52,7,12,15)
count_1=np.arange(1260).reshape(7,12,15)
count_1=np.zeros((7,12,15))

list_csv=np.arange(65520*5).reshape(65520,5)

a2=np.arange(1260,dtype=float).reshape(7,12,15)
a2=np.zeros((7,12,15))



r=0
for b in range(0,52):
    for c in range(0,7):
        for d in range(0,12):
            for e in range(0,15):
                week_list[b][c][d][e]=r
print('meke list values 0 --- Done')

print('Counting ..........')   
x=0    
for b in range(0,l):
    for c in range(0,52):
        if(csv_for_count[b,0]==c):
            for d in range(0,7):
                 for e in range(0,12):
                     if(csv_for_count[b,1]==d and csv_for_count[b,2]==e):
                         for f in range(0,15):
                             if(csv_for_count[b,3]==f):
                                 week_list[c][d][e][f]=week_list[c][d][e][f].astype(int)+1
##                                 print(c)
                                 x=x+1
##                                 print(b," ",c," ",d," ",e," ",f," "," ",week_list[c][d][e][f])

print('Counting Completed........')

                   
                       
print('searching hotspots........ larger than ',hot)                                         
x=np.arange(65520)                   
b=0
cont=-1
tot=0
for a in range(0,52):
    for b in range(0,7):
        for c in range(0,12):
            for d in range(0,15):
                cont=cont+1
                list_csv[cont][0]=b
                list_csv[cont][1]=c
                list_csv[cont][2]=d
                tot=tot+week_list[a][b][c][d]
                list_csv[cont][3]=week_list[a][b][c][d]
                if(week_list[a][b][c][d] >= hot):
                    list_csv[cont][3]=1
                else:
                    list_csv[cont][4]=0



numpy.savetxt('dsata_set_hot.csv',list_csv,delimiter=",")

print("csv to dataset -- done ")
print(tot)
import creat_dataset                    
                
                
                

                
              























                                   

##print(week_list)   
    
