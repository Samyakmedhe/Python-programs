# input : 721 
# 1  2  3    
def SumDigits(iNo):
    iDigit = 0
    iSum = 0
    while(iNo != 0):
        iDigit = iNo % 10 
        iSum = iSum + iDigit
        iNo = iNo // 10 

    return iSum
    
def main():
    print("Enter number : ")
    iValue = int(input())

    iRet = SumDigits(iValue)    
    print(f"Summation of Digits is : {iRet}")
   
if __name__ =="__main__":
    main()