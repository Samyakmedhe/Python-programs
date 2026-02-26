def SumDigit(iNo):
    
    iSum = 0 
    while(iNo != 0 ):
        iSum += iNo % 10
        iNo = iNo // 10 
    
    return iSum

def main():
    
    print("Enter number : ")
    iValue = int(input())

    iRet = SumDigit(iValue)
    print("Summation of ",iValue,"is : ",iRet)
if __name__ =="__main__":
    main()