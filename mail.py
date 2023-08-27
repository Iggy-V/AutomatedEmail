import smtplib, ssl, os
import requests
from email.message import EmailMessage

URL = ('https://newsapi.org/v2/top-headlines?')

###NOTE SOME VARIABLES ARE HARD CODED FOR TESTING PURPOSES DO NOT UPLOAD TO GIT OR CLOUD WITH THEM


def sendMail():
    dog_info = requests.get("https://api.thedogapi.com/v1/images/search?api_key={}".format(dog_api)).json()[0]
    dog_picture = dog_info["url"]
    news = get_artciles_by_category("general","lt")



    sender_email = 'ted'
    reciever_email = os.environ.get("RECIEVER") # receiver's email id
    message = "Subject: Daily Check-in \n\n {} \n\n {} \n\n {}".format(os.environ.get("FORM"), news, dog_picture) # Content to be sent
    context = ssl.create_default_context()
    
    msg = EmailMessage()
    msg["Subject"] = "Daily Check"
    msg["From"] = "tedt3830@gmail.com"
    msg["To"] = os.environ.get("RECIEVER")

    msg.set_content("{}".format(os.environ.get("FORM")))
    msg.add_alternative(f"Here is your dog! \n <img src='{dog_picture}' width='500px'> \n <p>{news}</p> " , subtype = "html")

    with smtplib.SMTP(host='smtp.gmail.com', port = 587) as smtp:
        smtp.ehlo() # Identify yourself to an ESMTP server using EHLO
        smtp.starttls(context=context) # Put the SMTP connection in TLS (Transport Layer Security) mode
        smtp.ehlo() # Identify yourself to an ESMTP server using EHLO
        smtp.login('tedt3830@gmail.com', os.environ.get("EMAIL_PASSWORD"))  # Sender's email ID and password
        #smtp.sendmail(sender_email, reciever_email, message)
        smtp.send_message(msg)
        print('Check your email ;)')

def _get_articles(params):
    response = requests.get(URL, params=params)

    articles = response.json()['articles']

    results = []
    i = 0
    for article in articles:
        results.append({"title": article["title"], "url": article["url"]})
        i += 1
        if i == 3:
            break 
    
    article_string = ""
    for result in results:
        article_string += result['title']
        article_string += result['url']
        article_string += "\n"
    
    return article_string

def get_artciles_by_category(category, country):
    query_parameters = {
        "category": category,
        "sortBy": "top",
        "country": country,
        "apiKey": API_KEY
    }
    return _get_articles(query_parameters)

sendMail()