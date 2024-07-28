from sys import *
import os
import hashlib

def hashfile(path, blocksize = 1024):
    afile = open(path, 'rb')
    hasher = hashlib.md5()

    buf = afile.read(blocksize)
    
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    
    afile.close()
    
    return hasher.hexdigest()

def findDupliacate(path):
    flag = os.path.isabs(path)

    if flag == False:
        path = os.path.abspath(path)
    exists = os.path.isdir(path)
    dups = {}

    if exists:
        for dirname , subdir, fileList in os.walk(path):
            for filen in fileList:
                path = os.path.join(dirname , filen)
                file_hash = hashfile(path)
                if file_hash in dups:
                    dups[file_hash].append(path)
                else:
                    dups[file_hash] = [path]
        return dups
    
    else:
        print("Invalid path ")


def printDupliacate(dict1 , log_dir = "log.txt"):
    results = list(filter(lambda X : len(X) > 1,dict1.values()))

    if(len(results) > 0):
        print("Duplicate found ")

        print("the following files are indentical ")
        iCnt = 0
        for i in results:
            for subresult in i:
                iCnt += 1
                if iCnt > 2:
                    print("\t\t%s"%subresult)
                    path = os.path.join(log_dir,"log.txt")
                    f = open(path, 'w')
    else:
        print("Duplicate not found ..")

def main():
    print("--------marvellous Infosystem---------")
    print("Application name : ",argv[0])

    if(len(argv) != 2):
        print("Error : Invaild number of argument")
        exit()

    if(argv[1] == "-h")or (argv[1] == "-H"):
        print("this script is used to print Dupliacate file into log file ")
        exit()
    
    if(argv[1] == "-u")or (argv[1] == "-U"):
        print("usage : ApplicationName absolutionPath_of_directory Extention")
        exit()

    
    Arr = {}
    Arr = findDupliacate(argv[1])
    printDupliacate(Arr)
        


if __name__ == "__main__":
    main()
