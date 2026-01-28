    
def Display(iNo):
    i = 1
    for i in range(1, iNo + 1):
        print("*", end = "\t")
    print()

def main():
    print("Enter number : ")
    iValue = int(input())

    Display(iValue)    
if __name__ =="__main__":
    main()