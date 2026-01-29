# input : 721 
# 1  2  3    
def DisplayDigits(iNo):
    iDigit = 0
    while(iNo != 0):
        iDigit = iNo % 10 
        iNo = iNo // 10 
        print(iDigit)

    
def main():
    print("Enter number : ")
    iValue = int(input())

    DisplayDigits(iValue)    
   
if __name__ =="__main__":
    main()