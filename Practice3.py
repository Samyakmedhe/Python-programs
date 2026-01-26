def facto(No):
    fact = 1
    for i in range(1 ,No + 1):
        fact = fact * i
    return fact

def main():
    print("Enter number :")
    No = int(input())

    result = facto(No)
    print(result)

if __name__ == "__main__":
    main()