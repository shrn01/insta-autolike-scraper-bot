from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as soup
import urllib.request
import os

print('-------Insta-login-v1.0-alpha-----------\n you need to login for the first time \n your login credentials stay on your device\n')
# name = input('please enter the username\n:>')

options = webdriver.ChromeOptions() 
options.add_argument("user-data-dir=C:\\Users\\shara\\AppData\\Local\\Google\\Chrome\\User Data\\Mr Noob") #Path to your chrome profile
# options.add_argument("--headless")
browser = webdriver.Chrome( chrome_options=options)
browser.get('https://www.instagram.com/')
browser.implicitly_wait(200)