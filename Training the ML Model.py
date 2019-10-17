import pickle
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LinearRegression

import joblib
from sklearn.metrics import accuracy_score

data=pickle.load(open('data.pickle','rb'))
target=pickle.load(open('target.pickle','rb'))
target_linear=pickle.load(open('target_count.pickle','rb'))


clsfr_linear=LinearRegression()
clsfr_linear.fit(data,target_linear)
joblib.dump(clsfr_linear,'Rides_predictor_linear_count.sav')

clsfr=KNeighborsClassifier()
clsfr.fit(data,target)
joblib.dump(clsfr,'Rides_Predictor_2.sav')
##train_data,test_data,train_target,test_target=train_test_split(data,target)
# clsfr=KNeighborsClassifier()
# clsfr.fit(train_data,train_target)
# results=clsfr.predict(test_data)
# print(results)
# print(test_target)
# accuracy=accuracy_score(test_target,results)
# print("Accuracy : ",accuracy)
import InterFaceForPredict
