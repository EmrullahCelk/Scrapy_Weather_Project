import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import json
from urllib.request import urlopen

url = "https://ipinfo.io/"
response = urlopen(url)
data = json.load(response)

location = data['city']
degree =f"https://www.google.com/search?q={location}+s%C4%B1cakl%C4%B1k"

print(location)

s = Service("C:\chromedriver.exe")
driver = webdriver.Chrome(service=s)
url1 = f"https://www.google.com/search?q={location}+s%C4%B1cakl%C4%B1k"

driver.get(url1)
driver.maximize_window()
time.sleep(5)

url = "https://openweathermap.org/weather-conditions"

driver.get(url)
x=5


time.sleep(x)
driver.maximize_window()
driver.find_element(By.XPATH, '//button[text()="Some text"]')
m=driver.find_element(By.XPATH, '/html/body/main/div[2]/div/div[1]/table[1]/tbody/tr[2]/td[1]/text()')
m = driver.find_element_by_xpath("/html/body/main/div[2]/div/div[1]/table[1]/tbody/tr[2]/td[1]/text()")

print(m)

driver.find_element_by_xpath("/html/body/main/div[2]/div/div[1]/table[1]/tbody/tr[3]/td[1]/text()")

x=5
# driver.get(url+"account/login.html?redirectUrl=/nl/rnwy/account/overzicht")

time.sleep(x)
driver.find_element_by_css_selector('.OdtSme').click()
# driver.back() # onceki sayfaya don

time.sleep(x)
# driver.forward() # sonraki sayfa

# driver.save_screenshot("ekran_goruntusu.png") # png dosyasi olustu
# print(driver.title)
driver.find_element_by_css_selector('.widget-scene-canvas').click()
time.sleep(x)

