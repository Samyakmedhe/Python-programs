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

def DisplayChecksum(path):
    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    if exists:
        for dirname, subdir, fileList in os.walk(path):
            print("current floder is : "+dirname)
            for filen in fileList:
                path = os.path.join(dirname, filen)
                file_hash = hashfile(path)
                print(path)
                print(file_hash)
                print(' ')
    else:
        print("Invaild path")


def main():
    print("-----Marvellous Infosystems by Samyak medhe------ ")

    print("Application name : "+argv[0])

    if(len(argv) != 2):
        print("Error : Invaild number of argument")
        exit()

    if(argv[1] == "-h")or (argv[1] == "-H"):
        print("this script is used to travse specfic directory and display Chechsum of file ")
        exit()
    
    if(argv[1] == "-u")or (argv[1] == "-U"):
        print("usage : ApplicationName absolutionPath_of_directory Extention")
        exit()

    try:
        arr = DisplayChecksum(argv[1])
    
    except ValueError:
        print("Error : Invaild data type of input")

    except Exception as E:
        print("Error : Invaild input",E)

if __name__ == "__main__":
    main()
