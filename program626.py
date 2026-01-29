
def CountEvenDigit(iNo):
    iCountEven = 0 
    iDigit = 0

    while(iNo != 0):
        iDigit = iNo % 10 
        if(iDigit % 2 == 0):
            iCountEven+= 1
        iNo = iNo // 10 
    
    return iCountEven

def main():

    print("Enter number : ")
    iValue = int(input())

    iRet = CountEvenDigit(iValue)
    print(f"Number of Even Digits in {iValue} are : {iRet}")

if __name__ =="__main__":
    main()