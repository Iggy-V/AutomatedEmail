import smtplib, ssl, os
import requests

URL = ('https://newsapi.org/v2/top-headlines?')

###NOTE SOME VARIABLES ARE HARD CODED FOR TESTING PURPOSES DO NOT UPLOAD TO GIT OR CLOUD WITH THEM


def sendMail():
    news = get_artciles_by_category("general","lt")



    sender_email = 'ted'
    reciever_email = 'ignasvolcokas@gmail.com' # receiver's email id
    message = "Subject: Daily Check-in \n\n {} \n\n {}".format(os.environ.get("FORM"), news) # Content to be sent
    context = ssl.create_default_context()
    


    with smtplib.SMTP(host='smtp.gmail.com', port = 587) as smtp:
        smtp.ehlo() # Identify yourself to an ESMTP server using EHLO
        smtp.starttls(context=context) # Put the SMTP connection in TLS (Transport Layer Security) mode
        smtp.ehlo() # Identify yourself to an ESMTP server using EHLO
        smtp.login('tedt3830@gmail.com', os.environ.get("EMAIL_PASSWORD"))  # Sender's email ID and password
        smtp.sendmail(sender_email, reciever_email, message)
        print('Check your email ;)')

def _get_articles(params):
    response = requests.get(URL, params=params)

    articles = response.json()['articles']

    results = []
        
    for article in range(0,3):
        results.append({"title": article["title"], "url": article["url"]})

    article_string = ""
    for result in results:
        article_string += result['title']
        article_string += result['url']
        article_string += ""
    
    return article_string.encode('utf-8')

def get_artciles_by_category(category, country):
    query_parameters = {
        "category": category,
        "sortBy": "top",
        "country": country,
        "apiKey": API_KEY
    }
    return _get_articles(query_parameters)

sendMail()