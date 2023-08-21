import smtplib, ssl, os

def sendMail():
    sender_email = 'ted'
    reciever_email = 'ignasvolcokas@gmail.com' # receiver's email id
    message = "Subject: Daily Check-in \n\n {}".format(os.environ.get("FORM")) # Content to be sent
    context = ssl.create_default_context()


    with smtplib.SMTP(host='smtp.gmail.com', port = 587) as smtp:
        smtp.ehlo() # Identify yourself to an ESMTP server using EHLO
        smtp.starttls(context=context) # Put the SMTP connection in TLS (Transport Layer Security) mode
        smtp.ehlo() # Identify yourself to an ESMTP server using EHLO
        smtp.login('tedt3830@gmail.com', os.environ.get("EMAIL_PASSWORD"))  # Sender's email ID and password
        smtp.sendmail(sender_email, reciever_email, message)
        print('Check your email ;)')


sendMail()