CheckEven = lambda No : (No % 2 == 0)
Increase = lambda No : No + 1
Add = lambda A,B : A+B


def filterX(Task, Elements):
    Result = []   

    for no in Elements:
        Ret = Task(no)

        if(Ret == True):
            Result.append(no)
            
    return Result

def mapX(Task, Elements):
    Result = []

    for no in Elements:
        Ret = Task(no)
        Result.append(Ret)
    
    return Result

def reduceX(Task , Elements):
    Sum = 0

    # [15,21,19,17,21]
    for no in Elements:
        Sum = Task(Sum,no)

    return Sum

def main():
    Data = []

    print("Enter number of elements : ")
    Size = int(input())

    print("Enter the elements : ")
    iCnt = 0
    for iCnt in range(0,Size):
        No = int(input())
        Data.append(No)    
        
    print("Data form input list : ",Data)

    FData = list(filterX(CheckEven,Data))
    print("Data after filter activity : ",FData)

    MData = list(mapX(Increase, FData))
    print("Data after map activity : ",MData)

    RData = reduceX(Add, MData)
    print("Data after reduce activity is : ",RData)

if __name__ == "__main__":
    main()


