import sys
import os
import time 
def DirectoryRename(Dirname , Extention1, Extention2):
    flag = os.path.isabs(Dirname)

    if(flag == False):
        Dirname = os.path.abspath(Dirname)
    
    exit = os.path.isdir(Dirname)

    if(exit == True):
        for foldername , subfolder, filename in os.walk(Dirname):
            for name in filename:
                if os.rename(Extention1,Extention2): 
                    print(name)
                
                
    else:
        print("there is no such directory ")

def main():
    print("------------------------------------------")
    print("--------- Directory Watcher --------------")
    print("------------------------------------------")

    if(len(sys.argv) == 3):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("this is use for Diretory Traversal")
            exit()
        
        if(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Usage of script : ")
            print("Name_Of_File Name_of_first_Directory Name_Of_second_Directory")
            exit()
    if(len(sys.argv) == 4):
        try:
            starttime = time.time()
            DirectoryRename(sys.argv[1] , sys.argv[2],sys.argv[3])
            endtime = time.time()
            print("time requred  to excute the script : ",endtime-starttime)

        except Exception as obj2:
            print("unable to perform task deu to : ",obj2) 

    else:
        print("Invaild option")
        print("use -- h option to get the help and use --u option to get the usage of application ")
        exit()


if __name__ == "__main__":
    main()