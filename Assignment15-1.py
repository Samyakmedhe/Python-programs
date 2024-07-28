from sklearn import metrics
from sklearn import datasets 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

def WinePredictor():
    wine = datasets.load_wine()
    print()

    print(wine.feature_names)
    print()

    print(wine.data[0:5])
    print()
    print(wine.target)

    X_train , X_test , Y_train , Y_test  = train_test_split(wine.data , wine.target , test_size = 0.3)

    knn = KNeighborsClassifier(n_neighbors = 3)

    knn.fit(X_train , Y_train)

    y_pred = knn.predict(X_test)

    print("Acurracy is : ",metrics.accuracy_score(Y_test,y_pred))

def main():
    print("-----marvellous predictor -----")
    print()
    print("Machine learning Apllication")

    print("Wine predictor application using KNN logorithm")

    WinePredictor()

if __name__ == "__main__":
    main()