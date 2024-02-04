import smtplib, ssl, os
import requests
import env
from email.message import EmailMessage

URL = ('https://newsapi.org/v2/top-headlines?')

###NOTE SOME VARIABLES ARE HARD CODED FOR TESTING PURPOSES DO NOT UPLOAD TO GIT OR CLOUD WITH THEM

#
# ENVIRONMENT VARIABLES
#

def sendMail():
    dog_info = requests.get("https://api.thedogapi.com/v1/images/search?api_key={}".format(os.environ.get("dog_api"))).json()[0]
    dog_picture = dog_info["url"]
    news = get_artciles_by_category("general","us", os.environ.get("news_api"))
    wheather = get_weather("37.78, -79.44", os.environ.get("wheather_api"))
    form = os.environ.get("FORM")

    # sender_email = 'ted'
    # reciever_email = os.environ["RECIEVER"]  # receiver's email id
    # message = "Subject: Daily Check-in \n\n {} \n\n {} \n\n {}".format(os.environ.get("FORM"), news, dog_picture) # Content to be sent
    
    context = ssl.create_default_context()
    
    msg = EmailMessage()
    msg["Subject"] = "Daily Check"
    msg["From"] = os.environ.get("sender")
    msg["To"] = os.environ.get("RECIEVER")

    msg.set_content("{}".format(os.environ.get("FORM")))
    msg.add_alternative(f"Here is your dog! <br> <img src='{dog_picture}' width='500px'> <br><br> <p>{news}</p> <br> <p>{wheather}</p> <br>  <p>{form}</p>" , subtype = "html")

    with smtplib.SMTP(host='smtp.gmail.com', port = 587) as smtp:
        smtp.ehlo() # Identify yourself to an ESMTP server using EHLO
        smtp.starttls(context=context) # Put the SMTP connection in TLS (Transport Layer Security) mode
        smtp.ehlo() # Identify yourself to an ESMTP server using EHLO
        smtp.login(os.environ.get("sender"), os.environ.get("EMAIL_PASSWORD"))  # Sender's email ID and password
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
        article_string += "<br>"
    
    return article_string

def get_artciles_by_category(category, country,api):
    query_parameters = {
        "category": category,
        "sortBy": "top",
        "country": country,
        "apiKey": api
    }
    return _get_articles(query_parameters)

def get_weather(location, wheather_api):
    url = "https://api.tomorrow.io/v4/timelines"

    querystring = {
    "location": location,
    "fields":["temperature", "cloudCover"],
    "units":"metric",
    "timesteps":"1d",
    "apikey": wheather_api}

    response = requests.request("GET", url, params=querystring)
    t = response.json()['data']['timelines'][0]['intervals'][0]['values']['temperature']

    outputString = "Weather Forecast<br>"
    outputString += "================<br>"
    results = response.json()['data']['timelines'][0]['intervals']
    for daily_result in results:
        date = daily_result['startTime'][0:10]
        temp = round(daily_result['values']['temperature'])
        outputString += "On " + date + " it will be " + str(temp) + " C" + "<br>"
    
    return outputString

sendMail()