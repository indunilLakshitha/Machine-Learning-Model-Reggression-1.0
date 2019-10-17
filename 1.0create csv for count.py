
import pandas as pd
import numpy as np
import csv
import datetime
from sklearn import tree
import re
import numpy

##l=100000
dataset=pd.read_csv('latlong.csv')

file = open("latlong.csv")
l = (len(file.readlines())-5)  ##l is count of rows in csv

print("reading lines ....",l)


list_csv=np.arange(l*4).reshape(l,4)
week_no=np.arange(l)
day_index=np.arange(l)
##time_index=np.arange(len)
time_index=[]
##loc_index=np.arange(15)
loc_index=[]
##count_=np.arange()




for a in range(0,l):
    date=dataset.Date[a]
    y = datetime.datetime.strptime(date, '%m/%d/%Y')
    week_no[a]=y.strftime("%U")
    day_index[a]=y.strftime("%w")

print("week no -- done ")
print("day no -- done ")
time_range=[200,400,600,800,1000,1200,1400,1600,1800,2000,2200,2400]
for a in range(0,l):
    t=dataset.Time[a]
    T=re.sub(r':',r'',t)
    
    for b in range(0,12):
        j=int(time_range[b])
        if(int(T)<=j):
            v=time_range.index(j)
            time_index.append(v)
            break
        
print("time no -- done ")            
print("locations predicting . . . . . ")          

for i in range(0, l):
    lat = dataset.latitude_from[i]
    long = dataset.longitude_from[i]
    features = [[6.9361, 79.845], [6.9199, 79.854], [6.8989, 79.8538], [6.8961, 79.8571],[6.8841,79.8759],
                [6.874657,79.860483],[6.9117,79.8646],[6.91472,79.87778],[6.9286,79.8686],[6.92327,79.8691],
                [6.93408,79.85],[6.9382,79.8605],[6.94278,79.85861],[6.9475,79.87472],[6.9,79.86667]]
    labels = ['Colombo 01', 'Colombo 02', 'Colombo 03', 'Colombo 04','Colombo 05',
              'Colombo 06','Colombo 07','Colombo 08','Colombo 09','Colombo 10',
              'Colombo 11','Colombo 12','Colombo 13','Colombo 14','Colombo 15']
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(features, labels)
    Area = clf.predict([[lat, long]])
    g=labels.index(Area)
    loc_index.append(g)

print("location no -- done ")

for i in range(0,l):
    list_csv[i][0]=week_no[i]
    list_csv[i][1]=day_index[i]
    list_csv[i][2]=time_index[i]
    list_csv[i][3]=loc_index[i]
    

print("writing csv .......")

##print(list_csv)


numpy.savetxt('output.csv',list_csv,delimiter=",")

print("csv -- done ")
import count























    
