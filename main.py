import scrapers
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup

driver = scrapers.initialize(["no-sandbox","disable-dev-shm-usage"])
driver.get("https://nmap.org")
parags = driver.find_elements(By.TAG_NAME, "li")
for i in range(len(parags)):
    print(parags[i].text)

time.sleep(1)
scrapers.findAndClick(driver, "TAG_NAME", "a")