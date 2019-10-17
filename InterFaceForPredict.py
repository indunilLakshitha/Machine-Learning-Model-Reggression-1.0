import tkinter as tk
from tkinter import ttk
import csv
import joblib
import pandas as pd

from sklearn.linear_model import LinearRegression


top = tk.Tk()
fnt_lble='Helvetica 19 bold'
# scrollbar = tk.Scrollbar(top)
# scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
# data_day_set=0
# data_place_set=0
# data_time_set=0

 
 


def button():
    global data_time_set,data_place_set,data_day_set
    data_day_set=day.current()
    data_place_set=place.current()
    data_time_set=time.current()
    predicitCSV=[(data_time_set,data_day_set,data_place_set)]
    csvfile=open('predictCSV.csv','w',newline='')
    obj=csv.writer(csvfile)
    for person in predicitCSV:
        obj.writerow(person)
        obj.writerow(person)
    csvfile.close()

    clsfr=joblib.load('Rides_Predictor_2.sav')
    dataset=pd.read_csv('predictCSV.csv').values
    data=dataset[:,0:3]
    result=clsfr.predict(data)

    ##---------------------------------------------------------linear

    clsfr_linear=joblib.load('Rides_predictor_linear_count.sav')

    result_linear=clsfr_linear.predict(data)
    print('linear : ',result_linear)

    ##--------------------------------------------
# print(result)
# a=int(input("Enter : "))
# b=int(input("Enter : "))
# c=int(input("Enter : "))
# d=int(input("Enter : "))
# results=clsfr.predict(a,b,c,d)
# label=results[0]
    pr='Ride count will be : ',result_linear
    print(result)
    lable_rslt.config(text=pr,bg='BLUE')
##    if(result==1):
##        lable_rslt.config(text='Ride count will be 50++',bg='BLUE')
##    else:
##        lable_rslt.config(text='Ride count will be 50--',bg='BLUE')
##    

selecting_time_range=tk.StringVar()
time=ttk.Combobox(top,width=20,textvariable=selecting_time_range)
time['values']=('12.00am-2.00am','2.00am-4.00am','4.00am-6.00am''6.00am-8.00am','8.00am-10.00am','10.00am-12.00pm','12.00pm-2.00pm',\
                '2.00pm-4.00pm','4.00pm-6.00pm','6.00pm-8.00pm','8.00pm-10.00pm','10.00pm-12.00am')
time.grid(row=0,rowspan=7,column=1)

selecting_place=tk.StringVar()
place=ttk.Combobox(top,width=20,textvariable=selecting_place)
place['values']=('Colombo 01','Colombo 02','Colombo 03','Colombo 04','Colombo 05','Colombo 06','Colombo 07','Colombo 08','Colombo 09','Colombo 10','Colombo 11','Colombo 12','Colombo 13','Colombo 14','Colombo 15')
place.grid(row=8,column=1)

selecting_day=tk.StringVar()
day=ttk.Combobox(top,width=20,textvariable=selecting_day)
day['values']=('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday')
day.grid(row=7,column=1)

lable_check=tk.Label(top,text='PREDICTING TIME',fg='white',font=fnt_lble)
lable_check.grid(row=0,column=0)

lable_day=tk.Label(top,text='PREDICTING DAY',fg='white',font=fnt_lble)
lable_day.grid(row=7,column=0,)

lable_place=tk.Label(top,text='PREDICTING PLACE',fg='white',font=fnt_lble)
lable_place.grid(row=8,column=0)

button_result=tk.Button(top,text='RESULT',bg='green',fg='white',font=fnt_lble,command=button)
button_result.grid(row=9,column=0,columnspan=2)

lable_rslt=tk.Label(top,text='                 ',bg='purple',fg='white',font=fnt_lble,width=35)
lable_rslt.grid(row=10,column=0,columnspan=2)

top.mainloop()
