import pandas as pd 
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

def MarvellousPredictor():
    data = pd.read_csv('Advertising (1).csv')

    print("Size of Actual dataset : ",data.shape)

    X = data[['TV','radio','newspaper']].values
    Y = data['sales'].values

    X_train , X_test , Y_train , Y_test = train_test_split(X , Y , test_size = 0.3)

    n = len(X)

    reg = LinearRegression()

    reg.fit(X_train , Y_train)

    y_pred = reg.predict(X)

    r2 = reg.score(X ,Y)

    print(r2)

def main():
    print("--------Marvellous predictor---------")

    print("----------Machine learning-------")

    print("----- Linear Regreesion on Advertisement ---")

    MarvellousPredictor()
if __name__ == "__main__":
    main()
