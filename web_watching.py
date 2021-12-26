# coding: utf-8

import smtplib
import requests
import os
import hashlib
from bs4 import BeautifulSoup

MY_EMAIL = "*********@gmail.com"
MY_PASSWORD = "**********"
URL = "https://*******/ir/"
PATH = "/Users/********/web_SHA.txt"


response = requests.get(URL)
soup = BeautifulSoup(response.content, "html.parser")
response_SHA = hashlib.md5(soup.encode()).hexdigest()

with open(PATH, mode='r+') as previous_web_SHA:
    previous_web_SHA_text = previous_web_SHA.readline()
    if previous_web_SHA_text == response_SHA:
        pass

    else:
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject:IR is changed"
    )

        previous_web_SHA.write(response_SHA)
