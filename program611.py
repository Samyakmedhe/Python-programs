def Maximum(No1, No2 , No3):
    iMax = 0
    if No1 > No2 and No1 > No3:
        iMax = No1
    elif No2 > No1 and No2 > No3:
        iMax = No2
    else:
        iMax = No3

    return iMax
    
def main():
    print("Enter first number : ")
    Value1 = int(input())
    print("Enter Second number : ")
    Value2 = int(input())
    print("Enter Third number : ")
    Value3 = int(input())
    

    iRet = Maximum(Value1, Value2 , Value3)
    print(f"Maximum number is : ",iRet)
if __name__ =="__main__":
    main()