

def Factorial(iNo):
    iCnt = 1 
    iFact = 1 
    while iCnt <= iNo:
        iFact = iFact * iCnt
        iCnt += 1
    
    return iFact
def main():
    iValue = 0

    print("Enter Number : ")
    iValue = int(input())

    iRet = Factorial(iValue)
    print("Factorial of",iValue," is : ",iRet)
    
if __name__ == "__main__":
    main()