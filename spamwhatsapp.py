from selenium import webdriver
from selenium.webdriver.support.ui import Select
driver=webdriver.Chrome('C:\\Users\\Arjun\\Downloads\\chromedriver.exe')
driver.get('http://web.whatsapp.com')
input()
elem = driver.find_element_by_xpath('//*[@title="Aman Gulyani"]')
elem.click()
elem1 = driver.find_elements_by_class_name('input')
count=0
while (count>10):
	elem1[1].send_keys('Your whatsapp is hacked')
	driver.find_element_by_class_name('send-container').click()
	count=count+1
