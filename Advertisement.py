import pandas as pd 
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split


def MarvellousPredictor():
    data = pd.read_csv("Advertising (1).csv")
    print("Actual size : ",data.shape)

    X = data[["TV","radio","newspaper",]]
    Y = data["sales"]

    Xtrain , Xtest , Ytrain, Ytest = train_test_split(X,Y ,test_size = 0.3)

    n = len(X)
    reg = LinearRegression()

    reg.fit(Xtrain , Ytrain)

    p_yed = reg.predict(Xtest)

    r2 = reg.score(X,Y)
    print("R2 value is : ",r2)


def main():
    print("------marvellous------")

    print("Advertisment linear Regression ")

    MarvellousPredictor()

if __name__ == "__main__":
    main()