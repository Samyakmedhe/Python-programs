    
def Display(iNo):
    i = 1
    while i <= iNo :
        print("*\t")
        i = i + 1

def main():
    print("Enter number : ")
    iValue = int(input())

    Display(iValue)    
if __name__ =="__main__":
    main()