

def main():
    print("Enter the Number of Elements : ")
    iLength = int(input())

    Arr = [] 
    print("please Enter the Elements : ")
    for i in range(1 ,iLength+1):
        No = int(input())
        Arr.append(No)

    print(Arr)

if __name__ =="__main__":
    main()