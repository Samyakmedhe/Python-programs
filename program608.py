

def Addition(No1 , No2):
    Sum = 0 
    Sum = No1 + No2
    return Sum

def main():
    print("Enter first number : ")
    Value1 = int(input())

    print("Enter Second number : ")
    Value2 = int(input())
    
    Ans = Addition(Value1 , Value2)
    print(f"Addition is {Value1} & {Value2} is : {Ans}")


if __name__ =="__main__":
    main()