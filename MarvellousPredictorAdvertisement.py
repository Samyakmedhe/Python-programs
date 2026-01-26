import pandas as pd 
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import numpy as np

def MarvellousPredictor():

    data = pd.read_csv("Advertising (1).csv")
    print("Size of Actual data set : ",data.shape)

    X = data[['TV', 'radio', 'newspaper']]
    Y = data['sales']
    X_train , X_test , Y_train , Y_test = train_test_split(X , Y , test_size = 0.3)

    n = len(X)
    reg  = LinearRegression()

    reg.fit(X_train , Y_train)

    y_pred = reg.predict(X)
    
    r2 = reg.score(X ,Y )

    print("Goodness of fit using R2 methos is :",r2)


def main():
    print("------- Marvellous ----------")

    print("------ Machine Learning --------")

    print("--- linear regression Algorithm -------")

    MarvellousPredictor()

if __name__ == "__main__":
    main()