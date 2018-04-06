
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import sys, re, time

#10 types - News, Sports, Shopping, Games, Computers, Adult, Science, Recreation, Health, Home
Alexa_websites = []
with open('alexa_top100.txt') as f:
    Alexa_websites = f.readlines()

chromedriver_path = "/Users/tianyuliu/Academics/CMU INI/2018 Spring/14828 - Browser Security/Project/Scripts/chromedriver"
extension_path = "/Users/tianyuliu/Library/Application Support/Google/Chrome/Default/Extensions/cfhdojbkjhnklbpkdaibdccddilifddb/"

chop = Options()
chop.add_extension('Adblock-Plus_v1.13.5.crx')
driver = webdriver.Chrome(executable_path=chromedriver_path, chrome_options = chop)
time.sleep(5)

for website in Alexa_websites:
    driver.get(website)
    driver.implicitly_wait(5)  
    time.sleep(3)  

driver.quit()
