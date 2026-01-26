
class Arthmatic:
    def Add(A , B):
        return A + B
    
    def sub(A , B):
        return A - B

    def Multi(A, B):
        return A * B
    
    def Div(A ,B):
        if B != 0:
            return A / B
        else:
            print("Cannnot divide by zero... ")


def main():
    print("Enter first number : ")
    No1 = int(input())

    print("Enter Second number : ")
    No2 = int(input())

    Obj = Arthmatic
    result = Obj.Add(No1 , No2)
    print("Addition of two number is : ",result)

    result = Obj.sub(No1, No2)
    print("Substraction of two number is : ",result)

    result = Obj.Multi(No1, No2)
    print("multipilcation of two numbwe is : ",result)

    result = Obj.Div(No1, No2)
    print("Divide of two number is : ",result)

if __name__ == "__main__":
    main()