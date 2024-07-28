import os
import hashlib
import shutil
import smtplib
from sys import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time


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



def MailSender(filename , time ):

    formaddr = "samyakmedhe796@gmail.com"
    toaddr = "medhesamyak990@gmail.com"
    sender_password = "qmji cqdx hdbo ijml"
    msg = MIMEMultipart()

    msg['From'] = formaddr

    msg['To'] = toaddr

    body = """
    Hello %s
    wellcome to marvellous Infossytems.
    please find attacched document which contain log runging process.
    log file is created at : %s 

    this is Automation genration mail.

    thankyou & Regareds,
    Samyak kailas Medhe
        """%(toaddr,time)

    Subject = """
    Marvellous Infosytem Process log genration at : %s
    """%(time)

    msg['Subject'] = Subject
     
    msg.attach(MIMEText(body , 'plain'))
    
    
    with open(filename,'rb') as attachment: 
        p = MIMEBase('application', 'octet-stream')
        p.set_payload((attachment).read())

    encoders.encode_base64(p)

    p.add_header('Content-Disposition', f"attachment; filename = {filename}")
    msg.attach(p)

    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.starttls()

    server.login(formaddr,sender_password)

    text = msg.as_string()

    server.sendmail(formaddr, toaddr, text)

    server.quit()

    print("log file succefully sent through Mail")

if __name__ == "__main__":

    print("--------------Marvellous----------------")
    print("Application Name : "+argv[0])

    if(len(argv)!= 2):
        print("Error : invalid number Arguments")
        exit()
        
    if(len(argv[1]) == "--h" or (argv[1]) == "--H"):
        print("this script is used log record of running processes")
        exit()
    
    if(len(argv[1]) == "--u" or (argv[1]) == "--U"):
        print("Usage : ApplicationName AbsolutePath_of_directory ")
        exit()
    
    try :
        schedule.every(int(argv[1])).minute.do(processLog)
        while True:
            schedule.run_pending()
            time.sleep(1)
    
    except ValueError:
        print("ERROR : Invalid datatype of input")
    except Exception as E:
        print("Error : Invalid input ",E)
