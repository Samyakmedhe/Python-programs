import os 
import time 
import psutil
import urllib.request
import smtplib
import schedule
from sys import *
from email import encoders 
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.message import EmailMessage

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


def processLog(log_dir = "Marvellous"):
    listprocess = []
    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass
    
    separator = "-" * 80
    log_path = os.path.join(log_dir,"Marvellouslog%s.log"%(time.ctime()))
    f = open(log_path,'w')
    f.write(separator + "\n")
    f.write("Marvellous Infossytem Process Logger : "+time.ctime() + "\n")
    f.write(separator + "\n")
    f.write("\n")

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid','name','username'])
            vms = proc.memory_info().vms / (1024 * 1024)
            pinfo['vms'] = vms
            listprocess.append(pinfo)
        except (psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass
    for element in listprocess:
        f.write("%s\n"%element)

    print("Log file is succesfully genration at loaction %s "%(log_path))

    startTime = time.time()
    MailSender(log_path,time.ctime())
    endTime = time.time()

    print('Took %s second to send mail ' %(endTime - startTime))




    print("----------marvellous Infosytem----------")

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

    
