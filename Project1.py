from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

path = "C:/Users/ACER/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"
s= Service(path)
driver= webdriver.Chrome(service=s)
driver.get("https://www.google.com/")
time.sleep(2)

box=driver.find_element_by_xpath('//*[@id="APjFqb"]')
box.send_keys("House of Dragon")
box.send_keys(Keys.ENTER)
time.sleep(3)

driver.find_element_by_xpath('//*[@id="kp-wp-tab-overview"]/div[4]/div/div/div/div/div/div[1]/div/div/span/a').click()
driver.save_screenshot('C:/Users/ACER/Documents/STUDIES/Skills/2. Web Scrapping/selenium/dragon.png')
time.sleep(2)