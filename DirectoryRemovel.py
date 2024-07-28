from sys import *
import os
import hashlib
import time
import logging

def DeleteFiles(dict1):
    results = list(filter(lambda X : len(X) > 1 , dict1.values()))

    iCnt = 0
    if len(results) > 0:
        for result in results:
            for subresult in result:
                iCnt += 1
                if iCnt >= 2:
                    os.remove(subresult)
            iCnt = 0
    else:
        print("Duplicate not found ") 

    
def hashfile(path , blocksize = 1024):
    afile = open(path , 'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()

    return hasher.hexdigest()

def FindDup(path):
    flag = os.path.isabs(path)

    if flag == False:
        path = os.path.abspath(path)
    
    exists = os.path.isdir(path)

    dups = {}
    
    if exists:
        for dirname , subdirs , fileList in os.walk(path):
            print("Current folder is : "+dirname)
            for filen in fileList:
                path = os.path.join(dirname , filen)
                file_hash = hashfile(path)

                if file_hash in dups:
                    dups[file_hash].append(path)
                else:
                    dups[file_hash] = [path]
        return dups
    else:
        print("Invalid Path ")

def printResult(dict1):
    results = list(filter(lambda X : len(X) > 1 ,dict1.values()))

    if len(results) > 0:
        print("duplicate Found : ")
        print("the following files are Duplicate")

        for result in results:
            for subressult in result:
                print("\t\t%s"%subressult)
    else:
        print("No duplicate Found ")

def main():
    print("----- Marvellous Infossytem-------")

    print("Applicatio name : "+argv[0])
    if(len(argv)!= 2):
        print("Error : invalid number Arguments")
        exit()

    if(len(argv[1]) == "--h" or (argv[1]) == "--H"):
        print("this Script is use to delete Duplicate file ")
        exit()
    
    if(len(argv[1]) == "--u" or (argv[1]) == "--U"):
        print("ApplicationName AbsolutePath_of_Directory Extention ")
        exit()
    
    try:
        arr = {}
        startTime = time.time()
        arr = FindDup(argv[1])
        printResult(arr)
        DeleteFiles(arr)
        endTime = time.time()

        print('Took %s seconds to evalute..'%(endTime - startTime))
    
    except ValueError:
        print("Error : invalid datatype of input")
    
    except Exception as E:
        print("Error : Invalid input",E)



if __name__ == "__main__":
    main()







    