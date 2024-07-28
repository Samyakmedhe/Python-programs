from sklearn import tree

def main():
    print("Ball Classification case study")

    Features = [[35,1],[47,1] , [90,0], [48,1] , [90,0] ,[35,1] ,[92,0] ,[35,1] ,[35,1 ],[35,1]]

    Labels = [1,1,2,1,2,1,2,1,1,1]
    
    obj = tree.DecisionTreeClassifier()

    obj = obj.fit(Features, Labels)

    print(obj.predict([[96,0]]))
    print(obj.predict([[43,1]]))



if __name__ == "__main__":
    main()