from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import time

#We can do the Web scraping part using directly Selenium Webdriver. However, for better practice and for better
#practice using BeautifulSoup is better while scraping a website.

# driver1 = webdriver.Edge()
# driver1.get(url="https://appbrewery.github.io/Zillow-Clone/")

# prices = []
# addresses = []
# links = []
# for i in range(1, 45):
#     prices.append(driver1.find_element(By.XPATH, f'/html/body/div/div[2]/div/div/div[1]/div[1]/div/ul/li[{i}]/div/div/article/div/div[1]/div[2]/div/span').text)
#     addresses.append(driver1.find_element(By.XPATH, f'/html/body/div/div[2]/div/div/div[1]/div[1]/div/ul/li[{i}]/div/div/article/div/div[1]/a/address').text)
#     links.append(driver1.find_element(By.XPATH, f'/html/body/div/div[2]/div/div/div[1]/div[1]/div/ul/li[{i}]/div/div/article/div/div[2]/div[2]/a').get_attribute("href"))

#Scraping the required data using BS.
response    = requests.get(url="https://appbrewery.github.io/Zillow-Clone/")
response.raise_for_status()

soup        = BeautifulSoup(response.text, "html.parser")

all_links_tags  = soup.find_all("a", attrs={"class": "property-card-link"})
links           = []
for link_tag in all_links_tags:
    links.append(link_tag.get("href"))

all_prices_tags = soup.find_all("span", attrs={"class": "PropertyCardWrapper__StyledPriceLine"})
prices          = []
for price_tag in all_prices_tags:
    prices.append(price_tag.text)

all_addresses_tags = soup.find_all("address", attrs={"data-test": "property-card-addr"})
addresses          = []
for address_tag in all_addresses_tags:
    addresses.append(address_tag.text.strip())

#Opening the google form in order to fill all the previously found data
google_form_driver_options  = webdriver.EdgeOptions()
google_form_driver_options.add_experimental_option("detach", True)

google_form_driver          = webdriver.Edge(options=google_form_driver_options)
google_form_driver.get(url="https://docs.google.com/forms/d/e/1FAIpQLScer5tp1oVRs_hAHFF6YdWxT8F_fyipVAaXdnj8_qbNJAXvBg/viewform")

#Filling up the form one by one into the google forms. NOTE: the time.sleep(1) is just for good practice to better visualize the results while giving some delay to the Operating System.
for _ in range(min(min(len(links), len(prices)), len(addresses))):
    text_areas                   = google_form_driver.find_elements(By.XPATH, '//textarea[@jsname="YPqjbf"]')
    submit_button                = google_form_driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div')

    text_areas[0].click()
    time.sleep(1)
    text_areas[0].send_keys(addresses[_])
    time.sleep(1)
    text_areas[1].click()
    time.sleep(1)
    text_areas[1].send_keys(prices[_])
    time.sleep(1)
    text_areas[2].click()
    time.sleep(1)
    text_areas[2].send_keys(links[_])
    time.sleep(1)
    submit_button.click()
    time.sleep(3)
    back_to_form_link = google_form_driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    back_to_form_link.click()
    time.sleep(1)

