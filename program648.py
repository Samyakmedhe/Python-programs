
def Update(Brr):

    crr = []
    for i in range(len(Brr)-1,-1,-1):
        if(Brr[i] % 2 == 0 ):
            Brr[i] += 1 
def main():
    print("Enter the Number of Elements : ")
    iLength = int(input())

    Arr = [] 
    print("please Enter the Elements : ")
    for i in range(1 ,iLength+1):
        No = int(input())
        Arr.append(No)

    Update(Arr)
    print(Arr)
if __name__ =="__main__":
    main()