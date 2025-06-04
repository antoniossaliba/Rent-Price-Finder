from bs4 import BeautifulSoup
import requests
from smtplib import *
import os
from pprint import pprint

headers = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0"
}

parameters = {
    "crid": "2MEP0EZYFWPY2",
    "dib": "eyJ2IjoiMSJ9.Gpt6XxqEyVuxHs0YaQSRwd6SEDubk216-upXOpY9zDY4Tx79ceaQo58B4NB-209OKKqQR8Srt1MOglWFuWy1FknmfQlI2SnylJjdSmU7bu2YvnzzT1IA0RewUlfNsqbunKSVzqhDUnwbFWUHULxlDHapwzpyFux_QnndVlMhzcoALzT5kPcx5QT7FuUsDaw5gpJhfTzRhX-4b3xwsF8VCr_sJiV46dDp-8vgFPNXsMk.1J3W_yI86X_xNW_FLkEuXiSjGn-XDyS1AkwAVHfNDJw",
    "dib_tag": "se",
    "keywords": "data+structures+and+algorithms+in+java",
    "qid": "1748889465",
    "sprefix": "Data+structures+%2Caps%2C296",
    "sr": "8-1"
}

response = requests.get(url="https://www.amazon.com/Data-Structures-Algorithms-Java-2nd/dp/0672324539/ref=sr_1_1",
                        headers=headers,
                        params=parameters)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

title = soup.find("span", attrs={"id": "productTitle"})
price = soup.find("span", attrs={"class": "a-price-whole"})
the_price = str()
the_price += price.text
the_price += soup.find("span", attrs={"class": "a-price-fraction"}).text
the_price = float(the_price)

title = title.text.replace("é", "e").strip()

if the_price < 100:
    with SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=f"{os.environ.get('email')}", password=f"{os.environ.get('password')}")
        connection.sendmail(from_addr=f"{os.environ.get('email')}",
                            to_addrs=f"{os.environ.get('email')}",
                            msg=f"Subject: Price Detected!\n\nNOW: {title}\nPRICE AT: ${the_price}. HURRY!")