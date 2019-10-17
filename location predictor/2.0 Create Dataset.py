import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from matplotlib import pyplot as plt
import numpy as np
import pickle

# import CSV file to data_set variable
data_set = pd.read_csv('LngLat.csv').as_matrix()
print(data_set)
# create the data & target
data = data_set[:,0:2]
target=data_set[:,2]
# classification
train_data,test_data,train_target,test_target=train_test_split(data,target,test_size=0.1)
# algorithm
clsfr=KNeighborsClassifier(n_neighbors=3)
# clsfr=SVC(kernel='linear')
# clsfr=SVC(kernel='poly',degree=2)
# clsfr=SVC(kernel='rbf')
clsfr.fit(train_data,train_target)
# predicting
results=clsfr.predict(test_data)
print(test_target)
print(results)
# check the accuracy
accuracy=accuracy_score(test_target,results)
print("Accuracy : ",accuracy)
# create the data_set
data=np.array(data)
target=np.array(target)
pickle.dump(data,open('2data.pickle','wb'))
pickle.dump(target,open('2target.pickle','wb'))