import smtplib, ssl

def sendMail():
    sender_email = 'ted'
    reciever_email = 'ignasvolcokas@gmail.com' # receiver's email id
    f = open("text.txt", "r")
    password = f.readline()
    form = f.readline()
    message = "Subject: Daily Check-in \n\n {}".format(form) # Content to be sent
    print(password)
    print(form)
    context = ssl.create_default_context()


    with smtplib.SMTP(host='smtp.gmail.com', port = 587) as smtp:
        smtp.ehlo() # Identify yourself to an ESMTP server using EHLO
        smtp.starttls(context=context) # Put the SMTP connection in TLS (Transport Layer Security) mode
        smtp.ehlo() # Identify yourself to an ESMTP server using EHLO
        smtp.login('tedt3830@gmail.com', password)  # Sender's email ID and password
        smtp.sendmail(sender_email, reciever_email, message)
        print('Check your email ;)')


sendMail()