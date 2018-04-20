
import os
from selenium import webdriver
from browsermobproxy import Server
import urlparse 
import json
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import sys, re, time
import sqlite3



##################################Function Calls######################################
#retrieve cookie data from current page
def retrieve_cookies_domains():
    #connect to sql database
    file2 = open("chrome_adblockplus_cookie.txt","a")
    conn = sqlite3.connect('Results/Default/Cookies')
    db = conn.cursor()

    #retrieve all unique domains that set cookie on current page
    args = 'SELECT DISTINCT host_key FROM cookies'
    db.execute(args)
    results = db.fetchall()

    for result in results:
        print("%s"%(result[0]))
        file2.write(result[0]+" ")
        file2.flush()
    file2.write("\n")
    file2.flush()
    file2.close()

#import test websites
def import_testing_websites(number_websites_to_test, top1m_build, top1m_test):
    count = 0
    top1m = []
    with open('top-1m.txt') as f:
        top1m = f.readlines()
    for website in top1m:
        if count >= 4000:
            break
        if count < 2000:
            top1m_build.append(website)
            count = count + 1
            continue
        top1m_test.append(website)
        count = count + 1
        


##############################Main Program############################################
#path to git folder
env_path = "/Users/tianyuliu/Academics/CMU INI/2018 Spring/14828 - Browser Security/Project/CMU14836-project/"
env_path_2 = "/Users/tianyuliu/Academics/CMU\ INI/2018\ Spring/14828\ -\ Browser\ Security/Project/CMU14836-project/"
#paths to proxy
proxy_path = env_path + "browsermob-proxy-2.1.4/bin/browsermob-proxy"

#open a http proxy
server = Server(proxy_path)
server.start()
proxy = server.create_proxy()

#import testing websites 
number_websites_to_test = 2000
top1m_build = []
top1m_test = []
import_testing_websites(number_websites_to_test, top1m_build, top1m_test)

#Edit options for chrome
extension_path = env_path + "adblock_plus-3.0.2-an+fx.xpi"


#files to dump out tracking data
file1 = open("Testing Results/firefox_noDNT.txt","a")
file2 = open("Testing Results/firefox_noDNT_failedsites.txt","a")
#file2 = open("chrome_adblockplus_cookie.txt","w")
#file2.close()

#04/18/ 00:04am - 0-999
count = 0
#collect data from all websites

for website in top1m_test:
    
    #if count <=992:
        #count = count+1
        #continue
    if count <= 1028:
        count = count+1
        continue

    if count >= 2000:
        break


    #profile = webdriver.FirefoxProfile('/Users/tianyuliu/Library/Application Support/Firefox/Profiles/0k0cj8b8.noDNT')
    profile = webdriver.FirefoxProfile()
    profile.set_proxy(proxy.selenium_proxy())
    driver = webdriver.Firefox(firefox_profile=profile)
    #driver.install_addon(extension_path, temporary=True)
    driver.set_page_load_timeout(15)

    try:

        print(website.strip())

        #browse the website and quit
        url = "http://"+website.strip()

        proxy.new_har(options={'captureHeaders': True,'captureCookies': True }) #
        driver.get(url)
        driver.implicitly_wait(5)
        time.sleep(3)
        results = json.dumps(proxy.har)
        file1.write(results+"\n")
        file1.flush()

        driver.quit()
        #os.system("rm -rf " + env_path_2 + "/Results")
        time.sleep(1)
        count = count + 1
        #break
    except:
        file2.write(website)
        file2.flush()
        results = json.dumps(proxy.har)
        file1.write(results+"\n")
        file1.flush()
        driver.quit()
        time.sleep(1)
        count = count + 1

#stop server and close files
server.stop()
file1.close()
file2.close()


