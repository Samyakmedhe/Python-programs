def Pattern(No):
    i = 0
    j = 0
    for i in range(No):
        for j in range(No):
            print(" * ", end ="")
        print()

def main():
    print("Enter number :")
    No = int(input())

    result = Pattern(No)
    print(result)

if __name__ == "__main__":
    main()