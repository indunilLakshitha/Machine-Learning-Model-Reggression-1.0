import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

csv_new = pd.read_csv("dsata_set_hot.csv").values
print('creating pickle.....')
data=csv_new[:,0:3]
target=csv_new[:,4]
target_count=csv_new[:,3]
train_data,test_data,train_target,test_target=train_test_split(data,target,test_size=0.1)
clsfr=KNeighborsClassifier(n_neighbors=2)
clsfr.fit(train_data,train_target)
results=clsfr.predict(test_data)
accuaracy=accuracy_score(test_target,results)
print("Accuaracy : ",accuaracy)

pickle.dump(data,open('data.pickle','wb'))
pickle.dump(target,open('target.pickle','wb'))
pickle.dump(target_count,open('target_count.pickle','wb'))
print('pickle file creating ---- Done')
