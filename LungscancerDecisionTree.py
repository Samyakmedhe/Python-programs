import pandas as pd
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def MarvellousPredictor():
    data = pd.read_csv("dataset.csv")

    print("Actual size of dataseat : ",data.shape)

    X = data[["SMOKING","YELLOW_FINGERS","ANXIETY","PEER_PRESSURE","CHRONIC_DISEASE","FATIGUE","ALLERGY","WHEEZING","ALCOHOL_CONSUMING","COUGHING","SHORTNESS_OF_BREATH","SWALLOWING_DIFFICULTY","CHEST_PAIN"]]
    Y = data["LUNG_CANCER"]

    Xtrain , Xtest , Ytrain , Ytest = train_test_split(X,Y ,test_size = 0.3)

    clf  = tree.DecisionTreeClassifier()
    clf.fit(Xtrain , Ytrain )
    prediction = clf.predict(Xtest)
    print("Having lungs cancer or not  : ",prediction)
    
    accuracy = accuracy_score(Ytest , prediction)
    print("Accurracy is : ",accuracy*100)

def main():
    print("---- Mavrelllous --------")

    print("lungs cancer case study Decision tree classifier ")

    MarvellousPredictor()
if __name__ =="__main__":
    main()