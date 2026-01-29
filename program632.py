


def SumFactor(iNo):
    
    iSum = 0 
    for i in range(1, (iNo//2)+1):
        if(iNo % i == 0 ):
            iSum += i 
    return iSum

def main():
    print("Enter number : ")
    iValue = int(input())

    iRet = SumFactor(iValue)
    print(f"Summation of Factor of {iValue} is : {iRet}")

if __name__ =="__main__":
    main()