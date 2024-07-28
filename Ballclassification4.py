from sklearn import tree

def MarvellousClassifire():
    
    Features = [[35,1],[47,1] , [90,0], [48,1] , [90,0] ,[35,1] ,[92,0] ,[35,1] ,[35,1 ],[35,1]]

    Labels = [1,1,2,1,2,1,2,1,1,1]
    
    obj = tree.DecisionTreeClassifier()

    obj = obj.fit(Features, Labels)

    ret  = obj.predict([[96,0]])

    if ret == 1:
        print("your object looks like Tennis ball")
    
    else:
        print("your object looks like cricket ball")


def main():

    print("------------Ball Classification case study------------ ")

    MarvellousClassifire()

if __name__ == "__main__":
    main()