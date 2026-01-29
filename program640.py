
def Addition(Brr):
    iSum = 0 
    for i in Brr:
        iSum = iSum + i
    
    return iSum
def main():
    print("Enter the Number of Elements : ")
    iLength = int(input())

    Arr = [] 
    print("please Enter the Elements : ")
    for i in range(1 ,iLength+1):
        No = int(input())
        Arr.append(No)

    iRet = Addition(Arr)
    print(f"Addition of Elements is : {iRet}")

if __name__ =="__main__":
    main()