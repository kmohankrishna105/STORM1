#-*- coding: utf-8 -*-
#driver.find_element_by_xpath(//h1[text(),"This site can’t be reached"])



from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import win32com.client


driver=webdriver.Chrome()
driver.get("http:www.paytm.com")

driver.maximize_window()

"""

try:
    driver.get("http://13.76.210.179:5555//MCCPreUAT/")
    time.sleep(6)
    no_access=driver.find_element_by_xpath("//h1[text()='This site can’t be reached']")
    if not no_access.is_displayed():
        print ("Access Granted")
    else:
        raise Exception
except:
    print("Network not reachable , please plug in ethernet card")
    #print(driver.execute_script("windows.alert='Please check connection'):")


aler=driver.switch_to().alert()
aler.send_keys("hai")
time.sleep(2)
aler.send_keys(Keys.TAB)
time.sleep(2)
aler.send_keys("Different")
time.sleep(2)
aler.accept()


shell=win32com.client.Dispatch("WScript.Shell")
time.sleep(2)
shell.Send_keys("user")
"""

#assert "Paytm.com – Digital & Utility Payment, Entertainment, Travel, Payment Gateway & more Online !" in driver.title
#   driver.find_element_by_xpath("//button[@class='_3y9b  _1wLi _2vdF']").send_keys(Keys.PAGE_DOWN)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

d=driver.find_elements_by_xpath("//h1")
for name in d:
    print name.text

print ("==========================================================")
d1=driver.find_elements_by_xpath("//h2")
for name in d1:
    print name.text

f=driver.get_cookies()
for g in f:
    print g


time.sleep(100)
f1=driver.get_cookies()
for g1 in f1:
    print g1
