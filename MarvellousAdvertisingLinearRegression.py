import numpy as np 
import pandas as pd 
from sklearn import metrics
from sklearn.linear_model import LinearRegression 
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plot 



def MarvellousAdvertisemnetPredictor(Data_Path):

    data = pd.read_csv(Data_Path , index_col = 0)

    print("Actual size of dataset",len(data))

    Features = ['TV','radio' ,'newspaper']

    print("Name of Features", Features)

    X = data[Features]
    Y = data.sales

    X_train , X_test  , Y_Train , Y_test = train_test_split(X, Y , test_size = 0.3)

    print("size of training dataset ", len(X_train))

    print("Size of testing dataset ", len(X_test))

    linreg = LinearRegression()
    linreg = linreg.fit(X_train , Y_Train)

    ypred = linreg.predict(X_test)

    print("Testing Set ")
    print(X_test)

    print("Result of testing")
    print(ypred)
    
    print(np.sqrt(metrics.mean_squared_error(Y_test , ypred)))


def main():

    MarvellousAdvertisemnetPredictor("Advertising (1).csv")
if __name__ == "__main__":
    main()