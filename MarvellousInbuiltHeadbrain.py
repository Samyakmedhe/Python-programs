import pandas as pd
from sklearn.linear_model import LinearRegression 
from sklearn.metrics import mean_squared_error

def MarvellousHeadBrainPredictor():
    data = pd.read_csv('MarvellousHeadBrain (1).csv')

    print("size if date set : ",data.shape)

    X = data['Head Size(cm^3)'].values
    Y = data['Brain Weight(grams)'].values

    X = X.reshapes((-1 , 1))

    n = len(X)
    reg = LinearRegression()
    reg = reg.fit(X , Y)

    Y_pred = red.predict(X)

    r2 = reg.score(X , Y)
    print(r2)
    

def main():
    print("---------- Marvellous Infosystem ----------")

    print("---------Suervied Machine learning -------")

    print("--Linear Regression on Head and Brain size data set--")

    MarvellousHeadBrainPredictor()

if __name__ == "__main__":
    main()