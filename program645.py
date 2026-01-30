
def ReverseArray(Brr):
    for i in range(len(Brr)-1,-1,-1):
        print(Brr[i]) 
def main():
    print("Enter the Number of Elements : ")
    iLength = int(input())

    Arr = [] 
    print("please Enter the Elements : ")
    for i in range(1 ,iLength+1):
        No = int(input())
        Arr.append(No)

    ReverseArray(Arr)
   
if __name__ =="__main__":
    main()