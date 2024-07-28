import sys
import os
import time

def DirectoryWatcher(Dirname, Extention):
    flag = os.path.isabs(Dirname)

    if(flag == False):
        Dirname = os.path.abspath(Dirname)
    
    exit = os.path.isdir(Dirname)

    if(exit == True):
        for foldername, subfolder, filename in os.walk(Dirname):
            for name in filename:
                if name.endswith(Extention):
                    print(name)
    else:
        print("there is no such directory ")
def main():
    print("------------------------------------------")
    print("-----------Directory Watcher--------------")
    print("------------------------------------------")
    
    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--H" or sys.argv[1] == "--h"):
            print("this script is used to perform directory traversal")
            exit()
        if(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("usage of script : ")
            print("Name_of_File  Name_Of__Directory Name_Of_Extention ")
            exit()
    
    if(len(sys.argv)== 3):
        try:
            starttime = time.time()
            DirectoryWatcher(sys.argv[1],sys.argv[2])
            endtime = time.time()

            print("time requred to excute the script is : ",endtime-starttime)

        except Exception as obj2:
            print("Unable to perform the task deu to ", obj2)

    else:
        print("Invaild option")
        print("use -- h option to get the help and use --u option to get the usage of application ")
        exit()


if __name__ == "__main__":
    main()