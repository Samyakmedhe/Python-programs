from sklearn import tree

def MarvellousClassifire(weight , surface):
    
    Features = [[35,1],[47,1] , [90,0], [48,1] , [90,0] ,[35,1] ,[92,0] ,[35,1] ,[35,1 ],[35,1]]

    Labels = [1,1,2,1,2,1,2,1,1,1]
    
    obj = tree.DecisionTreeClassifier()

    obj = obj.fit(Features, Labels)

    ret  = obj.predict([[weight, surface]])

    if ret == 1:
        print("your object looks like Tennis ball")
    
    else:
        print("your object looks like cricket ball")


def main():

    print("------------Ball Classification case study------------ ")

    print("Please Enter the information about the Object that you want to test")
    print("Please enter weight of your object in grams")
    no = int(input())

    print("Please mention type of surface Rough / Smmoth ")
    data = input()

    if data.lower == "Rough":
        data == 1
    elif data.lower == "Smmoth":
        data == 0


    MarvellousClassifire(no,data)

if __name__ == "__main__":
    main()