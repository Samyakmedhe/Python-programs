import sys
import os
import time

def DirectoryWatcher(DirName, Filename):
    Count = 0
    flag = os.path.isabs(DirName)

    if (flag == False):
        print("Path is not a absolute path")
        DirName = os.path.abspath(DirName)  
        print("Coverted absolute path is : ",DirName)  

    exit = os.path.isdir(DirName)
    if(exit == True):
        for foldername, subfoldername , filename in os.walk(DirName):
                for name in filename:
                    if name == Filename:
                        os.remove(os.path.join(foldername,name))
                        print("File gets deleted")
                        break

    else:
        print("there is no such directory")
def main():
    print("-----------------------------------------------")
    print("-------------- Directroy Watcher---------------")
    print("-----------------------------------------------")

    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "-H"):
            print("this script is used to perform Directory Traversal")
            exit()
    
        if(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Usage of the script :")
            print("Name_Of__file Name_Of_Directory  Name_of_file")
            exit()
    if(len(sys.argv) == 3):
        try:
            starttime = time.time()
            DirectoryWatcher(sys.argv[1])
            endtime = time.time()

            print ("Time requred to excute the script is : ",endtime-starttime)

        except Exception as obj2:
            print("Unable to perform the task deu to ",obj2)
    else:
        print("Invaild option")
        print("Use --h option to get the help and use --u option the usage of application")
        exit()

    print("-----------------------------------------------")
    print("------ thankyou for using our script ----------")
    print("----------Marvellous Infosystems---------------")

if __name__ == "__main__":
    main()