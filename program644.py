
def CountEvenOdd(Brr):
    iCountEven = 0 
  

    for i in Brr:
        if i % 2 == 0 :
            iCountEven+=1 

    return iCountEven , len(Brr)-iCountEven
def main():
    print("Enter the Number of Elements : ")
    iLength = int(input())

    Arr = [] 
    print("please Enter the Elements : ")
    for i in range(1 ,iLength+1):
        No = int(input())
        Arr.append(No)

    iRet1, iRet2 = CountEvenOdd(Arr)
    print(f"Count of Even number is  : {iRet1} and Odd elements : { iRet2}")
if __name__ =="__main__":
    main()