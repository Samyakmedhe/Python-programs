import sys

def Addition(A,B):
    return A + B
def main():
    print("-----------------------------------------------")
    print("------Automation to perform Addition ----------")
    print("-----------------------------------------------")

    if(len(sys.argv) == 2):

        if(sys.argv[1] == "--h" or sys.argv[1] == "-H"):
            print("this script is used to perform Addition of 2 intergral values")
            exit()
    
        if(sys.argv[1] == "--u"or sys.argv[1] == "--U"):
            print("Usage of the script :")
            print("Name_Of__file First_Argument  Second_Argument")
            print("Note : Both argument should be in integral format")
            exit()

        else:
            print("Invaild option")
            print("Use --h option to get the help and use --u option the usage of application")
            exit()
    if(len(sys.argv) == 3):
        try :
            ret = Addition(int(sys.argv[1]),int(sys.argv[2]))
            print("Addition is : ",ret)
        except ValueError as obj1:
            print("Invaild type of arguments")
        except Exception as obj2:
            print("Unable to perform the task ")
    else:
        print("Invaild option")
        print("Use --h option to get the help and use --u option the usage of application")
        exit()

    print("-----------------------------------------------")
    print("------ thankyou for using our script ----------")
    print("----------Marvellous Infosystems---------------")

if __name__ == "__main__":
    main()