def CheckDivible(No1):
    if No1 % 3 == 0 and No1 % 5 == 0:
        return True
    else:
        return False

def main():
    print("Enter first number : ")
    Value1 = int(input())
    
    bRet = CheckDivible(Value1)
    if bRet:
        print(f"{Value1} is Divible by  3 and 5")
    else:
        print(f"{Value1} is Divible by  3 &(or) 5")

if __name__ =="__main__":
    main()