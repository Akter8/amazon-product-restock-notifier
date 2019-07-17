# Changes to be made before use:
#     . Make the necessary changes in the URL.
#     . Update your "User-Agent" in headers.
#     . Enable Google Apps passwords for mail, and update it in the code on line 54
#     . Update your email from which the mail has to be sent.
#     . Update your email to which you want the mail to be sent.
#     . Make whatever changes you want to the message.
#     . Change the frequency at which you want to run the script.
#     . You are all done! You can run this script now!

#	. If you want to run this script on startup in Windows, make a batch file
#	Learn how to make a batch file from here https://datatofish.com/batch-python-script/
# 	Now, open Run, and execute this 'shell:common startup' and paste your batch file in there.


# Libraries required for the web-scraping.
import requests
from bs4 import BeautifulSoup

# Library required to send the email.
import smtplib

# Library to run the program over time.
import time


#Get data
data = {}
file = open('pars.txt', "r")
for f in file:
    [a, b] = f.split('=', 1)
    data[a] = b[:-1]

# You can use any Amazon product's URL.
url = data['url']

headers = {
    # Google "my user agent" and paste the value you get.
    "User-Agent": data['user_agent'],
    # This is so as to remove the cache that was previously stored, as otherwise even if the website has updated, it would not show up.
    'Cache-Control': 'no-cache',
    "Pragma": "no-cache"
}


def checkAvailablity():
    try:
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        # The data is stored in a div with ID as 'availability'
        availablity = soup.find(id="availability").get_text().strip()
        availablity = availablity.split('\n')
        if availablity[0] == "In stock.":
            price = soup.find(id='priceblock_ourprice')
            sendMail(price)
    except requests.exceptions.ConnectionError:
        time.sleep(5)


def sendMail(price):
    price = str(price)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    # Change this before use.
    # Example:
    #		server.login("abcd@gmail.com", "lndhrbjcwfqgddfdd")
    server.login(data['login'], data['pass'])
    subject = 'Amazon item has been restocked!!'
    price = price.split('>', 1)[1][1:].split('<', 1)[0][1:]
    body = 'The item you have been waiting for has been restocked. The price is ' + price + '. Check this link out ' + url
    message = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        data['login'],
        data['target'],
        message
    )
    server.quit()


while True:
    checkAvailablity()
    time.sleep(60 * 60 * 24)
