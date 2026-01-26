from sklearn import tree 

def DecisionTree(weight, Surface):
    ballsFeature = [[35,1],[47,1],[90,0], [48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0],[35,1], 
    [95,0]]
    Names = [1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]

    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(ballsFeature, Names)
    result = clf.predict([[weight,Surface]])
    if result == 1 :
        print("Your Object look like Tennis ball")
    elif result == 2 :
        print("Your Object look like Cricket ball")
    


def main():
    weight = input("Enter weight : ")

    print("What is the Surface type of object Rough or Smooth ")

    Surface = input()
    if Surface.lower() == "rough":
        Surface = 1 
    elif Surface.lower()=="smooth":
        Surface = 0 
    else:
        print("Error : wrong Input")
        exit()
    DecisionTree(weight, Surface)

if __name__== "__main__":
    main()