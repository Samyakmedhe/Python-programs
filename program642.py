
def Minimum(Brr):
    iMin = Brr[0]
    for i in Brr:
        if iMin > i :
            iMin = i 
    
    return iMin
def main():
    print("Enter the Number of Elements : ")
    iLength = int(input())

    Arr = [] 
    print("please Enter the Elements : ")
    for i in range(1 ,iLength+1):
        No = int(input())
        Arr.append(No)

    iRet = Minimum(Arr)
    print(f"Minimum number of Elements is : {iRet}")

if __name__ =="__main__":
    main()