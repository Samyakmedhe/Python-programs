
def ReverseArray(Brr):
    iStart = 0
    iEnd = len(Brr)-1

    while( iStart < iEnd):
        Brr[iStart],Brr[iEnd] = Brr[iEnd],Brr[iStart]

        iStart+= 1
        iEnd -= 1

def main():
    print("Enter the Number of Elements : ")
    iLength = int(input())

    Arr = [] 
    print("please Enter the Elements : ")
    for i in range(1 ,iLength+1):
        No = int(input())
        Arr.append(No)

    ReverseArray(Arr)
    print(Arr)
if __name__ =="__main__":
    main()