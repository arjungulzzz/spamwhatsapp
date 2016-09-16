#import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import Select
driver=webdriver.Chrome('C:\\Users\\Arjun\\Downloads\\chromedriver.exe')
driver.get('http://web.whatsapp.com')
driver.implicitly_wait(25) # seconds
elem = driver.find_element_by_xpath('//*[@title="Aman Gulyani"]')
elem.click()
driver.implicitly_wait(5) # seconds
elem1 = driver.find_elements_by_class_name('input')
#elem1.click()
#print(elem1[1].text)
count=0
while (count<10):
	elem1[1].send_keys('Your whatsapp is hacked')
	#enter = driver.find_element_by_css_selector(".icon btn-icon icon-send send-container")
	#enter = driver.find_elements_by_xpath("//*[@class='icon btn-icon icon-send send-container']")
	#driver.find_elements_by_class_name('icon btn-icon icon-send send-container')
	enter = driver.find_element_by_class_name('send-container')
	enter.click()
	#pyautogui.press('enter') #enters on console.LoL
	#driver.find_element_by_class_name('send-container').click()
	count=count+1
