from selenium import webdriver
username = 'USERNAME'
password = 'PASSWORD'
url = 'https://www.facebook.com/'
driver = webdriver.Chrome('path for chromedriver.exe file')  
driver.get(url)
driver.find_element_by_id('email').send_keys(username)
driver.find_element_by_id('pass').send_keys(password)
driver.find_element_by_id('loginbutton').click()
 
