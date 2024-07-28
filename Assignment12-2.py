import psutil
import os
from sys import *

def ProcessDisplay():
    listprocess = []

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs= ['pid','name','username']) 
            listprocess.append(pinfo);

        except (psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass
    
    return listprocess

def main():
    print("Marvellous Infossytem : python automation")

    print("Application name : "+argv[0])

    if(len(argv)!= 2):
        print("Error : invalid number Arguments")
        exit()
        
    if(len(argv[1]) == "--h" or (argv[1]) == "--H"):
        print("this script is used to see running process")
        exit()
    
    if(len(argv[1]) == "--u" or (argv[1]) == "--U"):
        print("Usage : ApplicationName ")
        exit()

    try:
        listprocess = ProcessDisplay()
        for element in listprocess:
            print(element)
        
    
    except ValueError:
        print("Error :Invalid datatype of input ")

    except Exception as E:
        print("Error : invalid input ",E)

if __name__ == "__main__":
    main()