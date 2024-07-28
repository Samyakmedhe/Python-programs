import os 

def main():
    print("Enter file name that you want open : ")
    Fname = input()

    if os.path.exists(Fname):
        print("unable to create file as file is allready existing ")
    else:
        open(Fname, "x")
        print("File gets sucesfully created")


if __name__ == "__main__":
    main()