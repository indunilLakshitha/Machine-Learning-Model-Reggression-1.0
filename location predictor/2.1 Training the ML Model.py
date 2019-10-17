import pickle
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import joblib
from sklearn.metrics import accuracy_score
# import data_set
data=pickle.load(open('2data.pickle','rb'))
target=pickle.load(open('2target.pickle','rb'))
# training the ML model
clsfr=KNeighborsClassifier()
clsfr.fit(data,target)
# saving the trained model
joblib.dump(clsfr,'LngLat_Predictor.sav')