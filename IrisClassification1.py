from sklearn import tree
from sklearn.datasets import load_iris

def main():
    print("---------- Iris Flower Classification case Study -----------")

    iris = load_iris()

    print(iris)
    # print(type(data))

    Features = iris.data
 
    Labels = iris.target

    print("Features are : ")
    print(Features)

    print("Labels are : ")
    print(Labels)
    
if __name__ == "__main__":
    main()