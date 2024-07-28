import psutil
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime
import time

def get_running_processes():
    return psutil.process_iter()

def create_log_file(log_dir):
    log_filename = os.path.join(log_dir, f"process_log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt")
    with open(log_filename, 'w') as f:
        f.write("PID\tName\tStatus\tMemory Usage\n")
    return log_filename

def write_process_info(log_file):
    with open(log_file, 'a') as f:
        for proc in get_running_processes():
            try:
                pid = proc.pid
                name = proc.name()
                status = proc.status()
                mem_usage = proc.memory_info().rss
                f.write(f"{pid}\t{name}\t{status}\t{mem_usage}\n")
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

def send_email(sender_email, sender_password, receiver_email, subject, body, attachment):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    with open(attachment, 'rb') as attachment_file:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment_file.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f"attachment; filename= {attachment}")
    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    text = msg.as_string()
    server.sendmail(sender_email, receiver_email, text)
    server.quit()

if __name__ == "__main__":

    interval = int(input("Enter time interval (in seconds): "))
    log_dir = input("Enter directory path to save log file: ")

    while True:
        log_file = create_log_file(log_dir)
        write_process_info(log_file)
        print(f"Log file created: {log_file}")

        # Email settings
        sender_email = "samyakmedhe796@gmail.com"
        sender_password = "envb sflc xmhz qkny"
        receiver_email = "medhesamyak990@gmail.com"
        subject = "Process Log"
        body = "Please find attached the log file containing information about running processes."

        send_email(sender_email,sender_password, receiver_email, subject, body, log_file)

        print("Log file sent via email.")

        time.sleep(interval)

