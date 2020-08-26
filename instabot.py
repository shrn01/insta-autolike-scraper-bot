from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as soup
import urllib.request



options = webdriver.ChromeOptions() 
options.add_argument("user-data-dir=C:\\Users\\shara\\AppData\\Local\\Google\\Chrome\\User Data\\Mr Noob") #Path to your chrome profile
browser = webdriver.Chrome( chrome_options=options)
num = 1
l = []
name = input('please enter the username\n')
# name = 'shrn'
browser.get('https://www.instagram.com/'+name)
browser.implicitly_wait(20)

# o = browser.find_element_by_xpath("//img[@alt = 'Change Profile Photo']")
# pp = o.get_attribute('innerHTML')
# for i in page.find_all('img'):
# 		k = i.get('src')
# 		print(k)
# 		print()
# 		js = name+str(num)+".jpg"
# 		print(js)
# 		print()
# 		if k!=None:
# 			num+=1
# 			urllib.request.urlretrieve(k,js)
# 		break

browser.find_element_by_css_selector('#react-root > section > main > div > div._2z6nI > article > div > div > div:nth-child(1) > div:nth-child(1) > a > div').click()
try:
	while(browser.find_element_by_css_selector('body > div._2dDPU.CkGkG > div.EfHg9 > div > div > a._65Bje.coreSpriteRightPaginationArrow')):
		a = browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[1]')
		page_source = a.get_attribute("innerHTML")
		page = soup(page_source,'html.parser')
		for i in page.find_all('img'):
			k = i.get('src')
			print(k)
			print()
			js = name+str(num)+".jpg"
			print(js)
			print()
			if k!=None:
				num+=1
				urllib.request.urlretrieve(k,js)
			# break
		try:
			while 1:
				browser.find_element_by_class_name('_6CZji').click()
				page_source = a.get_attribute("innerHTML")
				page = soup(page_source,'html.parser')
				print('scrolling for next in line')
				for i in page.find_all('img'):
					k = i.get('src')
					print(k)
					print()
					js = name+str(num)+".jpg"
					print(js)
					print()
					if k!=None:
						num+=1
						urllib.request.urlretrieve(k,js)
					# break
		except:
			print('done here')
		browser.find_element_by_xpath('html').send_keys(Keys.RIGHT)
		print('going for next image')
except:
	print('only one left')
	# if browser.find_element_by_css_selector('body > div._2dDPU.CkGkG > div.EfHg9 > div > div > a._65Bje.coreSpriteRightPaginationArrow')
a = browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[1]')
page_source = a.get_attribute("innerHTML")
page = soup(page_source,'html.parser')
for i in page.find_all('img'):
	k = i.get('src')
	print(k)
	js = name+str(num)+".jpg"
	print(js)
	if k!=None:
		num+=1
		urllib.request.urlretrieve(k,js)
try:
	while 1:
		browser.find_element_by_css_selector('body > div._2dDPU.CkGkG > div.zZYga > div > article > div._97aPb > div > div.pR7Pc > div.Igw0E.IwRSH.eGOV_._4EzTm.O1flK.D8xaz.fm1AK.TxciK.yiMZG > div > button'.click())
except:
	pass



