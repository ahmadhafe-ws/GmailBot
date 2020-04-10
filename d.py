

import smtplib

def sendEmail(gmail_user,gmail_pwd ,FROM ,TO ,SUBJECT,TEXT):

    # Prepare actual message
    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
      #server = smtplib.SMTP(SERVER)
      server = smtplib.SMTP("smtp.gmail.com", 587) #or port 465 doesn't seem to work!
      server.ehlo()
      server.starttls()
      server.login(gmail_user, gmail_pwd)
      server.sendmail(FROM, TO, message)
      #server.quit()
      server.close()
      print ('successfully sent the mail')
      return (True)
    except:
      print ("failed to send mail")
      return(False)
