
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import sys, re, time
import sqlite3

#retrieve cookie data from current page
def retrieve_cookies():
    #connect to sql database
    conn = sqlite3.connect('Results/Default/Cookies')
    db = conn.cursor()

    #retrieve all unique domains that set cookie on current page
    args = 'SELECT DISTINCT host_key FROM cookies'
    db.execute(args)
    results = db.fetchall()

    for result in results:
        print("%s"%(result[0]))


#10 types - News, Sports, Shopping, Games, Computers, Adult, Science, Recreation, Health, Home
Alexa_websites = []
with open('alexa_top100.txt') as f:
    Alexa_websites = f.readlines()

#path to git folder
env_path = "/Users/tianyuliu/Academics/CMU INI/2018 Spring/14828 - Browser Security/Project/CMU14836-project/"
env_path_2 = "/Users/tianyuliu/Academics/CMU\ INI/2018\ Spring/14828\ -\ Browser\ Security/Project/CMU14836-project/"
#paths to chrome webdriver and extension
chromedriver_path = env_path + "chromedriver"
extension_path = "/Users/tianyuliu/Library/Application Support/Google/Chrome/Default/Extensions/cfhdojbkjhnklbpkdaibdccddilifddb/"


chop = Options()
chop.add_extension('Adblock-Plus_v1.13.5.crx')
chop.add_argument("--user-data-dir=Results")
time.sleep(3)

for website in Alexa_websites:

    print(website)

    #browse the website and quit
    driver = webdriver.Chrome(executable_path=chromedriver_path, chrome_options = chop)

    driver.get(website)
    driver.implicitly_wait(3)  
    time.sleep(2)
    driver.quit()
    
    #retrieve all the cookies
    retrieve_cookies()
    os.system("rm -rf " + env_path_2 + "/Results")
    #break


