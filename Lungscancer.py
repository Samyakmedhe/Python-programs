import numpy as np 
import pandas as pd 
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
def MarvellousPredictor():
    data = pd.read_csv("dataset.csv")

    print("Actual size of dataset : ",data.shape)
    print()

    X = data[["SMOKING","YELLOW_FINGERS","ANXIETY","PEER_PRESSURE","CHRONIC_DISEASE","FATIGUE","ALLERGY","WHEEZING","ALCOHOL_CONSUMING","COUGHING","SHORTNESS_OF_BREATH","SWALLOWING_DIFFICULTY","CHEST_PAIN"]]
    Y = data["LUNG_CANCER"]

    n = len(X) 

    Xtrain , Xtest , Ytrain , Ytest = train_test_split(X,Y ,test_size = 0.3)
   
    model = KNeighborsClassifier(n_neighbors = 3)
    model.fit(Xtrain, Ytrain )

    prediction = model.predict(Xtest)
    print()
    print("Having Cancer or Not : ",prediction)
    
    print()
    Acuuracy = accuracy_score(Ytest , prediction)
    print("Acurracy of Lungs cancer is : ",Acuuracy*100)

    


def main():
    print("------ Mavrellous-------")

    print("Lungs Cancer case Study KNN logorithm")

    MarvellousPredictor()
if __name__ == "__main__":
    main()