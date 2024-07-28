import numpy as np 
import pandas as pd 
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier

def MarvellousPlayPredictor():
    data = pd.read_csv('PlayPredictor (2).csv')

    print("Size of Actual data : ",len(data))
    print()

    feature_name = ['Whether' , 'Temperature']

    print("Name of Feature : ", feature_name)
    print()

    Whether = data.Whether
    Temperature = data.Temperature
    Play  = data.Play

    le = preprocessing.LabelEncoder()
    print("Transform Whether in Encoded : ")

    Whether_encoded = le.fit_transform(Whether)

    print(Whether_encoded)
    print()

    print("Transfrom Temperature in Encoded :  ")
    Temp_encoded = le.fit_transform(Temperature)
    label = le.fit_transform(Play)
    print(Temp_encoded)
    print()


    features = list(zip(Whether_encoded , Temp_encoded))

    model = KNeighborsClassifier(n_neighbors = 3)

    model.fit(features , label)

    predicted = model.predict([[0,2]])
    print("Answer of this Predictor : ")
    print(predicted)
    print()

    print("Play or Not :  ")

    if predicted:

        print("Play..")
        print()
    else:
        print("Not")
        print()

def main():
    print("-------- Mavrellous Play Predictor -------")

    print("------------Machine Learning-------------")

    print("--- Play predictor unsing KKN algorithm ---")

    MarvellousPlayPredictor()
if __name__ == "__main__":
    main()