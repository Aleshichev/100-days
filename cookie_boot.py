from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


timeout = time.time() + 2       #секунды
two_min = time.time() + 60*2            # 5minutes

click_cookie = '//*[@id="cookie"]'
money_cookie = '//*[@id="money"]'
price_cake = '//*[@id="buyCursor"]/b/text()[2]'
grendma_price = '//*[@id="buyGrandma"]/b/moni'
cursor_background = '//*[@id="buyCursor"]'

web_page = 'http://orteil.dashnet.org/experiments/cookie/'

s = Service('C:\Web development\chromedriver_win32\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get(web_page)
# print(web_page)

# find_money =
money = int(driver.find_element(By.XPATH, money_cookie).text)
print(money)
price = int(driver.find_element(By.ID, "buyCursor").text.split()[2])
print(price)
grendma = int(driver.find_element(By.ID, "buyGrandma").text.split()[2])
print(grendma)

find_cookie = driver.find_element(By.XPATH, click_cookie)

find_cookie.click()

while two_min > time.time():
    find_cookie.click()
    money = int(driver.find_element(By.XPATH, money_cookie).text)
    if time.time() > timeout:
        if money > grendma:
            grendma_click = driver.find_element(By.XPATH, '//*[@id="buyGrandma"]')
            grendma_click.click()
        elif money > price:
            curr_bk = driver.find_element(By.XPATH, cursor_background)
            curr_bk.click()
        timeout = time.time() + 2
    cookie_second = driver.find_element(By.ID, "cps").text
print(cookie_second)

driver.quit()

