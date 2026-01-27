def CheckEvenOdd(No1):
    if No1 % 2 == 0:
        return True
    else:
        return False

def main():
    print("Enter first number : ")
    Value1 = int(input())
    
    bRet = CheckEvenOdd(Value1)
    if bRet:
        print(f"{Value1} is Even number..")
    else:
        print(f"{Value1} is Odd number..")

if __name__ =="__main__":
    main()