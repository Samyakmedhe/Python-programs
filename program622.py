    
def Addition(iNo):
    
    i = 1 
    iSum = 0
    for i in range(1 , iNo +1):
        iSum = iSum + i 

    return iSum 

def main():
    print("Enter number : ")
    iValue = int(input())

    iRet = Addition(iValue)    
    print(f"Addition is : {iRet}")
if __name__ =="__main__":
    main()