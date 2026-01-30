
def ReverseArray(Brr):

    crr = []
    for i in range(len(Brr)-1,-1,-1):
        crr.append(Brr[i])

    return crr
def main():
    print("Enter the Number of Elements : ")
    iLength = int(input())

    Arr = [] 
    print("please Enter the Elements : ")
    for i in range(1 ,iLength+1):
        No = int(input())
        Arr.append(No)

    Data = ReverseArray(Arr)
    print(f"Reverse Array is : {Data}")
   
if __name__ =="__main__":
    main()