import sys
import time
import glob
import os
import pyotp
import re
import random
import pandas as pd
import pymysql
import configparser
from datetime import date, datetime, timedelta
from tabulate import tabulate
from IPython.display import display
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from amazoncaptcha import AmazonCaptcha
from pyshadow.main import Shadow
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from datetime import datetime, timedelta
from  itertools import repeat
from selenium.webdriver.support.ui import Select

service = Service(r"C:\Users\LENOVO\Desktop\amz_download\chromedriver.exe")
driver = webdriver.Chrome(service=service)
print('Start')
driver.maximize_window()
driver.get("https://www.amazon.in/")

def handle_captcha():
    captcha_text = "we just need to make sure you're not a robot"
    n=5
    for i in range(0,n):
        if captcha_text in driver.page_source:
            print("Handling Captcha...")
            img_element = driver.find_element(By.CSS_SELECTOR, '.a-row.a-text-center img')
            img_url = img_element.get_attribute('src')
            print(img_url)
            captcha = AmazonCaptcha.fromlink(img_url)
            solution = captcha.solve()
            print('solution : ', solution)
            driver.find_element(By.ID, "captchacharacters").send_keys(str(solution))
            time.sleep(2)
            driver.find_element(By.CSS_SELECTOR, ".a-button-inner").click()
            time.sleep(3)
        else:
            print("No Captcha :) ")
            break    

# sign_in = '/html/body' 
# driver.find_elements(By.XPATH,'/html/body').click()      
# Using find_elements instead of find_element
sign_in_elements = driver.find_elements(By.XPATH, "/html/body/div[1]/header/div/div[1]/div[3]/div/a[2]/div/span")

# Check if any elements are found
if sign_in_elements:
    # Click on the first element in the list
    sign_in_elements[0].click()
else:
    print("Sign-in element not found.")

# /html/body/div[1]/div[1]/div[2]/div/div[2]/div[2]/div[1]/form/div/div/div/div[1]/input[1]
email = 'Enter Your Mail Id'
driver.find_element(By.XPATH, " /html/body/div[1]/div[1]/div[2]/div/div[2]/div[2]/div[1]/form/div/div/div/div[1]/input[1]").send_keys(email)
# time.sleep(5)

# Assuming you want to find elements by ID with the identifier 'continue'
elements = driver.find_elements(By.ID, 'continue')

# Check if any elements are found
if elements:
    # Click on the first element in the list
    elements[0].click()
else:
    print("Element not found.")

Password = "Enter Your Password"
driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div[2]/div/form/div/div[1]/input").send_keys(Password)
# time.sleep(5)

# Assuming you want to find elements by ID with the identifier 'continue'
elements = driver.find_elements(By.ID, 'signInSubmit')

# Check if any elements are found
if elements:
    # Click on the first element in the list
    elements[0].click()
else:
    print("Element not found.")

time.sleep(15)  
elements = driver.find_elements(By.ID, 'auth-signin-button') 
# Check if any elements are found
if elements:
    # Click on the first element in the list
    elements[0].click()
else:
    print("Element not found.")    
item_search = "redmi note 13 pro"
driver.find_element(By.XPATH, "/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input").send_keys(item_search)
# time.sleep(5)

# Assuming you want to find elements by ID with the identifier 'continue'
elements = driver.find_elements(By.ID, 'nav-search-submit-button')

# Check if any elements are found
if elements:
    # Click on the first element in the list
    elements[0].click()
else:
    print("Element not found.")    

# Assuming you want to find elements by ID with the identifier 'continue'
elements = driver.find_elements(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/span/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[3]/span/div/div[1]/form/span/div/div/span')

# Check if any elements are found
if elements:
    # Click on the first element in the list
    elements[0].click()
else:
    print("Element not found.")        
    
time.sleep(10)
