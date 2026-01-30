
def Maximum(Brr):
    iSum = 0 
    iMax = Brr[0]
    for i in Brr:
        if iMax < i :
            iMax = i 
    
    return iMax
def main():
    print("Enter the Number of Elements : ")
    iLength = int(input())

    Arr = [] 
    print("please Enter the Elements : ")
    for i in range(1 ,iLength+1):
        No = int(input())
        Arr.append(No)

    iRet = Maximum(Arr)
    print(f"Maximum number of Elements is : {iRet}")

if __name__ =="__main__":
    main()