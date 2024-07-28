import os
import psutil
from sys import *


def DisplayProcess(log_dir = 'Demo'):
    listprocess = []

    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass
    log_path = os.path.join(log_dir,"Demo.Log")
    
    f = open(log_path, 'w')

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid','name','username'])
            vms = proc.memory_info().vms / (1024 * 1024)
            pinfo['vms'] = vms
            listprocess.append(pinfo);
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    for element in listprocess:
        f.write("%s\n"%element)

def main():
    print("------Marvellous-----")
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
        DisplayProcess(argv[1])
    
    except ValueError:
        print("Error :Invalid datatype of input ")

    except Exception as E:
        print("Error : invalid input ",E)




if __name__ == "__main__":
    main()