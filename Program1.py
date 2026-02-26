

def EvenOdd(iNo):
    if iNo % 2 == 0:
        return True
    else:
        return False
    

def main():
    iValue = 0

    print("Enter number : ")
    iValue = int(input())

    bRet = EvenOdd(iValue)
    if bRet:
        print(iValue,"is Even number...")
    else:
        print(iValue,"is Odd number...")



if __name__ == "__main__":
    main()