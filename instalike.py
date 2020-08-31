from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as soup
import os
import time

print('-------Insta-Liker-v1.0-alpha-----------\n\nyou need to login for the first time \n\nyour login credentials stay on your device\n\n for login run the login script and login in the browser window that pops up\n')
name = input('please enter the username\n:>')
# name = 'shrn.js'
options = webdriver.ChromeOptions() 
options.add_argument("user-data-dir=C:\\Users\\shara\\AppData\\Local\\Google\\Chrome\\User Data\\Mr Noob") #Path to your chrome profile
# options.add_argument("--headless")
browser = webdriver.Chrome( chrome_options=options)
num = 1
l = []
# name = 'shrn'
browser.get('https://www.instagram.com/'+name)
browser.implicitly_wait(10)

try:
	browser.find_element_by_class_name('rkEop')
	os.system('cls')
	print('This Account is Private')
	time.sleep(5)
	quit()
except:
	# os.system('cls')
	browser.find_element_by_css_selector('#react-root > section > main > div > div._2z6nI > article > div > div > div:nth-child(1) > div:nth-child(1) > a > div').click()
	try:
		while(True):
			k = browser.find_element_by_class_name('fr66n')
			piece = k.get_attribute('innerHTML')
			page = soup(piece,'html.parser')
			t = page.find('svg').get('aria-label')
			if t != 'Unlike':
				browser.find_element_by_class_name('fr66n').click()
			browser.find_element_by_css_selector('body > div._2dDPU.CkGkG > div.EfHg9 > div > div > a._65Bje.coreSpriteRightPaginationArrow').click()
	except:
		print('mission accomplished, now Bye')
		time.sleep(4)
		quit()