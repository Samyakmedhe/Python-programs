import os 
def main():
    print("Enter file name that you want to open for writing purpose :  ")
    fname = input()

    if os.path.exists(fname):
        fobj = open(fname, "r")
        print("File is succesfull opened in write mode")

        Data = fobj.read()
        print(Data)
    else:
        print("unable to open file as file is not present in current directory")

if __name__ == "__main__":
    main()