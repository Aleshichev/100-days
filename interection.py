from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

signup = 'http://secure-retreat-92358.herokuapp.com/'
xpath = '//*[@id="articlecount"]/a[1]'
web_page = 'https://en.wikipedia.org/wiki/Main_Page'

chrome_drive_path = "C:\\Web development\\chromedriver_win32\\chromedriver.exe"
s = Service('C:\Web development\chromedriver_win32\chromedriver.exe')
driver = webdriver.Chrome(service=s)

driver.get(signup)
# article_count = driver.find_element(By.XPATH, xpath)
# print(article_count.text)
# article_count.click()          # нажимает на ссылку
# anyone = driver.find_element_by_link_text("anyone can edit.")
# anyone = driver.find_element(By.LINK_TEXT, 'anyone can edit')     # поиск для ссылок
# anyone.click()
# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)        #любая клавиша - ключ

search = driver.find_element(By.NAME, "fName")
search.send_keys("Cris")

search = driver.find_element(By.NAME, "lName")
search.send_keys("Americos")

search = driver.find_element(By.NAME, "email")
search.send_keys("Americos@yahoo.com")

search.send_keys(Keys.ENTER)
#
# driver.close()
# driver.quit()





