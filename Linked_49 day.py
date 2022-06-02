# https://www.linkedin.com/jobs/search/?geoId=102264497&keywords=python%20developer&location=Ukraine

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time

signup = 'http://secure-retreat-92358.herokuapp.com/'
enter_xpath = '/html/body/div[1]/header/nav/div/a[2]'
web_page = 'https://www.linkedin.com/jobs/search/?geoId=102264497&keywords=python%20developer&location=Ukraine'

s = Service('C:\Web development\chromedriver_win32\chromedriver.exe')
driver = webdriver.Chrome(service=s)

driver.get(web_page)

enter_page = driver.find_element(By.XPATH, enter_xpath)
enter_page.click()
time.sleep(2)

enter_name = driver.find_element(By.XPATH, '//*[@id="username"]')
enter_name.send_keys("Aleshichevigor@outlook.com")

enter_password = driver.find_element(By.XPATH, '//*[@id="password"]')
enter_password.send_keys("9i8u7y6t")

enter_page2 = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
enter_page2.click()

links_list = driver.find_elements(By.CSS_SELECTOR, '.artdeco-entity-lockup__title a')

for link in links_list:
    try:
        link.click()
        time.sleep(2)
        button_save = driver.find_element(By.CSS_SELECTOR, '.jobs-save-button span')
        time.sleep(2)
        button_save.click()
    except ElementClickInterceptedException:
        print("XZ")
        continue


driver.quit()